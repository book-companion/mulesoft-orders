#!/usr/bin/env python3
"""Loopback teaching dependencies; synthetic data only, Python standard library."""
import argparse
import json
import sqlite3
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

CATALOGUE = {"PEN-01": 2.5, "PAD-22": 6, "CLP-08": 1}
LOCK = threading.Lock()
COUNTS = {}
CONTROL = {"failNext": 0, "loseResponseNext": False}


class Handler(BaseHTTPRequestHandler):
    def reply(self, status, value):
        body = json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except BrokenPipeError:
            pass  # A timeout example deliberately abandons the response.

    def log_message(self, fmt, *args):
        pass  # Request counts below are sufficient; never log bodies or credentials.

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/control/state":
            with LOCK, sqlite3.connect(self.server.database) as db:
                events = [json.loads(row[0]) for row in db.execute("SELECT body FROM events ORDER BY event_id")]
                return self.reply(200, {"calls": dict(COUNTS), "events": events, "effects": len(events)})
        with LOCK:
            COUNTS[path] = COUNTS.get(path, 0) + 1
        if path == "/catalogue":
            tenant = parse_qs(parsed.query).get("tenant", ["retailer-a"])[0]
            prices = dict(CATALOGUE)
            if tenant == "retailer-b":
                prices["PEN-01"] = 3
            return self.reply(200, prices)
        if path == "/customers/C-42":
            return self.reply(200, {"id": "C-42", "name": "Dana", "status": "ACTIVE"})
        if path == "/shipping/unavailable":
            return self.reply(503, {"error": "SHIPPING_UNAVAILABLE"})
        if path == "/slow":
            time.sleep(3)
            return self.reply(200, {"arrived": True})
        if path == "/flaky":
            with LOCK:
                if CONTROL["failNext"]:
                    CONTROL["failNext"] -= 1
                    return self.reply(503, {"error": "TRY_AGAIN"})
            return self.reply(200, {"available": True})
        return self.reply(404, {"error": "NOT_FOUND"})

    def do_POST(self):
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))) or b"{}")
        except (ValueError, TypeError):
            return self.reply(400, {"error": "INVALID_JSON"})
        path = urlparse(self.path).path
        with LOCK:
            if path == "/control/reset":
                COUNTS.clear()
                CONTROL.update(failNext=0, loseResponseNext=False)
                with sqlite3.connect(self.server.database) as db:
                    db.execute("DELETE FROM events")
                return self.reply(200, {"reset": True})
            if path == "/control":
                CONTROL.update({k: body[k] for k in CONTROL if k in body})
                return self.reply(200, dict(CONTROL))
            if path != "/events":
                return self.reply(404, {"error": "NOT_FOUND"})
            COUNTS[path] = COUNTS.get(path, 0) + 1
            if CONTROL["failNext"]:
                CONTROL["failNext"] -= 1
                return self.reply(503, {"error": "RECEIVER_UNAVAILABLE"})
            if not isinstance(body, dict) or not isinstance(body.get("eventId"), str):
                return self.reply(400, {"error": "EVENT_ID_REQUIRED"})
            encoded = json.dumps(body, sort_keys=True, separators=(",", ":"))
            # The durable row IS this teaching receiver's business effect. A real
            # receiver must commit its own effect and processed ID together.
            with sqlite3.connect(self.server.database) as db:
                previous = db.execute("SELECT body FROM events WHERE event_id = ?", (body["eventId"],)).fetchone()
                if previous and previous[0] != encoded:
                    return self.reply(409, {"error": "EVENT_CONFLICT"})
                db.execute("INSERT OR IGNORE INTO events(event_id,body) VALUES (?,?)", (body["eventId"], encoded))
            if CONTROL["loseResponseNext"]:
                CONTROL["loseResponseNext"] = False
                # Simulate an acknowledged transport failure AFTER committing.
                return self.reply(503, {"error": "RESPONSE_LOST_AFTER_COMMIT"})
            return self.reply(200, {"eventId": body["eventId"], "duplicate": previous is not None})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=18882)
    parser.add_argument("--database", type=Path, default=Path(__file__).parents[1] / ".state" / "receiver.sqlite")
    args = parser.parse_args()
    args.database.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(args.database) as db:
        db.execute("CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY, body TEXT NOT NULL)")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.database = args.database
    print(f"Teaching dependencies: http://127.0.0.1:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
