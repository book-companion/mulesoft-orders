SELECT id, updated_at, total
FROM orders
WHERE updated_at > :last_time
   OR (updated_at = :last_time AND id > :last_id)
ORDER BY updated_at, id
LIMIT :page_size
