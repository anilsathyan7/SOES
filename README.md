# SOES
Stock Order Execution System: A Lame Approach

---------------------------------------------------------------------
PROBLEM
---------------------------------------------------------------------
A stock order is an order to buy/sell a given quantity of stocks of specified company. Person willing to buy or sell a stock will submit an order to a stock exchange, where it is executed against the opposite side order of same company i.e, buy order is executed against an existing sell order and vice-versa. The criteria for stock orders execution is that, they should belong to same company, they are opposite sides ( Buy vs Sell), and order of arrival i.e, the order is executed against the first available order. The left over quantity after execution is called remaining quantity. For example, if a buy order of quantity 10 is executed against a sell order of quantity 5, the remaining quantity of buy and sell orders are 5 and 0 respectively. An order status is called OPEN if the remaining quantity is greater than zero(>0), otherwise it’s called CLOSED(i.e., remaining quantity = 0).  Implement stock order execution system which takes input orders from given CSV (SOES - Input.csv), processes them and prints the status, remaining quantity of all the orders as output.

---------------------------------------------------------------------
PREREQUISITES
---------------------------------------------------------------------
1. python
2. numpy
3. pandas
---------------------------------------------------------------------
CONTENTS
---------------------------------------------------------------------
1. SOES.py : SOES program in python
2. test_SOES.py : SOES program test cases (unit test)
3. out.txt : output file
4. Output.png : Sample output screenshot for given input
5. Test case inputs : SOES - Input.csv and 3 additional test cases.
6. soes_pd.py : soes solution using pandas (raw)

---------------------------------------------------------------------
HOW TO RUN
---------------------------------------------------------------------
1.'python SOES.py' from cmd/terminal or use 'Run' form IDE

2.'python soes_pd.py' from cmd/terminal or use 'Run' form IDE
