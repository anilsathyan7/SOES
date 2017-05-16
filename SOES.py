#!/usr/bin/env python

"""
The program implements a Stock Order Execution System (SOES),which
takes an Input of inital stocks in CSV format and generates the
stock at end after execution in a text file.The details included
are Stock Id,Side,Company,Quantity,Remainig Quantity and Status.
"""

__author__ = "Anil Sathyan"
__date__ = "10/07/16"
__version__ = "1.0"
__email__ = "anilsathyan7@gmail.com"
__status__ = "Production"

import csv
import sys
import time
import itertools

#Structure of stock-list and indexes 
list_attr=['Stock Id','Side','Company','Quantity','Remaining','Status']
side=list_attr.index('Side')
company=list_attr.index('Company')
quantity=list_attr.index('Quantity')
remaining=list_attr.index('Remaining')
status=list_attr.index('Status')

def stock_print(list):
    for i in range(0, len(list)):
        print ','.join(map(str, list[i]))


def parse_input(list):
    for i in range(1, len(list)):
        if int(list[i][3]) < 0:
            return False
    return list


def operate_stock(list,trans_a,trans_b):

        
            #check for same company,different side and positive quantity
            if all([trans_a[company] == trans_b[company], trans_a[side] != trans_b[side],
                    trans_a[remaining] > 0, trans_b[remaining] > 0]):

                if(trans_a[remaining] > trans_b[remaining]):
                    trans_a[remaining] = trans_a[remaining] - trans_b[remaining]
                    trans_b[remaining] = 0
                    trans_b[status] = 'Closed'
                else:
                    trans_b[remaining] = trans_b[remaining] - trans_a[remaining]
                    trans_a[remaining] = 0
                    trans_a[status] = 'Closed'
            return list


def main():

    # Read CSV to List
    with open('SOES - Input_L.csv', 'rb') as f:
        reader = csv.reader(f)
        list = []
        for row in reader:
            list.append(row)
    # Parse input to validate
    if(not(parse_input(list))):
        print 'Invalid input'
        sys.exit()
    # Initialize stock with live values and status
    for i in range(1, len(list)):
        list[i].extend((int(list[i][3]), 'Open'))
    
    #Process transactions
    print '\n Inital Stock\n'
    stock_print(list)

    start=time.clock()
    #Execute the matching transaction pairs for each combination
    for trans_a, trans_b in itertools.combinations(list[1:], 2):
        operate_stock(list,trans_a,trans_b)
    print time.clock() - start, "seconds process time"



    print '\n Final Stock \n'
    stock_print(list)

    # Write output  to file
    with open('out.txt', 'a+') as f:
        for i in range(0, len(list)):
            f.write(','.join(map(str, list[i])) + '\n')

if __name__ == '__main__':
    main()
