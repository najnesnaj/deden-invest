## README ##

#############################################################################

This is a set of python tools to extract insider trading data from the Brussels stock exchange.

The data is stored into an sqlite database and gets processed.

The data was found on a public website (www.fsma.be). 

WARNING : although the data can be found on a public website, I've been careful and removed all personal data from the sample database. (Pls respect the privicy and legislation like GDPR)

############################################################################




###files####
sqlite database  = sample2.sqlite
table analyse1 = analyse1.sql
table newfsma = newfsma.sql
csv ISIN yahoo quotes = Euronext_Equities_2022-01-19.csv
scraping fsma site = scrapauto.py
fill up analyse1 = fillanalyse1.py
calculate delta percentage  = pandalyse.py



-----------------------------------------------------




https://live.euronext.com/nl/markets/brussels/equities/list
ISIN codes are not easily linked to bloomberg stock quote symbols




### Principle scrapauto.py ###

here you define period for which the website https://www.fsma.be/nl/transaction-search gets spidered

datumvan='2020-06-01'
datumtot='2020-12-30'

it collects all the data and stores it into a sqlite table "newfsma"


### fillanalyse1.py ###

to analyse the data you only need a subset, and the ISIN code has to be converted to something yahoo finance understands

Here we make a distinction on who performed the transaction and bundle this in field "Classificatie" :

=====member of board gets a 10 ============================
                    "Lid van een bestuurs- of toezichthoudend orgaan" : 10,
                    "Persoon verbonden met een lid van een bestuurs- of toezichthoudend orgaan" : 20,
                    "Kaderlid met leidinggevende functie" : 30,
                    "Persoon die nauw verbonden is met een kaderlid met leidinggevende functie" : 40
=====why the transaction happened is added, eg 9 is compensation ======================
=====so a CFO who gets a reward gets number 30 + 9 =========================================
=====a transaction with classification 39, is less valuable than boardmember (=10)====



                    "transactie in het kader van verloningsbeleid: aanvaarding en uitoefening van opties/warranten, alsook de verkoop van de eruit voortvloeiende aandelen": 9,
                    "VOID": 0,
                    "gift, ontvangen schenking of nalatenschap": 8,
                    "Andere": 6,
                    "primaire markt: intekening op een kapitaalverhoging of een uitgifte van schuldinstrumenten" : 5,
                    "transacties in aandelen of deelbewijzen van (alternatieve) beleggingsfondsen" : 3,
                    "lenen of uitlenen van financiële instrumenten" : 2
                    }
       
===================================



### pandalyse.py ###

for transactions greater than 4000 euro, we get stockquotes from yahoo.
we calculate the percentage of growth (or decay) and store this in analyse1


===================================


to analyse the data in analyse1, I used sqlitebrowser
I erased table newfsma to be compliant with GDPR (github is public)




