BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "compinfo" (
	"symbol" TEXT PRIMARY KEY,
	"sector"	TEXT,
	"why I bought it"	TEXT,
	"when to buy"	TEXT,
	"when to sell"	TEXT,
	"date buy" TEXT,
	"date sell" TEXT,
	"shares bought" REAL,
	"shares sold" REAL,
	"why go up?"	TEXT,
	"evaluation/profit/loss" TEXT,
	"extra" TEXT
);
COMMIT;
