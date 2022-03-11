"""
Author: naj 
Date: 2022-02-18
MIT License
"""


import sqlite3
from datetime import datetime
import yfinance as yahooFinance


#update the table with companydata
#according to Anthony Deden's insight
#no finance assurance
#not too big, not too small
#pay divident 
#not too much debt

def updatedb(transrecord):
    sqliteConnection = sqlite3.connect('stock/ticker.db')
    conn = sqlite3.connect('stock/ticker.db')
    cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    print ("update record")

#        for i in enumerate(transrecord):
    try:
        symbool = transrecord[0]
        print (symbool)
        cursor.execute('''update compinfo set 
        "sector" = ?   ,
        "lastDividendValue" = ?    ,
        "grossProfits" = ? ,
        "ebitda" = ?       ,
        "sharesOutstanding"  = ?  ,
        "regularMarketPrice" = ?  ,
        "forwardPE" = ?  ,
        "totalDebt"  = ? ,
        "heldPercentInsiders" = ? 
          where symbol=?''' , (transrecord[1], transrecord[2], transrecord[3], transrecord[4], transrecord[5], transrecord[6], transrecord[7], transrecord[8], transrecord[9], symbool))

        conn.commit()
    except sqlite3.Error as error:
        print("Error  sqlite", error)
#        
#        
    if conn:
        conn.close()




#todo remove rowid condition
def update_compinfo_yahoo():
    conn = sqlite3.connect('stock/ticker.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from compinfo where rowid > 53223''')
        rows = cursor.fetchall()
        for row in rows:
            #cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("", row[0])) 
            print (row[0])
            GetCompanyInformation = yahooFinance.Ticker(row[0])
            infothere = len(GetCompanyInformation.info)
            print ("lengte", infothere)
            if (infothere > 115):
                transrecord=[]
                transrecord.append(row[0])
                transrecord.append(GetCompanyInformation.info['sector'])
                transrecord.append(GetCompanyInformation.info['lastDividendValue'])
                transrecord.append(GetCompanyInformation.info['grossProfits'])
                transrecord.append(GetCompanyInformation.info['ebitda'])
                transrecord.append(GetCompanyInformation.info['sharesOutstanding'])
                transrecord.append(GetCompanyInformation.info['regularMarketPrice'])
                transrecord.append(GetCompanyInformation.info['forwardPE'])
                transrecord.append(GetCompanyInformation.info['totalDebt'])
                transrecord.append(GetCompanyInformation.info['heldPercentInsiders'])
                print (transrecord)
                updatedb (transrecord)
           
    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()



#get latest financial data from yahoo
update_compinfo_yahoo()

