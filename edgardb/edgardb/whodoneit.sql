BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "whodoneit" (
	"transactionID"	TEXT PRIMARY KEY,
	"Name"	TEXT,
	"totalamount"	REAL,
	"sellorbuy"	TEXT,
	"datepurchase"	TEXT,
	"datereporting"	TEXT,
	"importance"	TEXT,
	"where"	TEXT,
	"ticker"	TEXT,
	"howmany"	REAL,
	"shareprice"	REAL,
	"extrainfo"	TEXT
);
COMMIT;
