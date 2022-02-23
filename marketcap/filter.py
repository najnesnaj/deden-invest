#from datetime import datetime
import csv




def filter():
#    try:
    print ("test")
    with open('list', 'r') as fin:
        dr = csv.DictReader(fin,delimiter=',')
        for rij in dr:
            #Anthony Deden : under 10 billion and above 100 million
            if int(rij['marketcap']) > 100000000 and int(rij['marketcap']) < 10000000000:
                #"Rank","Name","Symbol","marketcap","price (USD)","country"
                print (rij['Symbol'],rij['marketcap'],rij['country'])
#filter()
#    return


filter()
