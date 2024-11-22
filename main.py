import yfinance as yf
import streamlit as st
import plotly.graph_objs as gr
from decimal import Decimal, ROUND_HALF_UP

# Supported cryptocurrencies
CRYPTO_NAMES = {
    'DOGE': 'DOGE-USD',
    'BTC': 'BTC-USD',
    'ETH': 'ETH-USD'
}

# Let the user select the cryptocurrency
st.set_page_config(layout='wide')
crypto_choice = st.sidebar.radio("Select Cryptocurrency", options=list(CRYPTO_NAMES.keys()))

NAME = CRYPTO_NAMES[crypto_choice]

# Initialize balances
if 'usd' not in st.session_state:
    st.session_state.usd = Decimal('1000000')

if crypto_choice not in st.session_state:
    st.session_state[crypto_choice] = Decimal('0')

if 'initial_usd' not in st.session_state:
    st.session_state.initial_usd = Decimal('1000000')

# Function to get data
@st.cache_data
def get_data(crypto_name):
    data = yf.download(tickers=crypto_name, period='1d', interval='1m')
    if data.empty:
        raise ValueError("No data fetched from yfinance")
    data.columns = ['_'.join(col) for col in data.columns]
    return data

# Function to get current price
def get_current_price(crypto_name):
    data = get_data(crypto_name)
    return Decimal(data.iloc[-1][f'Close_{crypto_name}']).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

# Fetch data for the selected cryptocurrency
data = get_data(NAME)
current_price = get_current_price(NAME)

# Create a two-column layout
col1, col2 = st.columns([3, 1])

with col1:
    st.header(f'{NAME} {current_price}')
    fig = gr.Figure(
        gr.Scatter(x=data.index, y=data[f'Close_{NAME}'])
    )
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Buy/Sell section
    st.header('Buy / Sell')

    # Buy cryptocurrency
    buy_amount = st.number_input('How many would you like to buy?', min_value=0, value=0, step=1, key="buy")
    if st.button('Buy'):
        buy_price = Decimal(buy_amount) * current_price

        if st.session_state.usd >= buy_price:
            st.session_state[crypto_choice] += Decimal(buy_amount)
            st.session_state.usd -= buy_price
            st.session_state.initial_usd += buy_price  # Update initial investment
            st.success(f'Bought {buy_amount} {crypto_choice} for ${buy_price:.2f}')
        else:
            st.warning('Not enough USD.')

    # Sell cryptocurrency
    sell_amount = st.number_input('How many would you like to sell?', min_value=0, value=0, step=1, key="sell")
    if st.button('Sell'):
        sell_price = Decimal(sell_amount) * current_price

        if st.session_state[crypto_choice] >= sell_amount:
            st.session_state[crypto_choice] -= Decimal(sell_amount)
            st.session_state.usd += sell_price
            st.success(f'Sold {sell_amount} {crypto_choice} for ${sell_price:.2f}')
        else:
            st.warning(f'Not enough {crypto_choice}.')

    # Display current balance
    st.subheader(f'My USD Balance: ${st.session_state.usd:.2f}')
    st.subheader(f'My {crypto_choice} Balance: {st.session_state[crypto_choice]:.2f} {crypto_choice}')

    # Display profit/loss
    total_in_usd = st.session_state.usd + (st.session_state[crypto_choice] * current_price)
    profit = (total_in_usd - st.session_state.initial_usd) / st.session_state.initial_usd * 100
    st.subheader(f'Profit/Loss: {profit:.9f}%')
