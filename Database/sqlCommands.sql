CREATE TABLE IF NOT EXISTS Data (
    unit_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    address TEXT NOT NULL,
    consumption INTEGER NOT NULL,
    month TEXT NOT NULL
);