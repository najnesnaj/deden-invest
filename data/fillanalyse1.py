import sqlite3


#insert records into database 

def readdb():
    sqliteConnection = sqlite3.connect('sample2.sqlite')
    conn = sqlite3.connect('sample2.sqlite')
    cursor = sqliteConnection.cursor()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * from newfsma;''')
        rows = cursor.fetchall()
        #the weighted parameter is about the purity of the transaction (wagepackage gets low score) - the smaller the number the more pure
        for row in rows:
            switcher = {
                    "Lid van een bestuurs- of toezichthoudend orgaan" : 10,
                    "Persoon verbonden met een lid van een bestuurs- of toezichthoudend orgaan" : 20,
                    "Kaderlid met leidinggevende functie" : 30,
                    "Persoon die nauw verbonden is met een kaderlid met leidinggevende functie" : 40
                    }
            typtrans = {
                    "transactie in het kader van verloningsbeleid: aanvaarding en uitoefening van opties/warranten, alsook de verkoop van de eruit voortvloeiende aandelen": 9,
                    "VOID": 0,
                    "gift, ontvangen schenking of nalatenschap": 8,
                    "Andere": 6,
                    "primaire markt: intekening op een kapitaalverhoging of een uitgifte van schuldinstrumenten" : 5,
                    "transacties in aandelen of deelbewijzen van (alternatieve) beleggingsfondsen" : 3,
                    "lenen of uitlenen van financiële instrumenten" : 2 
                    }
            #print (row[0],row[3],row[7])
            classif =  (switcher.get(row[3].strip(),0))
            typtr =  (typtrans.get(row[9].strip(),0))
            weighted = classif + typtr
            cursor.execute('''INSERT INTO analyse1 (
                    "URL",
                    "classificatie", 
                    "ISIN-code financieel instrument", 
                    "Soort transactie", 
                    "Totaal bedrag", 
                    "Prijs" ) VALUES(?,?,?,?,?,?)''' , (row[0],weighted,row[7],row[8],row[15],row[14]))
            conn.commit()

    except sqlite3.Error as error:
        print("Error  sqlite", error)

    finally:
        if conn:
            conn.close()

readdb()
