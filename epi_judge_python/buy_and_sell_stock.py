from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    rsI, rmI = 0, 0
    psI, pmI = 0,0
    for i, price in enumerate(prices):
      if price >= prices[psI]:
        if price - prices[psI] > prices[pmI] - prices[psI]:
          pmI = i
      else:
        if prices[pmI] - prices[psI] > prices[rmI] - prices[rsI]:
          rsI, rmI = psI, pmI
        psI, pmI = i, i        

    rSum = prices[rmI] - prices[rsI]
    pSum = prices[pmI] - prices[psI]
    return max(pSum,rSum)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
