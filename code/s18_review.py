"""
words = 'the cat sat on the mat'.split()
len(words)
print(words)
print(len(set(words)))"""


"""
def mystery(s):
    return len(set(s)) == len(s)

print(mystery('hello'))                     # false
print(mystery({'a': 2, 'b': 3, 'c': 2}))    # true
print(mystery(['a', 'b', 'c', 'd', 'a']))   # false """



"""
import yfinance as yf
from pprint import pprint

tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
stocks = {}

for t in tickers:
    stocks[t] = yf.Ticker(t).info['currentPrice']

print(stocks)

def sort_by_price(t):
    return t[1]
    
print(sorted(stocks.items(), key=lambda t: t[1]))
"""

"""
num = 100
try:
    a = float(input("Enter a number to divide by: "))
    print(num / a)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("That's not a valid number")
finally:
    print('We still want to print this!')

print("Let's move on to the next part of the code ...")
"""

"""
names = ['Alice', 'Bob', 123, 'Charlie']
uppercase_names = []

for name in names:
    try:
        print(name.upper())
        uppercase_names.append(name.upper())
    except AttributeError:
        print(f"Error: {name} is not a string and cannot be converted to uppercase")

print("Uppercase names:", uppercase_names)

print("Lets move on to the next part of the code ...")
"""

