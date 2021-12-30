from matplotlib.pyplot import ticklabel_format
import pandas as pd
import streamlit as st
import yfinance as yf
from yfinance import tickers
from yfinance.multi import download
from datetime import datetime

# Title of the page
st.title('Stock Information')

# Stock Ticker input by the user
ticker_symbol = st.text_input("Enter the ticker symbol:")

# Start and End date for the stock
start_date = str(st.date_input(label='Start Date'))
end_date = str(st.date_input(label='End Date'))

# Getting the data from yahoo! Finance
ticker = yf.Ticker(ticker_symbol)

# Shows the stock data by date-range  
ticker_data = ticker.history(period="max", start=start_date, end=end_date)

st.markdown('## Volume')
st.bar_chart(ticker_data.Volume)

st.markdown('## Close Price')
st.line_chart(ticker_data.Close)

st.markdown('## Open Price')
st.line_chart(ticker_data.Open)

st.markdown('## High')
st.line_chart(ticker_data.High)

st.markdown('## Low')
st.line_chart(ticker_data.Low)



