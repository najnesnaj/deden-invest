BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "form4" (
"transactionCode"  TEXT, 
"securityTitle"  TEXT, 
"transactionDate"  TEXT, 
"transactionShares"  INTEGER, 
"transactionPricePerShare"  INTEGER, 
"transactionAcquiredDisposedCode"  TEXT, 
"sharesOwnedFollowingTransaction"  REAL, 
"directOrIndirectOwnership"  TEXT, 
"documentType"  INTEGER, 
"periodOfReport"  TEXT, 
"issuerName"  TEXT, 
"issuerTradingSymbol"  TEXT, 
"rptOwnerCik"  TEXT, 
"officerTitle"  TEXT, 
"issuerCik"  TEXT, 
"rptOwnerName"  TEXT 
);



COMMIT;
