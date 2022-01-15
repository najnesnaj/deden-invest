BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "newfsma" (
	"URL"	TEXT PRIMARY KEY,
	"Datum openbaarmaking"	TEXT,
	"Naam meldplichtige"	TEXT,
	"Hoedanigheid meldplichtige"	TEXT,
	"Leidinggevende(n) waarmee de meldplichtige nauw verbonden is"	TEXT,
	"Emittent"	TEXT,
	"Soort financieel instrument"	TEXT,
	"ISIN-code financieel instrument"	TEXT,
	"Soort transactie"	TEXT,
	"Specificatie van het soort transactie"	TEXT,
	"Plaats van uitvoering transactie"	TEXT,
	"Date"	TEXT,
	"Munt"	TEXT,
	"Aantal financiële instrumenten"	REAL,
	"Prijs"	REAL,
	"Totaal bedrag"	REAL,
	"Toelichting van de meldplichtige"	TEXT
);
COMMIT;
