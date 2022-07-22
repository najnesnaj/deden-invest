"""
Author: naj 
Date: 2022-07-22
MIT License
"""


import sqlite3
from datetime import datetime



def update_compinfo_extrainfo():
    #sqliteConnection = sqlite3.connect('edgardb/edgar.db')
    conn = sqlite3.connect('garpstock/garp.db')
   # cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from garpinfo;''')
        
        rows = cursor.fetchall()
        for row in rows:
            #clear field first
            cursor.execute('''update garpinfo set extrainfo = (?) where symbol = (?)''', ("", row[0])) 
            score = 0
            #not too big not too small
            if (row[2] == 'Financial Services'):
                print ("finance found")
                #cursor.execute('''update garpinfo set extrainfo = (?) where symbol = (?)''', ("FINANCIALS", row[0])) 
            if (type(row[3]) != type(None) and type(row[7]) != type(None)):
                if (float(row[3]) > float(row[7])):
                #forward PE smaller than current PE = improvement
                    score = score + 1
            #if (row[4] > 0):
                #earnings per share positive
           #     score = score + 1
            if (row[5] < 1):
                #price smaller than book
                score = score + 1
            if (type(row[9]) != type(None) ):
                if (float(row[9]) > 1.3):
                    #currentRatio assets bigger than liabilities
                    score = score + 1
            if (row[11] < 1):
                #beta is smaller than 1
                score = score + 1
            if (row[12] < 1):
                #price to sales : smaller is better
                score = score + 1
            if (score > 3):
                cursor.execute('''update garpinfo set extrainfo = (?) where symbol = (?)''', ("TOP", row[0])) 
            elif (score == 3):
                cursor.execute('''update garpinfo set extrainfo = (?) where symbol = (?)''', ("ALMOST TOP", row[0])) 
            else:
                cursor.execute('''update garpinfo set extrainfo = (?) where symbol = (?)''', ("FLOP", row[0])) 

#            if (row[3] > row[7]):

        conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()


update_compinfo_extrainfo()

