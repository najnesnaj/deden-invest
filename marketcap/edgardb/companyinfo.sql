BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "compinfo" (
	"symbol" TEXT PRIMARY KEY,
	"sector"	TEXT,
	"lastDividendValue"	REAL,
	"grossProfits"	REAL,
	"ebitda"	REAL,
	"sharesOutstanding"	REAL,
	"regularMarketPrice"	REAL,
	"forwardPE"	REAL,
	"totalDebt"	REAL,
	"heldPercentInsiders"	REAL,
	"priceEstimate"	REAL,
	"color"	TEXT,
	"extrainfo"	TEXT
);
COMMIT;
