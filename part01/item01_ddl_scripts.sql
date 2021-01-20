-- sandbox.db

CREATE TABLE todo (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    is_completed INTEGER
);