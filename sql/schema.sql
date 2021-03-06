DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS usr;

CREATE TABLE usr (
  id SERIAL PRIMARY KEY NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id SERIAL PRIMARY KEY NOT NULL,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES usr (id)
);

SELECT version();
