import os
import yfinance as yf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def format_large_number(value):

    """ Formats large numbers into readable strings with appropriate suffixes K, M, B, T"""
    
    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"${value / 1_000_000_000_000:.2f}T"
    elif value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    else:
        return f"${value:,.0f}"


def format_percent(value):
    """ Formats a decimal value as a percentage string with two decimal places"""
    if value is None:
        return "N/A"

    return f"{value * 100:.2f}%"


def format_price(value):
    """ Formats a price value as a string with two decimal places and a dollar sign"""
    if value is None:
        return "N/A"

    return f"${value:.2f}"


def get_stock_data(ticker):
    """ Fetches stock data for a given ticker using yfinance and returns stock info"""
    stock = yf.Ticker(ticker)
    info = stock.info

    data = {
        "ticker": ticker,
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "market_cap": info.get("marketCap"),
        "enterprise_value": info.get("enterpriseValue"),
        "revenue": info.get("totalRevenue"),
        "ebitda": info.get("ebitda"),
        "net_income": info.get("netIncomeToCommon"),
        "shares_outstanding": info.get("sharesOutstanding"),
        "cash": info.get("totalCash"),
        "debt": info.get("totalDebt"),
        "revenue_growth": info.get("revenueGrowth"),
        "operating_margin": info.get("operatingMargins"),
        "profit_margin": info.get("profitMargins"),
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "ev_to_ebitda": info.get("enterpriseToEbitda"),
        "price_to_sales": info.get("priceToSalesTrailing12Months"),
        "summary": info.get("longBusinessSummary")
    }

    return data


def print_stock_report(data):
    """ Prints a formatted stock report based on the provided stock data"""


    # Company overview
    print("COMPANY OVERVIEW:")
    print(f"Company: {data['name']}")
    print(f"Ticker: {data['ticker']}")
    print(f"Sector: {data['sector']}")
    print(f"Industry: {data['industry']}")

    # Financial metrics
    print("\n==============================")
    print("KEY FINANCIAL METRICS")
    print(f"Current Price: {format_price(data['current_price'])}")
    print(f"Market Cap: {format_large_number(data['market_cap'])}")
    print(f"Enterprise Value: {format_large_number(data['enterprise_value'])}")
    print(f"Revenue: {format_large_number(data['revenue'])}")
    print(f"EBITDA: {format_large_number(data['ebitda'])}")
    print(f"Net Income: {format_large_number(data['net_income'])}")
    print(f"Cash: {format_large_number(data['cash'])}")
    print(f"Debt: {format_large_number(data['debt'])}")

    # Growth and profitability metrics
    print("\n==============================")
    print("GROWTH AND PROFITABILITY")
    print(f"Revenue Growth: {format_percent(data['revenue_growth'])}")
    print(f"Operating Margin: {format_percent(data['operating_margin'])}")
    print(f"Profit Margin: {format_percent(data['profit_margin'])}")

    # Valuation multiples
    print("\n==============================")
    print("VALUATION MULTIPLES")
    print(f"P/E Ratio: {data['pe_ratio']}")
    print(f"Forward P/E: {data['forward_pe']}")
    print(f"EV/EBITDA: {data['ev_to_ebitda']}")
    print(f"Price/Sales: {data['price_to_sales']}")

    # Business summary - can use AI API to expand this section
    print("\n==============================")
    print("BUSINESS SUMMARY")

    if data["summary"] is None:
        print("No business summary available.")
    else:
        print(data["summary"][:800] + "...")


## Milestone 1.5: simple valuations. want to allow user to input

def pe_valuation(data, target_pe=25):
    """ Simple P/E valuation method to calculate an implied stock price based on net income, shares outstanding, and a target P/E ratio"""
    net_income = data["net_income"]
    shares = data["shares_outstanding"]

    eps = net_income / shares
    implied_price = eps * target_pe

    return implied_price


def ev_ebitda_valuation(data, target_multiple=15):
    """ Simple EV/EBITDA valuation method to calculate an implied stock price based on EBITDA, debt, cash, shares outstanding, and a target EV/EBITDA multiple"""
    ebitda = data["ebitda"]
    debt = data["debt"] or 0
    cash = data["cash"] or 0
    shares = data["shares_outstanding"]

    implied_enterprise_value = ebitda * target_multiple
    implied_equity_value = implied_enterprise_value - debt + cash
    implied_price = implied_equity_value / shares

    return implied_price


def get_blended_target(pe_price, ev_ebitda_price):
    """ Calculates a blended target price by averaging the valid implied prices from the P/E and EV/EBITDA valuation methods"""
    
    valid_prices = []

    if pe_price is not None:
        valid_prices.append(pe_price)

    if ev_ebitda_price is not None:
        valid_prices.append(ev_ebitda_price)

    if len(valid_prices) == 0:
        return None

    return sum(valid_prices) / len(valid_prices)


def calculate_upside(current_price, target_price):
    if current_price is None or target_price is None or current_price == 0:
        return None

    upside = (target_price / current_price) - 1
    return upside


