# getting US stock exchange insider data

Insiders have to report their transactions using a Form4 

This is meant as an aid to the "Guru" investors actions.

If more than 1 Guru buys a share of a company, with the form4 data you can check if any company-insider did something similar (which would be a big plus)

Mind you, the form4 data contains benefit programs as well, managers receive shares as part of their wage. I consider these as non-informed buys.

It gets very interesting if a huge amount gets invested, preferbly by somebody high in rank.

# What is this about?

Retrieve4.py (contains the methods to retrieve, parse and store form4 data)
parse-form4.py (is a testprogram for 1 company)


# how does it work ?

the insider data gets stored in an sqlite table (form4):
 "form4" (
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

# analyzing

These are selects on the sqlitedatabase (table form4)

Distilling something useful is not an easy task!
Certainly not with the example (= Apple computer) I used.



- you get only price per share when they sell!


select avg(transactionPricePerShare) from form4 where transactionAcquiredDisposedCode = "D" and transactionPricePerShare > 0;


- this is a select of who buys more than 4 times the average of shares

select officerTitle,transactionShares,transactionDate from form4 where transactionShares > (select 4*avg(transactionShares) from form4 where transactionAcquiredDisposedCode = "A" and transactionPricePerShare is not null);

- sell more that 4 times average
select officerTitle,transactionShares,transactionDate from form4 where transactionShares > (select 4*avg(transactionShares) from form4 where transactionAcquiredDisposedCode = "D" and transactionPricePerShare is not null);

- what does someone do who owns more than twice the average
select securityTitle,officerTitle,transactionShares,transactionDate, transactionAcquiredDisposedCode from form4 where transactionShares > (select 2*avg(transactionShares) from form4 where sharesOwnedFollowingTransaction > 0);









