# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load historical stock data
# Preprocess and engineer features
# Split data into training and testing sets

# Define and train a simple model (e.g., Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Visualize actual vs. predicted prices
plt.figure(figsize=(12, 6))
plt.title('Stock Price Prediction')
plt.plot(test_dates, y_test, label='Actual Price', color='blue')
plt.plot(test_dates, y_pred, label='Predicted Price', color='red')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

print(f"Root Mean Squared Error: {rmse}")
