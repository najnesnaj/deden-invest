import os
import fileinput
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import seaborn as sns

import yfinance as yf
import sqlite3

from bokeh.plotting import ColumnDataSource, figure, output_file, show, save
from bokeh.layouts import gridplot
from bokeh.models import HoverTool, BoxAnnotation, Span, Label, Arrow, NormalHead
from collections import OrderedDict
from datetime import date, timedelta, datetime
from pandas import to_datetime






def analyze_stock(stockname='', ticker='', PLOT_OFFSET = 0, IS_SHOW=True, transactions=''):
    """ Analysis of stock price since last reporting and filing day """
    
    # Retrieve stock data from Yahoo finance
    try:
        stock = yf.Ticker(ticker)
    except Exception:
        return
    hist = stock.history(period="max") # All historical data

    # Define important dates (datetime)
    #REPORT_START = self.previous_report_date    # Previous reporting day
    #REPORT_END = self.current_report_date       # Current reporting day
    #REPORT_FILING = self.current_filing_date    # Current filing day (ca. 60 days delay) 
    
    TODAY = date.today()
    YESTERDAY = TODAY - timedelta(days = 1)
    
    # Create dataframe from Reporting day - offset until most recent trading day
    START = YESTERDAY - timedelta(days = PLOT_OFFSET)
    df=hist.loc[START:]
    jf=df
    maximum = max(df.High)
    minimum = min(df.Low)
    newjf = jf.join(transactions)
    aantalsell=0
    aantalbuy=0
    for idx in newjf.index:
        #print(newjf['sellorbuy'].loc[idx])
        if newjf['sellorbuy'].loc[idx] == 'sell':
        #print(idx)
            newjf['Open'].loc[idx] = maximum 
            newjf['Close'].loc[idx] = minimum 
            aantalsell=aantalsell + 1
        elif newjf['sellorbuy'].loc[idx] == 'buy':
            newjf['Close'].loc[idx] = maximum 
            newjf['Open'].loc[idx] = minimum 
            aantalbuy = aantalbuy + 1
    #inc = df.Close > df.Open
    #dec = df.Open > df.Close
    inc = newjf.Close > newjf.Open
    dec = newjf.Open > newjf.Close
    # Convert DataFrame to ColumnDataSource
    source = ColumnDataSource(ColumnDataSource.from_df(newjf))
    source_dec = ColumnDataSource(ColumnDataSource.from_df(newjf[dec]))
    source_inc = ColumnDataSource(ColumnDataSource.from_df(newjf[inc]))
    
    # 1st Plot: Candlestick
    # Plot parameters
    WITDH = 1500
    HEIGHTVOL = 300
    BARWITDH = 16*60*60*1000
    
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    
    # Create plot
    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=WITDH, title = stockname +' (' + ticker +'), ' +'Portfolio: ' )
    p.grid.grid_line_alpha=0.3
    p.segment('Date', 'High', 'Date', 'Low', source=source, color="black", name="segment")
    p.vbar('Date', BARWITDH, 'Open', 'Close', source=source_inc, fill_color="greenyellow", line_color="black")
    p.vbar('Date', BARWITDH, 'Open', 'Close', source=source_dec, fill_color="#F2583E", line_color="black")


    # Create tooltips
    p.add_tools(HoverTool(
        names=["segment"],
        tooltips=OrderedDict([
            ("Date", "@Date{%F}"),
            ("Open", '$@{Open}{0.2f}'),
            ("Close", '$@{Close}{0.2f}' ),
            ("Who?", '@fonds' ),
            ("price estimate", '@shareprice')]),
        formatters={
            '@Date': 'datetime'},
        mode='vline'))
    
    # Closing prices
    #PURCHASE_CLOSE_MIN = min(df.loc[REPORT_START:REPORT_END].Close)
    #PURCHASE_CLOSE_MAX = max(df.loc[REPORT_START:REPORT_END].Close)
    #YESTERDAY_CLOSE = df.loc[YESTERDAY].Close
    YESTERDAY_CLOSE = df.iloc[-1].Close
    
    # Add annotations
    #p.add_layout(BoxAnnotation(
    #left=REPORT_START, right=REPORT_END, 
    #fill_alpha=0.1, fill_color='green'))

    #p.add_layout(BoxAnnotation(
    #    left=REPORT_END, right=REPORT_FILING, 
    #    fill_alpha=0.06, fill_color='blue'))
    p.add_layout(Label(x=START , 
                       y=0, y_units='screen', 
                       text='(FUNDS BUYING = )' + str(aantalbuy)))
    p.add_layout(Label(x=START , 
                       y=20, y_units='screen', 
                       text='(FUNDS SELLING = )' + str(aantalsell)))
