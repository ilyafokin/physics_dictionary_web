DROP TABLE IF EXISTS acronyms;

CREATE TABLE acronyms (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  acronym TEXT UNIQUE NOT NULL,
  descr TEXT NOT NULL,
  webpage TEXT NOT NULL,
  tags TEXT NOT NULL
);