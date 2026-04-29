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

def assumptions_for_valuation(data):
    """ Prints the assumptions used for the simple valuation methods to help users understand the context of the implied prices"""
    
    sector = data["sector"]
    revenue_growth = data["revenue_growth"]
    operating_margin = data["operating_margin"]

    # default assumptions:
    target_pe = 20
    target_ev_ebitda = 12

    #sector based assumptions:
    if sector == "Technology":
        target_pe = 28
        target_ev_ebitda = 18
    elif sector == "Consumer Cyclical":
        target_pe = 22
        target_ev_ebitda = 13
    elif sector == "Consumer Defensive":
        target_pe = 18
        target_ev_ebitda = 11
    elif sector == "Healthcare":
        target_pe = 25
        target_ev_ebitda = 15
    elif sector == "Energy":
        target_pe = 12
        target_ev_ebitda = 7
    elif sector == "Financial Services":
        target_pe = 13
        target_ev_ebitda = 10

        # growth/margin based adjustments:
    if revenue_growth is not None and revenue_growth > 0.15:
        target_pe += 4
        if target_ev_ebitda is not None:
            target_ev_ebitda += 2

    if operating_margin is not None and operating_margin > 0.25:
        target_pe += 3
        if target_ev_ebitda is not None:
            target_ev_ebitda += 2

    return target_pe, target_ev_ebitda

def pe_valuation(data, target_pe):
    """ Simple P/E valuation method to calculate an implied stock price based on net income, shares outstanding, and a target P/E ratio"""

    net_income = data["net_income"]
    shares = data["shares_outstanding"]

    eps = net_income / shares
    implied_price = eps * target_pe

    return implied_price


def ev_ebitda_valuation(data, target_multiple):
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
    print("CONSERVATIVE VALUATION CASE")

    target_pe, target_ev_ebitda = assumptions_for_valuation(data)

    pe_price = pe_valuation(data, target_pe)

    if target_ev_ebitda is None:
        ev_ebitda_price = None
    else:
        ev_ebitda_price = ev_ebitda_valuation(data, target_ev_ebitda)

    blended_target = get_blended_target(pe_price, ev_ebitda_price)
    upside = calculate_upside(data["current_price"], blended_target)

    print(f"Current P/E: {data['pe_ratio']}")
    print(f"Conservative P/E Assumption: {target_pe}x")

    print(f"Current EV/EBITDA: {data['ev_to_ebitda']}")

    if target_ev_ebitda is None:
        print("Conservative EV/EBITDA Assumption: Not used for this sector")
    else:
        print(f"Conservative EV/EBITDA Assumption: {target_ev_ebitda}x")

    print(f"P/E Conservative Implied Price: {format_price(pe_price)}")
    print(f"EV/EBITDA Conservative Implied Price: {format_price(ev_ebitda_price)}")
    print(f"Blended Conservative Value: {format_price(blended_target)}")
    print(f"Implied Upside/Downside vs. Current Price: {format_percent(upside)}")


# helper function to run the simple valuation and return results as a tuple, important for AI API integration in next milestone
def get_simple_valuation_results(data):
    target_pe, target_ev_ebitda = assumptions_for_valuation(data)

    pe_price = pe_valuation(data, target_pe)

    if target_ev_ebitda is None:
        ev_ebitda_price = None
    else:
        ev_ebitda_price = ev_ebitda_valuation(data, target_ev_ebitda)

    blended_target = get_blended_target(pe_price, ev_ebitda_price)
    upside = calculate_upside(data["current_price"], blended_target)

    return target_pe, target_ev_ebitda, pe_price, ev_ebitda_price, blended_target, upside

# OpenAI API SECTION - used AI to help with this part of the code

def generate_full_ai_analysis(data):
    """Generates a full equity research report including memo + bull/base/bear in ONE API call"""

    target_pe, target_ev_ebitda, pe_price, ev_ebitda_price, blended_target, upside = get_simple_valuation_results(data)

    prompt = f"""
    Write a detailed equity research report for {data['ticker']}.

    IMPORTANT:
    - Focus on insights, trends, and implications (not just repeating numbers)
    - Use the data provided but interpret it
    - Do NOT make up data
    - Keep it professional, like an equity research analyst

    ----------------------------
    COMPANY DATA
    ----------------------------
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

    ----------------------------
    CONSERVATIVE VALUATION CASE
    ----------------------------
    Current P/E: {data['pe_ratio']}
    Conservative P/E Assumption: {target_pe}
    P/E Implied Price: {pe_price}

    Current EV/EBITDA: {data['ev_to_ebitda']}
    Conservative EV/EBITDA Assumption: {target_ev_ebitda}
    EV/EBITDA Implied Price: {ev_ebitda_price}

    Blended Conservative Value: {blended_target}
    Implied Upside/Downside: {upside}

    These are conservative estimates — NOT exact price targets.

    ----------------------------
    BUSINESS SUMMARY
    ----------------------------
    {data['summary']}

    ----------------------------
    OUTPUT FORMAT
    ----------------------------

    Investment Memo:

    1. Business Overview
    (high-level summary of company and positioning)

    2. Financial Analysis
    (growth, margins, profitability insights)

    3. Valuation View
    (compare conservative valuation vs current market)

    4. Key Risks
    (2-4 real risks)

    5. Final Recommendation
    (Buy / Hold / Sell with reasoning)

    ----------------------------

    Bull / Base / Bear Case:

    Bull Case:
    - 
    - 

    Base Case:
    - 
    - 

    Bear Case:
    - 
    - 

    Keep analysis concise but insightful.
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": "You are a professional equity research analyst. Be analytical, structured, and realistic."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def get_web_analysis(ticker):
    """Runs the stock analysis and returns data for the Flask web app."""

    data = get_stock_data(ticker)

    if data["name"] is None:
        return None

    target_pe, target_ev_ebitda, pe_price, ev_ebitda_price, blended_target, upside = get_simple_valuation_results(data)

    ai_analysis = generate_full_ai_analysis(data)

    results = {
        "data": data,
        "target_pe": target_pe,
        "target_ev_ebitda": target_ev_ebitda,
        "pe_price": pe_price,
        "ev_ebitda_price": ev_ebitda_price,
        "blended_target": blended_target,
        "upside": upside,
        "ai_analysis": ai_analysis
    }

    return results


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

if __name__ == "__main__":
    main()