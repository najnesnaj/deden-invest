BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "garpinfo" (
	"symbol" TEXT PRIMARY KEY,
	"name"	TEXT,
	"sector"	TEXT,
	"PE"	REAL,
	"EPS"	REAL,
	"Price/book"	REAL,
	"regularMarketPrice"	REAL,
	"forwardPE"	REAL,
	"totalDebt"	REAL,
	"growthrate"	REAL,
	"priceEstimate"	REAL,
	"color"	TEXT,
	"extrainfo"	TEXT
);
COMMIT;
