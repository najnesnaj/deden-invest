# getting US stock exchange data, transactions by funds

I would like to thank zpetan, which scripts where used as a starting point : 
https://github.com/zpetan/sec-13f-portfolio-python

- Filing13FHR.py
- Portfolio13FHR.py

were slightly modified

Getting financial data for free is not an easy task. (thanks Yahoo and thank you SEC)


# What is this about?
on the https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent website, you can read the forms. 
Fund managers have to file their position, using the "13F" form.

important dates : 

- 13F is filed after the reported quarter 
- the transactiondate is an estimate eg. half the quarter = 45 days
- filing date
- publishing date 

**the data could be more than 4 months old**

# list of gurus I want to track and their cik
cik={'Buffett': '0001067983', 'Mohnish': '0001549575', 'Seth': '0001061768', 'Carl': '0000921669',
     'TCI_Chris': '0001647251', 'Pershing_Ackman': '0001336528', 'Greenlight_Einhorn': '0001079114',
     'Himalaya_Li_Lu': '0001709323', 'David_Tepper': '0001656456', 'Dalio':'0001350694',
     'Guy': '0001404599'}


# how does it work ?

for each of these "investment Guru's" I get their last 4, 13F filings.
Actually you only need 2 (current and previous)

Remember : they only publish their holdings.
By comparing current and previous holding, you know what they bought/sold.

this data is stored in an sqlite3 database : edgardb/edgar.db

-> fill_edgardb.py


# plotting 

plotting beautifull graphical representations of the "Guru" portfolio?

uncomment #plot... in fill_edgardb.py

see also : samples directory


# analyzing


OK the data is now contained in our edgardb database, and now what?

first of all, we need to convert the cusip number of the stocks to a usable stockquote. 

-> update_whodoneit.py
-> Stock_Symbol_CUSIP.csv (found it on github)


# plotting revisited

OK, now we can plot candlestick graphics for each quote.
On this 'html' form, the transactions are marked with the biggest vertical bar (red sell, green buy)

-> analyse_stock.py

this scripts generates html pages for each "quote" that was subject to the "Guru" attention
Each transaction is marked on the candlestick diagram with a big bar (red is sell, green is buy)
Hover over this bar and you can see the estimated price


see : samples directory 

# My 3 cents ....

OK, now you can stare at graphs, so what?

You know the price at which a share got sold or bought by a "Guru", with an important delay.
- suppose you only get "buyers" for a share 
- the average shareprice resembles the current price
- or is cheaper
=> buy, buy, buy !!!!

- suppose you only get "sellers" for a share 
- the average shareprice resembles the current price
- or is higher
=> sell, sell, sell !!!

**what is a company worth? well an average buying price might get you an idea, the Gurus are investors and not speculators ...**


# your own portfolio

two scenario's
- building a portfolio : get noticed for opportunities
- maintain a portfolio : check the status of your shares (are there a lot of sellers?)





