"""
Author: najnesnaj 
Date: 2022-07-02
MIT License


todo -- one place to define dir

"""

import os
import fileinput
import numpy as np
import pandas as pd
from secedgar import filings, FilingType
#import matplotlib
#matplotlib.use('Qt5Agg')
#import matplotlib.pyplot as plt
#import matplotlib.colors as colors
#import matplotlib.cm as cmx
#import seaborn as sns
from bs4 import BeautifulSoup
import yfinance as yf
import sqlite3

#from bokeh.plotting import ColumnDataSource, figure, output_file, show, save
#from bokeh.layouts import gridplot
#from bokeh.models import HoverTool, BoxAnnotation, Span, Label, Arrow, NormalHead
#from collections import OrderedDict
from datetime import date, timedelta


class RetrieveForm4:
    """ 
        Class 
        1.  Retrieves form4 filings from SEC Edgar database.
        2.  Parses forms
        3.  Stores in sqlite database

    """
    
    # If True prints out results in console
    debug = False
    
    def __init__(self,CIK='',Name='',formstoget=0):
        """ Sets up object """
        self.CIK = CIK # Company identifier: Central Index Key
        self.Name = Name # Company name
        self.backtrack = formstoget #number of form4 to trace back 
        # Directly call functions when filename is provided upon __init__
        if self.CIK:
            self.retrieve_filings(self.CIK, self.backtrack)
            self.parse_all()
            
            
    def retrieve_filings(self, CIK='', backtrack=0):
        """ Download latest filings from SEC Edgar system into directory in pseudo html/xml .txt format """
        self.CIK = CIK
#my_filings = filings(cik_lookup="0001067983",
#                     filing_type=FilingType.FILING_13FHR,
#                     user_agent="najnesnaj@gmail.com", count=4)

        
        self.filings = filings(cik_lookup=self.CIK,
                              #filing_type=FilingType.FILING_13F,
                              filing_type=FilingType.FILING_4,
                              user_agent="najnesnaj@gmail.com",
                              count=backtrack) # Set count=4 for the last four filings
        
        foldername = 'edgar-type4'
        self.filings.save(foldername)
        self.directory = foldername + '/' + self.CIK + '/4' # example: "Edgar filings_XML/CIK/13f"


        #for some reason the textfiles now contain extra text : ns1 - have to filter this out first

        #docs = [d for d in os.listdir(self.directory) if d.endswith('.txt')] # List of document names
        #for document in docs:
        #    fullpath = self.directory +'/' + document
        #    for line in fileinput.input(fullpath, inplace=True):
            # inside this loop the STDOUT will be redirected to the file
            # the comma after each print statement is needed to avoid double line breaks
        #        print(line.replace("ns1:", ""), end="")



        return

    def insertdb(self, transrecord):
        sqliteConnection = sqlite3.connect('edgardb/edgar.db')
        conn = sqlite3.connect('edgardb/edgar.db')
        cursor = sqliteConnection.cursor()
        cursor = conn.cursor()
        print ()
        print ("nieuw nieuw record")

