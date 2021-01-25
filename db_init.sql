DROP TABLE IF EXISTS pizero;
CREATE TABLE temperature (
	celsius VARCHAR(10) NOT NULL,
	timestamp DATETIME DEFAULT (DATETIME('now', 'localtime'))
);
