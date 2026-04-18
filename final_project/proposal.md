# Final Project - AI Equity Research Assistant

## What I'm building 

I'm building a Flask web app where a user can enter a stock ticker and receive an AI-assisted stock analysis report (either using OpenAI or Claude API). The app will pull financial data from Yahoo Finance, give a quick display of the data, provide the user with all valid metrics, any news (like quarterly updates or any big headlines), use simple financial valuation methods (I have learned from other classes), and provide a simple bull/bear (maybe also base) case scenarios for the stock. 

The goal of this tool is to generate an equity research style memo for the user. Obviously AI should not be used to give financial advice so this would be just more of an analytical tool (and maybe where the web app can do the valuation calculations based on user input to provide more accurate data)


## Why I chose this

I chose this idea because it combines what we have learned all class with my concentration of finance, something I am generally interested in, especially since I have taken classes in stock analysis, equity research, risk management, etc. I feel this idea is the most applicable, that it is a partical and feels like a real tool instead of an exercise, since it helps organize financial data and turn it into a more readable analysis for someone looking at a company. It will help me also develop my skills of Flask and API's, especially leveraging AI api's for code which was one of my goals before taking this course. 


## MVP vs. Stretch Goals: 

For the MVP:
- a .py file that uses yahoo finance to pull news, company and stock data
- a flask homepage where the user can enter a stock ticker
-  display metrics like price, market cap, margins, growth, valuation multiples, etc.
-  run very simple valuation methods, like P/E and EV/EBITDA
-  use an AI API to generate a short investment memo + bull/base/bear case summary

Stretch Goals:
- Add charts and visualizations for stock performance and valuation outputs
- run more defined valuation methods, still including P/E, EV/EBITDA, but also Price/Sales, and basic DCF model
- let the user adjust valuation assumptions from the page and getting real time outputs based on those changes
- export the data/memo to PDF for a clean formatted report
- improve the design to make it feel like a real (company level) research dashboard


## What I don't know yet

- How I want to structure all of the files, especially the Flask routes and templates for a larger project like this
- Decide between Claude's and OpenAI's API, do some research to see if there is one better for this type of analysis
- How reliable Yahoo Finance data will be across different stocks and what missing fields I may need to handle (or maybe research if there is a more specific API for better live data for this project)
- How to prompt engineer the AI output to make sure it is grounded in the actual financial data and not being too generic
- How much valuation detail is actually realistic for the MVP versus what should stay as a stretch goal (too many valuations could be overambitious)
