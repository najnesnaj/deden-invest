import matplotlib
import PyQt5
import quandl
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

quandl.ApiConfig.api_key = 'gWs2gyG3aWPmQUZ4mfMY'
#data = quandl.get('NSE/OIL')
data = quandl.get('ECONOMIST/BIGMAC_IDN')
infla = quandl.get('ODA/IDN_PCPI')
print(data)
#import yfinance as yf

#df = yf.download("AMZN MSFT", start="2019-01-01", end="2020-01-01",group_by="ticker") 
#df = yf.download("MSFT", start="2019-01-01", end="2020-01-01",group_by="ticker") 
#df = yf.download("RYSAS.IS", start="2019-01-01", end="2021-11-17",group_by="ticker") 
#df = yf.download("RYSAS.IS", start="2019-01-01", end="2021-12-03",group_by="ticker") 
#df = yf.download("TUR", start="2000-01-01", end="2021-12-03",group_by="ticker") 


#print(df) 
print(infla) 
#print(df.AMZN)

'''
inflation is taken from ODA
Bigmac index is taken from the economist

scaling inflation value to align with local bigmac price
'''

infla["Value"]=infla["Value"] * 230 
data["local_price"].plot(figsize=(10,10),label="local price big Mac");
#data.legend();

#data["dollar_price"].plot(secondary_y=True,figsize=(10,10),label="price");
infla["Value"].plot(figsize=(10,10),label="inflation");

#df.plot(xlabel="RYSAS.IS",ylabel="High",figsize=(10,10),label="price");
#df["RYSAS.IS", "High"].plot(secondary_y=True,figsize=(10,10));
#df["Volume"].plot(figsize=(10,10));
plt.title(label="inflation in Indonesia",loc="left", fontstyle="italic", color="r")
plt.legend(loc="upper left")
plt.show()