def print_simple_valuation(data):
    print("\n==============================")
    print("SIMPLE VALUATION")

    pe_price = pe_valuation(data, target_pe=25)
    ev_ebitda_price = ev_ebitda_valuation(data, target_multiple=15)
    blended_target = get_blended_target(pe_price, ev_ebitda_price)
    upside = calculate_upside(data["current_price"], blended_target)

    print(f"P/E Implied Price: {format_price(pe_price)}")
    print(f"EV/EBITDA Implied Price: {format_price(ev_ebitda_price)}")
    print(f"Blended Target Price: {format_price(blended_target)}")
    print(f"Upside/Downside: {format_percent(upside)}")


# helper function to run the simple valuation and return results as a tuple, important for AI API integration in next milestone
def get_simple_valuation_results(data):
    pe_price = pe_valuation(data, target_pe=25)
    ev_ebitda_price = ev_ebitda_valuation(data, target_multiple=15)
    blended_target = get_blended_target(pe_price, ev_ebitda_price)
    upside = calculate_upside(data["current_price"], blended_target)

    return pe_price, ev_ebitda_price, blended_target, upside

# OpenAI API SECTION - used AI to help with this part of the code

def generate_ai_memo(data):
    """ Generates an equity research memo using the OpenAI API based on the provided stock data and simple valuation results"""

    pe_price, ev_ebitda_price, blended_target, upside = get_simple_valuation_results(data)

    prompt = f"""
    Write a concise equity research memo for {data['ticker']}.

    Focus on insights, trends, and implications rather than repeating raw numbers. Use the provided data to support your analysis, but do not simply restate it. Instead, interpret what the data means for the company's business prospects and stock valuation.

    Company: {data['name']}
    Sector: {data['sector']}
    Industry: {data['industry']}
    Current Price: {data['current_price']}
    Market Cap: {data['market_cap']}
    Revenue: {data['revenue']}
    EBITDA: {data['ebitda']}
    Net Income: {data['net_income']}
    Revenue Growth: {data['revenue_growth']}
    Operating Margin: {data['operating_margin']}
    Profit Margin: {data['profit_margin']}
    P/E Ratio: {data['pe_ratio']}
    Forward P/E: {data['forward_pe']}
    EV/EBITDA: {data['ev_to_ebitda']}
    Price/Sales: {data['price_to_sales']}

    Simple valuation outputs:
    P/E implied price: {pe_price}
    EV/EBITDA implied price: {ev_ebitda_price}
    Blended target price: {blended_target}
    Upside/downside: {upside}

    Business summary:
    {data['summary']}

    Structure the memo with these sections:
    1. Business Overview
    2. Financial Analysis
    3. Valuation View
    4. Key Risks
    5. Final Recommendation

    Keep it professional, concise, and written like an equity research analyst.
    Do not make up data that was not provided.
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": "You are a careful equity research analyst. Use only the data provided and avoid making unsupported claims."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_bull_base_bear(data):
    """ Generates a bull, base, and bear case analysis using the OpenAI API based on the provided stock data and simple valuation results"""  

    pe_price, ev_ebitda_price, blended_target, upside = get_simple_valuation_results(data)

    prompt = f"""
    Create a bull, base, and bear case analysis for {data['ticker']}.

    Company: {data['name']}
    Sector: {data['sector']}
    Industry: {data['industry']}
    Current Price: {data['current_price']}
    Revenue Growth: {data['revenue_growth']}
    Operating Margin: {data['operating_margin']}
    Profit Margin: {data['profit_margin']}
    Debt: {data['debt']}
    Cash: {data['cash']}
    P/E Ratio: {data['pe_ratio']}
    EV/EBITDA: {data['ev_to_ebitda']}
    Blended Target Price: {blended_target}
    Upside/Downside: {upside}

    Format exactly like this:

    Bull Case:
    - 

    Base Case:
    - 

    Bear Case:
    - 

    Keep each case to 2-3 bullets.
    Do not make up financial data.
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": "You are a balanced equity research analyst. Be objective and avoid hype."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def run_stock_analysis(ticker):
    """ Main function to run the stock analysis for a given ticker"""
    data = get_stock_data(ticker)

# Check if the company name/stock data was retrieved
    if data["name"] is None:
        print("Could not find stock data. Please check the ticker.")
    else:
        print_stock_report(data)
        print_simple_valuation(data)

        # used AI to help print the memo & bull/bear/base case analysis
        print("\n==============================")
        print("AI-GENERATED MEMO:")
        memo = generate_ai_memo(data)
        print(memo)

        print("\n==============================")
        print("AI-GENERATED BULL/BASE/BEAR ANALYSIS:")
        cases = generate_bull_base_bear(data)
        print(cases)

def main():
    while True:
        """ Prompts user for a stock ticker and runs the stock analysis"""

        ticker = input("Enter a stock ticker: ").upper()

        if ticker == "QUIT":
            break

        run_stock_analysis(ticker)

main()