"""
Author: naj 
Date: 2022-01-29
MIT License
"""

from Portfolio13FHR import Portfolio

'''
#%%
CIK_2 = '0001067983'
Name_2 = 'buffett'

portfolio_2 = Portfolio(CIK_2,Name_2)

#%%
portfolio_2.compare_recent_changes()

portfolio_2.data_recent.head()

portfolio_2.plot_recent_shares_change(portfolio_2.data_recent)
portfolio_2.plot_recent_value_change(portfolio_2.data_recent)

'''

# list of gurus I want to track and their cik
#cik={'Buffett': '0001067983', 'Mohnish': '0001549575', 'Seth': '0001061768', 'Carl': '0000921669',
#     'TCI_Chris': '0001647251', 'Pershing_Ackman': '0001336528', 'Greenlight_Einhorn': '0001079114',
cik={'Buffett': '0001067983',  'Seth': '0001061768', 'Carl': '0000921669',
     'TCI_Chris': '0001647251', 'Pershing_Ackman': '0001336528', 'Greenlight_Einhorn': '0001079114',
     'Himalaya_Li_Lu': '0001709323', 'David_Tepper': '0001656456', 'Dalio':'0001350694',
     'Guy': '0001404599'}
#cik={'Dalio':'0001350694',
#cik={ 'Guy': '0001404599'}

for i in cik:
    print (i,cik[i])

    Name_2 = i 
    CIK_1 = cik[i] 
    portfolio_1 = Portfolio(CIK_1,Name_2)
    if portfolio_1.compare_recent_changes():
        portfolio_1.data_recent.head()
#    print(portfolio_1.data_recent)
        portfolio_1.insertdb(portfolio_1.data_recent)
    #print(portfolio_1.data_recent.info())
    portfolio_1.plot_recent_shares_change(portfolio_1.data_recent)
    portfolio_1.plot_recent_value_change(portfolio_1.data_recent)


