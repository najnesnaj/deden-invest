"""
Author: naj 
Date: 2022-07-20
MIT License
"""


import sqlite3
from datetime import datetime
import yfinance as yahooFinance


#update the table with companydata
# no finance , assurance
#
# tickerdata are small value stock


def updatedb(transrecord):
    sqliteConnection = sqlite3.connect('garpstock/garp.db')
    conn = sqlite3.connect('garpstock/garp.db')
    cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    print ("update record")

#        for i in enumerate(transrecord):
    try:
        symbool = transrecord[0]
        print (symbool)
        cursor.execute('''update garpinfo set 
        "name" = ?    ,
        "sector" = ? ,
        "trailingPE" = ?       ,
        "EPS"  = ?  ,
        "price/book" = ?  ,
        "totalCashPerShare" = ?  ,
        "forwardPE"  = ? ,
        "totalDebt" = ?, 
        "currentRatio" = ?, 
        "growthRate" = ?, 
        "beta" = ? ,
        "priceToSalesTrailing12Months" = ?
          where symbol = ?''' , (transrecord[1], transrecord[2], transrecord[3], transrecord[4], transrecord[5], transrecord[6], transrecord[7], transrecord[8], transrecord[9], transrecord[10], transrecord[11],transrecord[12], symbool))

        conn.commit()
    except sqlite3.Error as error:
        print("Error  sqlite", error)
#        
#        
    if conn:
        conn.close()




def update_compinfo_yahoo():
    conn = sqlite3.connect('garpstock/garp.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from garpinfo ''')
        rows = cursor.fetchall()
        for row in rows:
            #cursor.execute('''update compinfo set color = (?) where symbol = (?)''', ("", row[0])) 
            print (row[0])
            GetCompanyInformation = yahooFinance.Ticker(row[0])
            #print (GetCompanyInformation.info)
            infothere = len(GetCompanyInformation.info)
            print ("lengte", infothere)
            if (infothere > 115):
                transrecord=[]
                transrecord.append(row[0])
                transrecord.append(GetCompanyInformation.info['longName'])
                transrecord.append(GetCompanyInformation.info['sector'])
                try:
                    trailingPE = GetCompanyInformation.info['trailingPE']
                    transrecord.append(trailingPE)     
                except KeyError:
                    transrecord.append(0)     

                #transrecord.append(GetCompanyInformation.info['trailingPE'])
                transrecord.append(GetCompanyInformation.info['forwardEps'])
                transrecord.append(GetCompanyInformation.info['priceToBook'])
                transrecord.append(GetCompanyInformation.info['totalCashPerShare'])
                transrecord.append(GetCompanyInformation.info['forwardPE'])
                transrecord.append(GetCompanyInformation.info['debtToEquity'])
                transrecord.append(GetCompanyInformation.info['currentRatio'])
                transrecord.append(GetCompanyInformation.info['earningsGrowth'])
                transrecord.append(GetCompanyInformation.info['beta'])
                transrecord.append(GetCompanyInformation.info['priceToSalesTrailing12Months'])
                print (transrecord)
                updatedb (transrecord)
           
    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()



#get latest financial data from yahoo
update_compinfo_yahoo()

