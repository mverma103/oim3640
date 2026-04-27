import yfinance as yf


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

    # Business summary - use AI API to expand this section
    print("\n==============================")
    print("BUSINESS SUMMARY")

    if data["summary"] is None:
        print("No business summary available.")
    else:
        print(data["summary"][:800] + "...")


def run_stock_analysis(ticker):
    """ Main function to run the stock analysis for a given ticker"""
    data = get_stock_data(ticker)

# Check if the company name/stock data was retrieved
    if data["name"] is None:
        print("Could not find stock data. Please check the ticker.")
    else:
        print_stock_report(data)


def main():
    while True:
        """ Prompts user for a stock ticker and runs the stock analysis"""
        ticker = input("Enter a stock ticker: ").upper()

        if ticker == "QUIT":
            break

        run_stock_analysis(ticker)


main()