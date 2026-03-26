## python -m pip install yfinance (into terminal)

import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
print(type(info))

print(len(info))
print(info['shortName'])
print(info['longName'])
print(info['currentPrice'])

#print(info['longBusinessSummary'])

print(info['longBusinessSummary'].split())
print('iPhone' in info['longBusinessSummary'])

print(info['city'])
info['city'] = 'Wellesley'
print(info['city'])


tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']
"""
print(prices)

print(sorted(prices)) # create a new list of the keys in prices, sorted alphabetically
print(sorted(prices.values()))

print(tickers)"""

total = 0
for price in prices.values():
    total += price
print(total)

tickers.append('GOOG')
print(tickers)
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']
print(prices)

tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
stocks = {} # {'NVDA': [open, currentPrice, volume]}

for t in tickers:
    #stocks[t] = yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume'] # create a tuple
    info_list = {}
    for name in ['open', 'currentPrice', 'volume']:
        info_list[name] = yf.Ticker(t).info[name]
    stocks[t] = info_list
print(stocks)