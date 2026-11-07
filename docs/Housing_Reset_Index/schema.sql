PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS sources (
  id INTEGER PRIMARY KEY,
  path TEXT UNIQUE NOT NULL,
  sha256 TEXT,
  size INTEGER,
  mtime TEXT,
  title TEXT,
  author TEXT,
  date TEXT,
  keywords TEXT,
  ext TEXT,
  text_excerpt TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS sources_fts USING fts5(
  text,
  content='sources',
  content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS sources_ai AFTER INSERT ON sources BEGIN
  INSERT INTO sources_fts(rowid, text) VALUES (new.id, new.text_excerpt);
END;

CREATE TRIGGER IF NOT EXISTS sources_ad AFTER DELETE ON sources BEGIN
  INSERT INTO sources_fts(sources_fts, rowid, text) VALUES('delete', old.id, old.text_excerpt);
END;

CREATE TRIGGER IF NOT EXISTS sources_au AFTER UPDATE ON sources BEGIN
  INSERT INTO sources_fts(sources_fts, rowid, text) VALUES('delete', old.id, old.text_excerpt);
  INSERT INTO sources_fts(rowid, text) VALUES (new.id, new.text_excerpt);
END;
