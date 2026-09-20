CREATE TABLE IF NOT EXISTS accepted_orders (tenant_id VARCHAR(40), order_id VARCHAR(40), response TEXT NOT NULL, PRIMARY KEY(tenant_id,order_id));
CREATE TABLE IF NOT EXISTS request_results (tenant_id VARCHAR(40), request_key VARCHAR(40), fingerprint TEXT NOT NULL, response TEXT NOT NULL, PRIMARY KEY(tenant_id,request_key));
CREATE TABLE IF NOT EXISTS outbox (event_id VARCHAR(100) PRIMARY KEY, body TEXT NOT NULL, sent BOOLEAN DEFAULT FALSE NOT NULL);
