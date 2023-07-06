# -*- coding: utf-8 -*-
"""
@author: Noaht
"""

class Currency:
    def __init__(self, symbol, isLeft, isUSSystem, amount):
        self.symbol = symbol
        self.isLeft = isLeft
        self.isUSSystem = isUSSystem
        self.amount = amount
        
    def __str__(self):
        amount = "{:,.2f}".format(self.amount)
        if not self.isUSSystem:
            amount = amount.replace(".", "#").replace(",", ".").replace("#", ",")
        
        if self.isLeft:
            return "{}{}".format(self.symbol, amount)
        else:
            return "{}{}".format(amount, self.symbol)
    
def main():
    hongKongCurrency = Currency("HK$", True, True, 7882911.355)
    hungaryCurrency = Currency("Ft", False, False, 3719.34)
    switzerlandCurrency = Currency("fr", True, False, 2828128.4)
    saudiArabiaCurrency = Currency("SAR", False, True, 999999)
    print(hongKongCurrency)
    print(hungaryCurrency)
    print(switzerlandCurrency)
    print(saudiArabiaCurrency)
        
main()