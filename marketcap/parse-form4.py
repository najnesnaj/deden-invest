"""
Author: najnesnaj    
Date: 2022-02-07
MIT License
"""

from Retrieve4 import RetrieveForm4


### program get form4 for certain CIK, parses and stores in database
### purpose is to check if any insiders bought/sold shares, that the Guru's bought/sold


CIK_2 = '1065059'
Name_2 = 'LEU'
formstoget = 40

RetrieveForm4(CIK_2,Name_2,formstoget)


