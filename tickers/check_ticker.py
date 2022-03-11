import csv
import yfinance as yahooFinance
import sqlite3



def insertdb(transrecord):
    sqliteConnection = sqlite3.connect('stock/ticker.db')
    conn = sqlite3.connect('stock/ticker.db')
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







            #GetCompanyInformation = yahooFinance.Ticker(rij['Symbol'])
            #transrecord.append(GetCompanyInformation.info['sector'])
            #transrecord.append(GetCompanyInformation.info['lastDividendValue'])
            #transrecord.append(GetCompanyInformation.info['grossProfits'])
            #transrecord.append(GetCompanyInformation.info['ebitda'])
            #transrecord.append(GetCompanyInformation.info['sharesOutstanding'])
            #transrecord.append(GetCompanyInformation.info['regularMarketPrice'])
            #transrecord.append(GetCompanyInformation.info['forwardPE'])
            #transrecord.append(GetCompanyInformation.info['totalDebt'])
            #transrecord.append(GetCompanyInformation.info['heldPercentInsiders'])


def check_ticker():
#    try:
    print ("test")
    with open('tickers.csv', 'r') as fin:
        dr = csv.DictReader(fin,delimiter=';')
        for rij in dr:
            transrecord=[]
            transrecord.append(rij['Ticker'])
            transrecord.append(rij['Category Name'])
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(0)
            transrecord.append(rij['Name'])
            transrecord.append(rij['Exchange'])
            transrecord.append(rij['Country'])
            insertdb(transrecord)



#filter()
check_ticker()






