import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ===============================
# 1. Sidebar for controls
# ===============================
with st.sidebar:
    st.title('Controls')
    n = st.slider('Number of data points (n)', 100, 5000, 500)
    a = st.slider('Coefficient (a)', -10.0, 10.0, 5.0)
    var = st.slider('Noise variance (var)', 0, 1000, 100)
    new_area_input = st.number_input('Enter a new area to predict the price:', min_value=0, max_value=200, value=60)

# ===============================
# 2. Main area for output
# ===============================
st.title('Linear Regression with Streamlit')

# ===============================
# 3. Data generation and outlier detection
# ===============================
np.random.seed(42)
area = np.random.randint(20, 100, n)
noise = np.random.normal(0, np.sqrt(var), n)
price = area * a + noise

data = pd.DataFrame({'Area': area, 'Price': price})

# Outlier detection
Q1 = data['Price'].quantile(0.25)
Q3 = data['Price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data['is_outlier'] = (data['Price'] < lower_bound) | (data['Price'] > upper_bound)

st.write("First five rows of data:")
st.write(data.head())

# ===============================
# 4. Data preparation
# ===============================
X = data[['Area']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# 5. Modeling
# ===============================
model = LinearRegression()
model.fit(X_train, y_train)

# ===============================
# 6. Evaluation
# ===============================
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.write(f"Mean Squared Error (MSE): {mse:.2f}")
st.write(f"Coefficient of Determination (R^2): {r2:.2f}")
st.write(f"Intercept: {model.intercept_:.2f}, Coefficient: {model.coef_[0]:.2f}")

# ===============================
# 7. Visualization
# ===============================
fig, ax = plt.subplots()

inliers = data[~data['is_outlier']]
outliers = data[data['is_outlier']]

ax.scatter(inliers['Area'], inliers['Price'], color='blue', label='Inliers')
ax.scatter(outliers['Area'], outliers['Price'], color='red', label='Outliers')
ax.plot(X_test, y_pred, color='green', linewidth=2, label='Prediction line')

ax.set_title('Linear Regression: House Area vs. Price')
ax.set_xlabel('Area (square meters)')
ax.set_ylabel('Price (in 10,000s)')
ax.legend()
st.pyplot(fig)

# ===============================
# 8. Deployment (simple demonstration)
#    Predict new data
# ===============================
if new_area_input:
    new_area = np.array([[new_area_input]])
    predicted_price = model.predict(new_area)
    st.write(f"Predicted price for {new_area_input} ping: {predicted_price[0]:.2f} in 10,000s")
