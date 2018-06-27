import numpy as np
import pandas as pd

stocks=pd.read_csv('SOES - Input.csv',index_col='Stock Id') # read csv to a dataframe

print(stocks)	# print stock-dataframe


stocks=stocks.groupby('Company')	# group the data based on company

print(stocks.groups)	# show groups

for company, group in stocks:	# print the group dataframes
     print(company)
     print(group)

# iterate over rows in company-groups (dataframes)
for company in stocks:	
	for trans_a,trans_b in itertools.combinations(company[1].index,2):
             if company[1].at[trans_a,'Side'] != company[1].at[trans_b,'Side']:	# match buy and sell
                     temp=company[1].at[trans_a,'Quantity']
                     company[1].at[trans_a,'Quantity']=max( 0, company[1].at[trans_a,'Quantity'] - company[1].at[trans_b,'Quantity']) 
                     company[1].at[trans_b,'Quantity']=max( 0, company[1].at[trans_b,'Quantity'] - temp)
	     
	print(company[1])	# print the result

