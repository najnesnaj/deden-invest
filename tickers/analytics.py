"""
Author: naj 
Date: 2022-02-18
MIT License
"""


import sqlite3
from datetime import datetime


#update the table with companydata
#according to Anthony Deden's insight
#no finance assurance
#not too big, not too small
#pay divident 
#not too much debt


#CREATE TABLE IF NOT EXISTS "compinfo" (
#	"symbol" TEXT PRIMARY KEY,
#	"sector"	TEXT,
#	"lastDividendValue"	REAL,
#	"grossProfits"	REAL,
#	"ebitda"	REAL,
#	"sharesOutstanding"	REAL,
#	"regularMarketPrice"	REAL,
#	"forwardPE"	REAL,
#	"totalDebt"	REAL,
#	"heldPercentInsiders"	REAL,
#	"priceEstimate"	REAL,
#	"extrainfo"	TEXT,
#	"extrainfo"	TEXT
#);
#



def update_compinfo_extrainfo():
    #sqliteConnection = sqlite3.connect('edgardb/edgar.db')
    conn = sqlite3.connect('stock/ticker.db')
   # cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from compinfo;''')
        
        rows = cursor.fetchall()
        for row in rows:
            #clear field first
            cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("", row[0])) 
            #not too big not too small
            if (type(row[2]) == type(None)):
                cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("NO DIVIDENT DATA", row[0])) 
            if (type(row[1]) == type(None) or type(row[3]) == type(None)or type(row[4]) == type(None)or type(row[5]) == type(None)):
                cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("INCOMPLETE", row[0])) 
            if (row[1] == 'Financial Services'):
                print ("finance found")
                        #symbol = (rij['Symbol'] + '.BR')
                cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("FINANCIALS", row[0])) 
            #not too big not too small
            if (type(row[5]) != type(None) and type(row[6]) != type(None)):
                print (row[5], row[6])
                marketcap = float(row[5]) * float(row[6])
                if (type(row[8]) != type(None) and marketcap > 0 ):
                    if ((row[8] / marketcap) > 0.5):
                        cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("DEBT!", row[0])) 
                if (marketcap > 100000000000 ):
                    cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("BIG MARKETCAP", row[0])) 
                if (marketcap < 250000000):
                    cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("SMALL MARKETCAP", row[0])) 
                #print (type(row[4]))
                #negative EBITDA
            if (type(row[4]) != type(None)):
                if (row[4] < 0):
                    cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("BAD EBIDTA", row[0])) 
                #no divident
            if (type(row[2]) != type(None)):
                if (row[2] < 0.0000001):
                    cursor.execute('''update compinfo set extrainfo = (?) where symbol = (?)''', ("NO DIVIDENT", row[0])) 

        conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()


update_compinfo_extrainfo()

