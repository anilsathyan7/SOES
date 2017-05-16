#!/usr/bin/env python

"""
The program implements three test cases for program SOES.py .
1. Under the assertion all entries are 'buy' ,no changes occur in stocks(edge case).
2. Under the assertion all entries are 'sell' ,no changes occur in stocks(edge case).
3. The quantity entry in input should be a positive value(exception).
"""

__author__ = "Anil Sathyan"
__date__ = "10/07/16"
__version__ = "1.0"
__email__ = "anilsathyan7@gmail.com"
__status__ = "Production"

import unittest
from SOES import operate_stock, parse_input


class StockTestCase(unittest.TestCase):
    """Tests for `operate_stock` and 'parse_input' in SOEST.py ."""

    def test_is_same_stock_buy(self):
        """Is stock changed if all are Buys?"""
        test_list = [
            [
                'Stock Id', 'Side', 'Company', 'Quantity'], [
                '1', 'Buy', 'ABC', '10', 10, 'Open'], [
                '2', 'Buy', 'XYZ', '15', 15, 'Open'], [
                    '3', 'Buy', 'ABC', '13', 13, 'Open'], [
                        '4', 'Buy', 'XYZ', '10', 10, 'Open'], [
                            '5', 'Buy', 'XYZ', '8', 8, 'Open']]
        self.assertEqual(test_list, operate_stock(test_list))

    def test_is_same_stock_sell(self):
        """Is stock changed if all are Sells?"""
        test_list = [
            [
                'Stock Id', 'Side', 'Company', 'Quantity'], [
                '1', 'Sell', 'ABC', '10', 10, 'Open'], [
                '2', 'Sell', 'XYZ', '15', 15, 'Open'], [
                    '3', 'Sell', 'ABC', '13', 13, 'Open'], [
                        '4', 'Sell', 'XYZ', '10', 10, 'Open'], [
                            '5', 'Sell', 'XYZ', '8', 8, 'Open']]
        self.assertEqual(test_list, operate_stock(test_list))

    def test_is_input_valid(self):
        """Is input valid?"""
        test_list = [
            [
                'Stock Id', 'Side', 'Company', 'Quantity'], [
                '1', 'Sell', 'ABC', '10', 10, 'Open'], [
                '2', 'Buy', 'XYZ', '-15', -15, 'Open'], [
                    '3', 'Sell', 'ABC', '13', 13, 'Open'], [
                        '4', 'Sell', 'XYZ', '10', 10, 'Open'], [
                            '5', 'Sell', 'XYZ', '8', 8, 'Open']]
        self.assertFalse(
            parse_input(test_list),
            msg='Quantity should be positive')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(StockTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
