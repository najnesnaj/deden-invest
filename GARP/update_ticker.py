"""
Author: naj 
Date: 2022-07-20
MIT License
"""


import sqlite3
from datetime import datetime
import yfinance as yahooFinance
import pandas as pd

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
        "TangibleValuePerShare" = ?  ,
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
            infolen =  len(GetCompanyInformation.info)
            print ("lengte")
            print (infolen)
            if (infolen > 149):
            #print (GetCompanyInformation.balance_sheet['Net Tangible Assets'])
            #print (GetCompanyInformation.balance_sheet.keys())
                pnl = GetCompanyInformation.financials
                bs = GetCompanyInformation.balance_sheet
                cf = GetCompanyInformation.cashflow
#            fs = pd.concat([pnl, bs, cf])
            #transposedfs = fs.T
                transposedfs = bs.T
                financials = pnl.T
                cashflow = cf.T
                col_name = 'Net Tangible Assets'
            #col_name = 'Total Stockholder Equity'
            # OPGELET !!!! deze index verandert ieder jaar !!!!!!!!
             #   date = '2021-12-31' 
             # nu index 0 gebruikt is beter, maar de kolompositie is risico ....

            #print(financials.columns)
            #print(transposedfs.columns)
            #print(cashflow.columns)
                if (type(GetCompanyInformation.info['totalDebt']) != type(None) ):
                    totaleschuld = GetCompanyInformation.info['totalDebt']
                else:
                    totaleschuld = 9999999999999999
                try:
                    echtewaarde = (transposedfs.iloc[0,22])
                except IndexError:
                    echtewaarde = 0 
                #echtewaarde = (transposedfs.loc[date,col_name].iat[0])
                aantalaandelen = GetCompanyInformation.info['sharesOutstanding']
                prijs = GetCompanyInformation.info['currentPrice']
                if (type(aantalaandelen) != type(None)) : 
                    if (aantalaandelen > 0):
                        waardeperaandeel = (echtewaarde/aantalaandelen)
                        schuldperaandeel = (totaleschuld/aantalaandelen)
                    else:
                        waardeperaandeel = -99999999999 
                        schuldperaandeel = 99999999999
                else : 
                    aantalaandelen = 0
                    waardeperaandeel = 0
                if (prijs > 0):
                    realvalue = waardeperaandeel / prijs
                    realdebt = schuldperaandeel / prijs
                else: 
                     realvalue = 99999
                     realdebt = 99999
                print (realvalue)
                infothere = len(GetCompanyInformation.info)
                #print ("lengte", infothere)
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
                    transrecord.append(GetCompanyInformation.info['trailingEps'])
                    transrecord.append(GetCompanyInformation.info['priceToBook'])
                    #transrecord.append(GetCompanyInformation.info['totalCashPerShare'])
                    transrecord.append(realvalue)
                    transrecord.append(GetCompanyInformation.info['forwardPE'])
                    #transrecord.append(GetCompanyInformation.info['debtToEquity'])
                    transrecord.append(realdebt)
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

