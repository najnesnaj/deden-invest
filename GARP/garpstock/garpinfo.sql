BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "garpinfo" (
	"symbol" TEXT PRIMARY KEY,
	"name"	TEXT,
	"sector"	TEXT,
	"trailingPE"	REAL,
	"EPS"	REAL,
	"Price/book"	REAL,
	"TangibleValuePerShare"	REAL,
	"forwardPE"	REAL,
	"totalDebt"	REAL,
	"currentRatio"	REAL,
	"growthrate"	REAL,
	"beta"	REAL,
	"priceToSalesTrailing12Months"	REAL,
	"color"	TEXT,
	"extrainfo"	TEXT
);
COMMIT;
