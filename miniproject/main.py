import requests
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Replace with your Alpha Vantage API key
api_key = '8zaJca9wPBJPHdXO2ozRab021EfkCA6K'

# Define the stock symbol and time frame
symbol = 'AAPL'  # Apple Inc. stock symbol
interval = '1min'  # You can choose a different time frame

# Initialize the Alpha Vantage client
ts = TimeSeries(key=api_key, output_format='pandas')

# Fetch historical stock data
data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize='compact')

# Extract the timestamp and closing prices
timestamps = data.index
prices = data['4. close']

# Plot the stock price data
plt.figure(figsize=(12, 6))
plt.title(f'{symbol} Stock Price')
plt.plot(timestamps, prices, label='Closing Price', color='blue')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

# Perform a simple stock price prediction (e.g., 5-minute ahead prediction)
prediction = prices.shift(-5)  # Shifting 5 time periods ahead

# Plot the predicted prices
plt.figure(figsize=(12, 6))
plt.title(f'{symbol} Stock Price Prediction')
plt.plot(timestamps, prices, label='Actual Price', color='blue')
plt.plot(timestamps, prediction, label='Predicted Price', color='red')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

# Show the plots
plt.show()
