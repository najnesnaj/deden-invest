#from datetime import datetime
import csv
import yfinance as yahooFinance
import sqlite3


def insertdb(transrecord):
    sqliteConnection = sqlite3.connect('edgardb/edgar.db')
    conn = sqlite3.connect('edgardb/edgar.db')
    cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    print ("insert record")

#        for i in enumerate(transrecord):
    try: 
        cursor.execute('''INSERT INTO compinfo( 
        "symbol" ,
        "sector"    ,
        "lastDividendValue"     ,
        "grossProfits"  ,
        "ebitda"        ,
        "sharesOutstanding"    ,
        "regularMarketPrice"   ,
        "forwardPE"   ,
        "totalDebt"   ,
        "heldPercentInsiders"  ,
        "priceEstimate" ,
        "color" ,
        "extrainfo"     
        ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''' , (transrecord[0:13]))

        conn.commit()
    except sqlite3.Error as error:
        print("Error  sqlite", error)
#        
#        
    if conn:
        conn.close()







def filter():
#    try:
   # print ("test")
    with open('companies.csv', 'r') as fin:
        dr = csv.DictReader(fin,delimiter=',')
        for rij in dr:
            transrecord=[]
            #print (rij['Symbol'])
            transrecord.append(rij['Symbol'])
            GetCompanyInformation = yahooFinance.Ticker(rij['Symbol'])
            transrecord.append(GetCompanyInformation.info['sector'])
            transrecord.append(GetCompanyInformation.info['lastDividendValue'])
            transrecord.append(GetCompanyInformation.info['grossProfits'])
            transrecord.append(GetCompanyInformation.info['ebitda'])
            transrecord.append(GetCompanyInformation.info['sharesOutstanding'])
            transrecord.append(GetCompanyInformation.info['regularMarketPrice'])
            transrecord.append(GetCompanyInformation.info['forwardPE'])
            transrecord.append(GetCompanyInformation.info['totalDebt'])
            transrecord.append(GetCompanyInformation.info['heldPercentInsiders'])
            #dummy field for later use
            transrecord.append(0)
            transrecord.append("")
            transrecord.append("")
            insertdb(transrecord)




'''


"compinfo" (
        "symbol" TEXT PRIMARY KEY,
        "sector"        TEXT,
        "lastDividendValue"     REAL,
        "grossProfits"  REAL,
        "ebitda"        REAL,
        "sharesOutstanding"     REAL,
        "regularMarketPrice"    REAL,
        "forwardPE"     REAL,
        "totalDebt"     REAL,
        "heldPercentInsiders"   REAL,
        "priceEstimate" REAL,
        "color" TEXT,
        "extrainfo"     TEXT
);

'''

filter()