#    p.add_layout(Label(x=START , 
#                       y=40, y_units='screen', 
#                       text='(---INSIDER BUY = ---)'))
#    p.add_layout(Label(x=START , 
#                       y=60, y_units='screen', 
#                       text='(---INSIDER SELL = ---)'))
    ''' 
    p.add_layout(Label(x=REPORT_END + (REPORT_FILING-REPORT_END)/4, 
                       y=0, y_units='screen', 
                       text='(---Until filing---)'))
    p.add_layout(Label(x=REPORT_FILING + (TODAY-REPORT_FILING)/2, 
                       y=0, y_units='screen', 
                       text='(---After filing---)'))
    ''' 
    p.add_layout(Span(
        location=YESTERDAY_CLOSE, 
        dimension='width', 
        line_color='black', 
        line_dash='dotted', 
        line_width=0.5))
    '''  
    p.add_layout(Span(
        location=PURCHASE_CLOSE_MIN, 
        dimension='width', 
        line_color='black', 
        line_dash='dotted', 
        line_width=0.5))
    
    p.add_layout(Span(
        location=PURCHASE_CLOSE_MAX, 
        dimension='width', 
        line_color='black', 
        line_dash='dotted', 
        line_width=0.5))
    ''' 
    p.add_layout(Span(
        location=YESTERDAY_CLOSE, 
        dimension='width', 
        line_color='black', 
        line_dash='dotted', 
        line_width=0.5))
    ''' 
    p.add_layout(Label(
        x=REPORT_START, 
        y=PURCHASE_CLOSE_MIN, 
        text=''+str(PURCHASE_CLOSE_MIN)+' (Min. purchase price)'))
    
    p.add_layout(Label(
        x=REPORT_START, 
        y=PURCHASE_CLOSE_MAX, 
        text=''+str(PURCHASE_CLOSE_MAX)+' (Max. purchase price)'))
    
    p.add_layout(Label(
        x=REPORT_START, 
        y=YESTERDAY_CLOSE, 
        text=''+str(YESTERDAY_CLOSE)+' (Current price)'))
    p.add_layout(Arrow(
        start=NormalHead(fill_color="black",size=10),
        end=NormalHead(fill_color="black",size=10),
        x_start=TODAY, 
        y_start=PURCHASE_CLOSE_MIN, 
        x_end=TODAY, 
        y_end=YESTERDAY_CLOSE))
    
    p.add_layout(Label(
        x=TODAY + timedelta(days = 1), 
        y=PURCHASE_CLOSE_MIN + abs(PURCHASE_CLOSE_MIN-YESTERDAY_CLOSE)/2, 
        text=str(round((100*(YESTERDAY_CLOSE-PURCHASE_CLOSE_MIN)/PURCHASE_CLOSE_MIN),1))+"%"))
    ''' 
    
    
    # 2nd Plot: Volume
    q = figure(plot_height=HEIGHTVOL,
               plot_width = WITDH,
               x_axis_type='datetime',
               x_range=p.x_range, 
               title="Volume",
               tools=TOOLS)
    
    q.vbar('Date',
          top = 'Volume',
          source=source_inc,
          width = BARWITDH,
          fill_alpha = .5,
          fill_color="greenyellow", line_color="black")
    
    q.vbar('Date',
          top = 'Volume',
          source=source_dec,
          width = BARWITDH,
          fill_alpha = .5,
          fill_color="#F2583E", line_color="black")
    
    
    q.add_tools(HoverTool(
        tooltips=OrderedDict([
            ("Date", "@Date{%F}"),
            ("Open", '$@{Open}{0.2f}'),
            ("Close", '$@{Close}{0.2f}' ),
            ("Volume", "@Volume{($ 0.00 a)}")]),
        formatters={
            '@Date': 'datetime'},
        mode='vline'))
    
    
    # Stock 1st and 2nd plot
    plot = gridplot([[p], [q]])
    
    # Save in directory
    output_file(ticker+'_'+'_'+ str(YESTERDAY)+'.html', title=stockname +' (' + ticker +')', mode='inline')
    save(plot)
    
    if IS_SHOW==True:
        show(plot)  # Open in browser
    
    return





symbols = {
  'JACK IN THE BOX INC': 'JACK',
  'QORVO INC':'QRVO',
  'BOEING CO': 'BA',
  'EBAY INC': 'EBAY',
  'HCA HEALTHCARE INC': 'HCA',
  'VERINT SYS INC': 'VRNT',
  'VENTAS INC': 'VTR',
  'SS&C TECHNOLOGIES HLDGS INC': 'SSNC',
  'VIASAT INC': 'VSAT',
  'BED BATH & BEYOND INC': 'BBBY',
  'DISCOVERY INC (COM SER A)': 'DISCA',
  'TRIP COM GROUP LTD (ADS)': 'TCOM',
  'COPA HOLDINGS SA (CL A)': 'CPA',
  'HELMERICH & PAYNE INC': 'HP',
  'RETAIL OPPORTUNITY INVTS COR': 'ROIC',
  'PRECISION DRILLING CORP (COM 2010)': 'PDS',
  'KIMBALL INTL INC (CL B)': 'KBAL'
}

#previous 6 months
OFFSET = 180

#analyze_stock('BED BATH & BEYOND INC', symbols['BED BATH & BEYOND INC'], OFFSET, True)


conn = sqlite3.connect('edgardb/edgar.db')
cursor = conn.cursor()

cursor.execute('''SELECT distinct ticker from whodoneit;''')
#cursor.execute('''SELECT  distinct ticker from whodoneit where ticker = "DLR";''')
rows = cursor.fetchall()
rows_result = [x[0] for x in rows]
#print (rows_result)
for row in rows_result:
# get for each quote the transactionlines

    cursornieuw = conn.cursor()
    cursornieuw.execute('''SELECT extrainfo, sellorbuy, datepurchase, shareprice from whodoneit where ticker = (?) ;''', [row])
    selectie = cursornieuw.fetchall()
    df = pd.DataFrame(selectie, columns=['fonds','sellorbuy', 'datum', 'shareprice'])
    df['datum']=df['datum'] + ' 00:00:00'
    df['Date']=to_datetime(df['datum'])
    df.drop(['datum'], axis=1, inplace=True)
    df.sort_values(by=['Date'], inplace = True)
    df = df.reset_index(drop=True)

    for idx in df.index:
        if idx > 0:
            if df['Date'].loc[idx] <= df['Date'].loc[idx-1] :
                df['Date'].loc[idx] = df['Date'].loc[idx-1] + timedelta(1) 
    df.set_index('Date', inplace=True)    
#    print (df)
    analyze_stock(stockname='test', ticker=row, PLOT_OFFSET = OFFSET, IS_SHOW=False, transactions=df)