#        for i in enumerate(transrecord):
        try: 
            cursor.execute('''INSERT INTO form4( 
            "transactionCode"  ,
            "securityTitle"  ,
            "transactionDate"  ,
            "transactionShares"  ,
            "transactionPricePerShare"  ,
            "transactionAcquiredDisposedCode"  ,
            "sharesOwnedFollowingTransaction"  ,
            "directOrIndirectOwnership"  ,
            "documentType"  ,
            "periodOfReport"  ,
            "issuerName"  ,
            "issuerTradingSymbol"  ,
            "rptOwnerCik"  ,
            "officerTitle"  ,
            "issuerCik"  ,
            "rptOwnerName"  
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' ,( 
            transrecord.get("transactionCode"),
            transrecord.get("securityTitle"),
            transrecord.get("transactionDate"),
            transrecord.get("transactionShares"),
            transrecord.get("transactionPricePerShare"),
            transrecord.get("transactionAcquiredDisposedCode"),
            transrecord.get("sharesOwnedFollowingTransaction"),
            transrecord.get("directOrIndirectOwnership"),
            transrecord.get("documentType"),
            transrecord.get("periodOfReport"),
            transrecord.get("issuerName"),
            transrecord.get("issuerTradingSymbol"),
            transrecord.get("rptOwnerCik"),
            transrecord.get("officerTitle"),
            transrecord.get("issuerCik"),
            transrecord.get("rptOwnerName")
            )
            )
            conn.commit()
        except sqlite3.Error as error:
            print("Error  sqlite", error)
#        
#        
        if conn:
            conn.close()


    def f_dictionary(self,form4_soup):
        form4_dict = {}
        debug = False
        form4_key_list = ['documentType', 'periodOfReport', 'issuerName', 'issuerTradingSymbol', 'rptOwnerCik',
                          'officerTitle', 'issuerCik', 'rptOwnerCik', 'rptOwnerName']
        for key in form4_key_list:
            find_key = form4_soup.find(key)
            if find_key:  # if the the key is found
                value = find_key.text
                if key == 'periodOfReport':
                    value = value[:10]  # remove trailing characters from date
                else:
                    pass
            else:  # if the key is not found
                if debug:
                    print ("no key found")
                value = "NaN"
            form4_dict.update({key: value})
    
            # derivativeTransaciton contains several value tags that make up a transaciton
        dt = form4_soup.findAll('derivativeTransaction')
        self.dict_list = []
        for value in dt:
            form4_dict_value = {}
            #         new_dict = {'transaction':'derivative'}
            # transactionCode does not contain a value tag
            tx_code = value.find('transactionCode')
            if tx_code:
                tx_code = tx_code.text
                form4_dict_value.update({'transactionCode': tx_code})
            else:
                pass
            # parents of value tags contain the name of the value
            value_tag = value.find_all('value')
            for tag in value_tag:
                y = tag.parent.name
                x = tag.text
                form4_dict_value.update({y: x})
            #             new_dict.update(form4_dict_value)
            #             dict_list.append(new_dict)
            form4_dict_value.update(form4_dict)
            self.dict_list.append(form4_dict_value)
    
        # nonDerivativeTransaciton contains several value tags that make up a transaciton
        ndt = form4_soup.findAll('nonDerivativeTransaction')
        for value in ndt:
            form4_dict_value = {}
            #         new_dict = {'transaction':'nonDerivative'}
            tx_code = value.find('transactionCode')
            # transactionCode does not contain a value tag
            if tx_code:
                tx_code = tx_code.text
                form4_dict_value.update({'transactionCode': tx_code})
            else:
                pass
            value_tag = value.find_all('value')
            for tag in value_tag:
                y = tag.parent.name
                x = tag.text
                form4_dict_value.update({y: x})
            #             new_dict.update(form4_dict_value)
            #             dict_list.append(new_dict)
            form4_dict_value.update(form4_dict)
            self.dict_list.append(form4_dict_value)
        return self.dict_list
    
    




    def parse_all(self):
        """ Creates parsed FORM 4 instance for all text documents in directory """
        foldername = 'edgar-type4'
        #self.filings.save(foldername)
        self.directory = foldername + '/' + self.CIK + '/4' # example: "Edgar filings_XML/CIK/13f"

        docs = [d for d in os.listdir(self.directory) if d.endswith('.txt')] # List of document names
    
    
        self.parsed_filings = []
        for doc in docs:
            filepath = self.directory + '/' + doc
            testdoc = open(filepath)
            soup = BeautifulSoup(testdoc, 'lxml-xml') # OBS! XML parser will not work with SEC txt format
    
            form4_dict = self.f_dictionary(soup)
            self.parsed_filings.append(form4_dict)
            teller = 0
        for lijst in self.parsed_filings:
            for dictionary in lijst:
                 self.insertdb(dictionary)
    
        return
        

    
