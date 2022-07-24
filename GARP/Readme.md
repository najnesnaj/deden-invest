## README ##

############################################################################
GARP: Growth at a Reasonable Price
############################################################################

#this is an American EFT which tracks small cap value internationally: 
#https://us.dimensional.com/funds/international-small-cap-value

## Filtering ##

- as a proof of concept I've used Belgium based companies

## scripts ##

- tickers in the files tickers.csv are used

- a database is filled from tickers in tickers.csv with insert_ticker.py  
- next, relevant data is updated with update_ticker.py

- finally analytics.py checks criterea and gives a score (the higher the better)

## Criteria ##



- P/E ratios lower than 10 

- the price-to-book value (P/B) ratio 
(P/B ratios under 1 are typically considered solid investments)

- EPS (earnings per share) positive

- beta smaller than 1 considered a plus (low volatility) 

- current ratio bigger than 1 : assets are bigger than liabilities

- sales per shares smaller than 1 considered a plus

- free cash per share is indicator for solvency

- I do not like too much debt ...

###files####

https://us.dimensional.com/dfsmedia/f27f1cc5b9674653938eb84ff8006d8c/61627-source/options/download/idg-book-full-soi-04-30-2022.pdf


-----------------------------------------------------








### note ###

  
Suppose there would be a 100 dollarbill on the pavement.
Would you pick it up?

According to efficientmarkettheory it would not be lying there.

Maybe small value stock markets ain't that efficient ...





