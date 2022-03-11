# 100000 companies 
------------------

Here I took a 2017 list with over 100000 companies worldwide.

OK this not up to date, but in the philosophy of Anthony Deden, a company has to be around for some time (it is likely it will be in the future ...)

## update data
--------------

For each company, I did a look-up in yahoo finance. 
This is a slow process... (so I settled for 40000 companies)
Some financial data is inserted.

For more than half(!) of the companies I did not find quality data.
They were excluded.

## Anthony Deden Philosophy
---------------------------

- Anthony does not invest in banks nor insurance companies.
- A company has to pay a divident (however small)
- A company cannot be too big (not manageble)
- A company should not be too small
- A company should not have too much debt
- A company should make a profit

## Applying philosophy
----------------------

-the python script:  analytics.py was applied
-it fills the field extrainfo with the above criteria
-As it happens : the ones we're after should have a blank "extrainfo" field


## Findings ?
-------------

only 88	are left blank... (and meet Anthony's criteria)


4029	BAD EBIDTA
1368	BIG MARKETCAP
4031	DEBT!
939	FINANCIALS
541	INCOMPLETE
4250	NO DIVIDENT DATA
3403	SMALL MARKETCAP

## And now what?
----------------

The preliminary list is worldwide, so probably not possible to buy/or sell.
eg. How do I buy Turkish shares?

-- I will have to look up the company structure (family business?)
-- I will have to look at insider (type form4) transactions

















