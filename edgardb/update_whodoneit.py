import sqlite3
from datetime import datetime
import csv


#    for row in dr:
#        print (row['ISIN'],row['Symbol'])
    #    student_info = [(i['Datum'], i['Naam']) for i in dr]
    #    print(student_info)


#insert records into database 
# "whodoneit" (
#        "transactionID" TEXT PRIMARY KEY,
#        "Name"  TEXT,
#        "totalamount"   REAL,
#        "sellorbuy"     TEXT,
#        "datepurchase"  TEXT,
#        "datereporting" TEXT,
#        "importance"    TEXT,
#        "where" TEXT,
#        "ticker"      TEXT,
#        "howmany"       REAL,
#        "shareprice"    REAL,
#        "extrainfo"     TEXT
#




def updatedb():
    #sqliteConnection = sqlite3.connect('edgardb/edgar.db')
    conn = sqlite3.connect('edgardb/edgar.db')
   # cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from whodoneit;''')
        rows = cursor.fetchall()
        for row in rows:
            with open('Stock_Symbol_CUSIP.csv', 'r') as fin:
                dr = csv.DictReader(fin,delimiter=',')
                for rij in dr:
                 #print (row['ISIN'],row['Symbol'])
                    if (rij['CUSIP'] == row[1].lstrip("0")):
                        print (rij['Symbol'])
                        #symbol = (rij['Symbol'] + '.BR')
                        cursor.execute('''update whodoneit set ticker = (?) where transactionID = (?)''', (rij['Symbol'], row[0])) 
#                    "URL",
#                    "classificatie", 
#                    "ISIN-code financieel instrument", 
#                    "Soort transactie", 
#                    "Totaal bedrag", 
#                    "Prijs",
#                    "Datum") VALUES(?,?,?,?,?,?,?)''' , (row[0],weighted,symbol,row[8],row[15],row[14],datum))
                        conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()

updatedb()
