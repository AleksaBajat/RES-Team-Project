CREATE TABLE IF NOT EXISTS meterReadings (
    unit_id INTEGER,
    user_id INTEGER NOT NULL,
    consumption INTEGER NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    street TEXT NOT NULL,
    street_number INTEGER NOT NULL,
    month TEXT NOT NULL
);