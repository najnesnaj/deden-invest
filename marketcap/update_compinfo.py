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
#	"color"	TEXT,
#	"extrainfo"	TEXT
#);
#



def update_compinfo_color():
    #sqliteConnection = sqlite3.connect('edgardb/edgar.db')
    conn = sqlite3.connect('edgardb/edgar.db')
   # cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from compinfo;''')
        
        rows = cursor.fetchall()
        for row in rows:
            #clear field first
            cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("", row[0])) 
            #not too big not too small
            if (type(row[2]) == type(None)):
                cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("NO DIVIDENT DATA", row[0])) 
            if (type(row[1]) == type(None) or type(row[3]) == type(None)or type(row[4]) == type(None)or type(row[5]) == type(None)):
                cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("INCOMPLETE", row[0])) 
            if (row[1] == 'Financial Services'):
                print ("finance found")
                        #symbol = (rij['Symbol'] + '.BR')
                cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("FINANCIALS", row[0])) 
            #not too big not too small
            if (type(row[5]) != type(None) and type(row[6]) != type(None)):
                print (row[5], row[6])
                marketcap = float(row[5]) * float(row[6])
                if (type(row[8]) != type(None) and marketcap > 0 ):
                    if ((row[8] / marketcap) > 0.5):
                        cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("DEBT!", row[0])) 
                if (marketcap > 100000000000 ):
                    cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("BIG MARKETCAP", row[0])) 
                if (marketcap < 250000000):
                    cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("SMALL MARKETCAP", row[0])) 
                #print (type(row[4]))
                #negative EBITDA
            if (type(row[4]) != type(None)):
                if (row[4] < 0):
                    cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("BAD EBIDTA", row[0])) 
                #no divident
            if (type(row[2]) != type(None)):
                if (row[2] < 0.0000001):
                    cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("NO DIVIDENT", row[0])) 

        conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()


#in the sec edgar there is a difference between CIK an CUSIP numbers
#here we update the database with CIK numbers

def updatedb_cik():
    conn = sqlite3.connect('edgardb/edgar.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from whodoneit;''')
        rows = cursor.fetchall()
        for row in rows:
            with open('cik.csv', 'r') as fin:
                dr = csv.DictReader(fin,delimiter=',')
                for rij in dr:
                    if (rij['symbol'] == row[8]):
                        print (rij['symbol'])
                        #symbol = (rij['Symbol'] + '.BR')
                        cursor.execute('''update whodoneit set 'CIK' = (?) where transactionID = (?)''', (rij['cik'], row[0])) 
                        conn.commit()


    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()

#updatedb_symbol()
update_compinfo_color()

