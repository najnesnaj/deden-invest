# this python script gets info about insider stock purchases on Bel stock exchange
#
# parameters : date from / date to
# range cannot exceed a week (page limit)
#
# a transaction search (in dutch, since content is not english even with english language option....)
#
# a list of transaction is given
# for each of these transactions a page is called, the same page is included in each record for further reference
#

import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd


#insert records into database 

def insertdb(fsmarecord):
    sqliteConnection = sqlite3.connect('sample2.sqlite')
    conn = sqlite3.connect('sample2.sqlite')
    cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO newfsma( "URL"   ,
        "Datum openbaarmaking"  ,
        "Naam meldplichtige"    ,
        "Hoedanigheid meldplichtige"    ,
        "Leidinggevende(n) waarmee de meldplichtige nauw verbonden is"  ,
        "Emittent"      ,
        "Soort financieel instrument"   ,
        "ISIN-code financieel instrument",
        "Soort transactie",
        "Specificatie van het soort transactie",
        "Plaats van uitvoering transactie",
        "Date" ,
        "Munt" ,
        "Aantal financiële instrumenten",
        "Prijs" ,
        "Totaal bedrag" ,
        "Toelichting van de meldplichtige") VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' , (fsmarecord[0:17]))
        conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()




def recordclean(lijst, URLREC):
    fsmadata = []
    for datalijn in lijst:
        hulp = ''.join(datalijn)
        record = hulp.split(";")
        #record differ (number of fields) , fill this with VOID
    if (record[6] !="Leidinggevende(n) waarmee de meldplichtige nauw verbonden is"):
        record.insert(6, "VOID")
        record.insert(6, "VOID")
    if (record[16] !="Specificatie van het soort transactie"):
        record.insert(16, "VOID")
        record.insert(16, "VOID")
    teller=0
    # The URL of the record is used as a unique key in the database later on
    for element in record:
        if (teller == 0):
            #print (URL, ";", end="")
            fsmadata.append(URLREC)
        teller = teller + 1
        if (teller % 2) == 0:
            #print (element,";", end="")
            fsmadata.append(element)
#    print ("\n", end="")
    insertdb(fsmadata)
    fsmadata.clear()
	


def getselfromfsma(URL):
    #print (URL)
    r = requests.get(URL)
    #print(r.content)
    soup = BeautifulSoup(r.content, 'html5lib') 

    # If this line causes an error, run 'pip install html5lib' or install html5lib

    #print(soup.prettify())
    table = soup.find_all('td')
    return (table)


def getrecordsfsma(table):
    #process records and insert into database 
    for row in table:
        for links in (row.find_all("a")):
            URLREC = "https://www.fsma.be" + links.get("href")
            r = requests.get(URLREC)
            #print (URL)
            soup = BeautifulSoup(r.content, 'html5lib')
	    #this the html tag which defines the important database content
	    #
	    #this converts the tag article - content to text, which is all the relevant data in page
            hulp = (soup.article.text)
            #convert list to string / cleaning
            hulp = hulp.replace("\n",";") 
            hulp = hulp.replace(";;",";")
            hulp = hulp.replace(";      ;        ;    ","")
            hulp = hulp.replace("          ;  ;    ","")
            #convert string to list which contains lines that contain records
            lijst = hulp.split("\n")
            recordclean(lijst, URLREC)	


datumvan='2022-01-01'
datumtot='2022-05-01'

enddate = datumvan

while (enddate < datumtot):
    enddate = pd.to_datetime(datumvan) + pd.DateOffset(days=5)
    enddate = (enddate.strftime('%Y-%m-%d'))
    #print (datumvan, " ", enddate)
    URL = "https://www.fsma.be/nl/transaction-search?issuer=&date%5Bmin%5D=" + datumvan + "&date%5Bmax%5D=" + enddate 
    #print (URL)
    tabel = getselfromfsma(URL)
    getrecordsfsma(tabel)
    #print (tabel)
    datumvan = enddate

#URL = "https://www.fsma.be/nl/transaction-search?issuer=&date%5Bmin%5D=" + datumvan + "&date%5Bmax%5D=" + datumtot


