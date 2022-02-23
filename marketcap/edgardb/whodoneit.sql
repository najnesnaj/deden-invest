BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "whodoneit" (
	"transactionID"	TEXT PRIMARY KEY,
	"CUSIP"	TEXT,
	"totalamount"	REAL,
	"sellorbuy"	TEXT,
	"datepurchase"	TEXT,
	"datereporting"	TEXT,
	"importance"	TEXT,
	"CIK"	TEXT,
	"ticker"	TEXT,
	"howmany"	REAL,
	"shareprice"	REAL,
	"extrainfo"	TEXT
);
COMMIT;
