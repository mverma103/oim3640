from flask import Flask, render_template, request
from stock_info import get_web_analysis, format_large_number, format_percent, format_price #AI recommended this

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.post("/analyze")
def analyze():
    ticker = request.form.get("ticker")

    if not ticker:
        return render_template("index.html", error="Please enter a stock ticker.")

    ticker = ticker.upper()

    try:
        results = get_web_analysis(ticker)

        if results is None:
            return render_template("index.html", error="Could not find stock data. Please check the ticker.")

        return render_template(
            "results.html",
            results=results,
            data=results["data"],
            format_large_number=format_large_number,
            format_percent=format_percent,
            format_price=format_price
        )

    except Exception as e:
        return render_template("index.html", error=f"Something went wrong: {e}")


if __name__ == "__main__":
    app.run(debug=True)