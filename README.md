# Cryptocurrency Trading Simulator

This application is a simple cryptocurrency trading tool that uses Streamlit and Plotly to visualize the price of selected cryptocurrencies and simulate trading. Users can buy and sell cryptocurrencies using an initial virtual balance of $1,000,000 USD. The app uses Yahoo Finance data to provide real-time price updates and track users' profit/loss based on their trades.

[![](./Cryptocurrency_Exchange_Simulator/result.png)](https://github.com/Hyunji-Yun/Cryptocurrency_Exchange_Simulator/issues/1#issue-2682189248)

## Features

- Cryptocurrency Selection: Users can select from DOGE, BTC, or ETH to view price trends and make trades.

- Real-time Price Updates: Uses the yfinance library to fetch price data from Yahoo Finance.

- Buy and Sell Simulation: Users can buy or sell cryptocurrencies, and their balances are updated accordingly.

- Balance Display: Displays the user's current USD balance and cryptocurrency holdings.

- Profit/Loss Calculation: Tracks the user's profit or loss as a percentage of the initial investment.

## Dependency

- Streamlit

- Plotly

- yfinance

- Python

## Running the Application

To run the application locally:

1. Clone the repository.

2. Install the required libraries: streamlit, yfinance, plotly.


    pip install streamlit yfinance plotly


3. Run the Streamlit app.


    streamlit run main.py
    

4. Access the app in your web browser at the URL provided by Streamlit.

## Future Improvements

Add More Cryptocurrencies: Add more cryptocurrencies for users to choose from.

Historical Data Analysis: Provide users with the ability to view longer historical trends and perform technical analysis.

User Authentication: Add login functionality to allow users to track trades across sessions.

Persistent Data Storage: Store user balances and trade history in a database for long-term tracking.


