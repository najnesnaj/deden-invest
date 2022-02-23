import sqlite3
from datetime import datetime
import csv



def analyze_form4(ticker=''):
    conn = sqlite3.connect('edgardb/edgar.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT sum(transactionShares) from form4 where issuerTradingSymbol=(?) and transactionacquireddisposedcode=(?) ''', (ticker,"A"));

#SELECT sum(transactionShares) from form4 where issuerTradingSymbol='ADSK' and transactionacquireddisposedcode='D';
#''')
        buys = cursor.fetchall()
        for gekocht in buys:
            print (gekocht)
        cursor.execute('''SELECT sum(transactionShares) from form4 where issuerTradingSymbol=(?) and transactionacquireddisposedcode=(?) ''', (ticker,"D"));
        sells = cursor.fetchall()
        for verkocht in sells:
            print (verkocht)
        #if (sells > 0):
        #print (type(gekocht)) 
        ratio = (gekocht[0]/verkocht[0]) 
        print ("buy", gekocht[0], "sell", verkocht[0], "ratio", ratio)
        print ("no info on buy prices")
     #   cursor.execute('''SELECT avg(transactionPricePerShare ) from form4 where issuerTradingSymbol=(?) and transactionacquireddisposedcode=(?) ''', (ticker,"A"));
     #   gemiddeldeaankoop=cursor.fetchall()
     #   for aankoop in gemiddeldeaankoop:
     #       print ("average share price buy", aankoop)
        cursor.execute('''SELECT avg(transactionPricePerShare ) from form4 where issuerTradingSymbol=(?) and transactionacquireddisposedcode=(?) and transactionPricePerShare > 0''', (ticker,"D"));
        gemiddeldeverkoop=cursor.fetchall()
        for verkoop in gemiddeldeverkoop:
            print ("average share price sell", verkoop)

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()

analyze_form4(ticker='GILD')
