import yfinance as yf
import sqlite3
import pandas as pd
from datetime import datetime,timedelta


conn = sqlite3.connect('sample2.sqlite')
cursor = conn.cursor()

cursor.execute('''SELECT * from analyse1;''')
rows = cursor.fetchall()
today = datetime.now().strftime('%Y-%m-%d')
deltadate = datetime.now() - timedelta(days=4)
yesterday = deltadate.strftime('%Y-%m-%d')

def checkvalue():
    try:
        for row in rows:
    #   for some reason I've to convert the REAL datatype of sqlite to string and to float 
            vorm=row[4].replace(".","")
            getal=vorm.replace(",",".")
            flget = float(getal)        
	    #select a minimum amount of money invested
            if (flget>4000):
                if ((row[2] != "AKA.BR") & (row[2] != "EMPTY") & (row[2] != "ALAVY.BR") & (row[2] != "MLTV.BR") & (row[2] != "ALVET.BR")):
                    cleandate =  (row[6].replace('00:00:00','').strip())
                    dftoday = yf.download(row[2].strip(),start=cleandate,end=today)
                    lengtedf = len(dftoday) - 1
                    startprice =  (dftoday['High'].iloc[0])
                    endprice =  (dftoday['High'].iloc[lengtedf])
                    percentage = int((endprice-startprice)/startprice*100)
                    print (row[0], percentage)
                    cursor.execute('''UPDATE analyse1 SET percentage=? where URL=?;''', (percentage, row[0].strip()))
                    conn.commit()
    except:
        print("no data")

    finally:
        print("the End")
        if conn:
            conn.close()
                   
checkvalue()
