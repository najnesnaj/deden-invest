# How would an investor like Anthony Deden select companies ?

- he looks at their financial data
- they shouldn't be too small nor too big
- they have to generate a positive return
- preferbly pay out a divident, however small
- no financial services like banks and insurances (since hard to get an idea about risk)


# How to get data? 


https://companiesmarketcap.com/?download=csv

this gives a list of 5000+ companies. (file companies.cvs-orig)

For each company I lookup EBIDTA, divident and forwardPE and store this in an sqlite database.
(I get the data from finance.yahoo)

The companydata is stored in compinfo.
(file : selectc.py)

# analyzing?

all the company data is stored in the database

for each company there is a field color.

We update this field with : 
 
(file : update_compinfo.py)

This procedure inserts a comment like "TOO BIG" or "NEGATIVE EBIDTA" or "NO DIVIDENT" ....

The ones were interested in do not have a comment.

(by selecting color="" you get the few companies we're interested in)

# extended analyzing


You might want to know a little bit more about a company.

You can get the Form4 for a particular company at the SEC.

Mind you, you only have a ticker symbol. (the SEC can only handle CIK number)

- First look up the corresponding cik number of the ticker you're interested in
(file cik.csv)

- Fill in the CIK number
(file parse-form4.py)
- This script will get you 40 forms of type4 insider transaction and store this in the database table : form4

# analyzing form4 

- fill in the ticker you want analysed
analyze_form4.py
- this script adds up all the sell and all the buy transactions, and calculates the ratio 



