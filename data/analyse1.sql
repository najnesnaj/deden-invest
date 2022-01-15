BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "analyse1" (
	"URL"	TEXT PRIMARY KEY,
	"classificatie"	INTEGER,
	"ISIN-code financieel instrument"	TEXT,
	"Soort transactie"	TEXT,
	"Totaal bedrag"	REAL,
	"Prijs" REAL
);
COMMIT;
