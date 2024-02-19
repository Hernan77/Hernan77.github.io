#!/usr/bin/env python
# coding: utf-8

# # HOW TO REMOVE TREND & SEASONALITY FROM TIME-SERIES DATA WITH PYTHON?
# 
# ref. https://coderzcolumn.com/tutorials/data-science/how-to-remove-trend-and-seasonality-from-time-series-data-using-python-pandas

# Both **Trends** and **Seasonality** are generally presented in the majority of time-series data of the real work. When we want to do the forecasting with time series, we need a **stationary time series**.
# 
# The **stationary time series** is time-series dataset where there is no trend or seasonality information present in it. The stationary time-series is a series with constant mean, constant variance, and constant autocorrelation.
# 
# To make time-series stationary, we need to find a way to remove trends and seasonality from out series so that we can use it with prediction models. To do that, we need to understand what is trends and seasonality in-depth to handle them better.
# 
# Apart from trend and seasonality, some time-series also have ***noise/error/residual*** component present as well. We can decompose time-series to see different components.

# # WHAT CAN YOU LEARN FROM THIS TUTORIAL?
# 
# As part of this tutorial, we hve explained how to detect and then remove trend as well as seasonality present in time-series dataset. We have explained different ways to remove trend and seasonality like power transformation, log transformation, moving window function, linear regression, etc., from data. Apart from this, we have also explained how to test for stationary once trend and seasonality are removed. This tutorial is good starting point for understanding concepts like trend, seasonality, stationary, etc.
# 
# Below, we have listed impoortant sections of this post to give an overview of the material covered.
# 
# ## IMPORTANT SECTIONS OF THE TUTORIAL
# 
# 1. Types of TIme-Series
# 2. What is Trend?
#     * Ways to remove Trend
# 3. What is seasonality?
#     * Ways to remove Seasonality
# 4. Load Dataset for Tutorial
# 5. Decompose Time-Series and See Individual Components
# 6. Checking Whether Time-Series is Stationary of Not
#     * Stationary Check by Calculating Change in Mean, Variance and & Auto-Covariance Over Time
#     * Stationary Check Using ACF Plot
#     * Dicky-Fuller Test for Stationarity
# 7. Remove Trend
#     * Logged Transformations
#     * Power Transformations
#     * Moving Window Functions
#     * Linear Regression to Remove Trend
# 8. Remove Seasonality
#     * Differencing Over Log Transformed Time-Series
#         - Test for Stationarity
#     * Differencing Over Power Transformed Time-Series
#     * Differencing Over Linear Regression Transformed Time-Series

# # TYPES OF TIME-SERIES
# 
# Time-series are of generally two types:
# 
# * **Additive Time-Series**: Additive time-series is time-series where components (trend, seasonality, noise) are added to generate time-series.
#     <br/>***Time Series = trend + seasonality + noise***
# * **Multiplicative Time-Series**: Multiplicative time-series is time-series where components (trend, seasonality, noise) are multiplied to generate time series. One can notice an increase in the amplitude of seasonality in multiplicative time-series.
#     <br/>***Time Series = trend * seasonality * noise***
#     
# <img src="IMAGES/FIG_1.png" alt="INTERRUPTED TIME SERIES" width="1200" height="900">
#    

# # TREND
# 
# The trend represents an increase or decrease in time-series value over time. If we notice that the value of measuurement over time is increasing or decreasing then we can say that it has an upward or downward trend.
# 
# ## HOW TO REMOVE TREND FROM TIME-SERIES DATA?
# 
# There are various ways to de-trend a time-series. We have explained a few below.
# 
# * Log Transformations.
# * Power Transformations.
# * Local Smoothing - Applying moving window functions to time-series data.
# * Differencing a time-series.
# * Linear Regression.

# # SEASONALITY
# 
# The seasonality represents variations in measured values which repeats over the same time interval regularly. if we notice that particular variations in value are happening every week, month, quarter or half-yearly then we can say that the time-series has some kind of seasonality.
# 
# ## HOW TO REMOVE SEASONALITY FROM TIME-SERIES DATA?
# 
# There are various ways to remove seasonality. The task of removing seasonality is a bit complicated. We have explained a few ways below to remove seasonality.
# 
# * Average de-trended values.
# * Differencing a Time-Series.
# * Use the Loess Method.

# # LOAD TIME SERIES DATASET
# 
# We'll now explore trend and seasonality removal with examples. We'll be using famous air passenger datasets available online for our purpose because it has both trend and seasonality. It has information about US airline from 1949 to 1960 recorded each month.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


air_passengers = pd.read_csv("AirPassengers.csv", index_col=0, parse_dates=True)
air_passengers.head()


# In[2]:


air_passengers.plot(figsize=(8,4), color="tab:red");


# In[3]:


air_passengers.info(verbose=True)
air_passengers['Year'] = air_passengers.index.year

air_passengers_1951 = air_passengers[(air_passengers.Year == 1951)]["#Passengers"]
air_passengers_1951.plot(kind="bar", color="tab:red", legend=False);


# In[4]:


air_passengers_1952 = air_passengers[(air_passengers.Year == 1952)]["#Passengers"]
air_passengers_1952.plot(kind="bar", color="tab:red", legend=False);


# By looking at the above plots we can see that our time-series is multiplicative and has both trend as well as seasonality. We can see the trend as passengers are constantly increasing over time. We can see seasonality with the same variations repeating for 1 year where value peaks somewhere around August.

# # DECOMPOSE TIME-SERIES TO SEE COMPONENTS (TREND, SEASONALITY, NOISE, ETC)
# 
# We can decompose a time-series to see various components of time-series. Python module named ***statsmodels*** provides us with easy to use utility which we can use to get an individual component of a time-series and then visualize it.

# In[5]:


import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

air_passengers = air_passengers["#Passengers"]
decompose_result = seasonal_decompose(air_passengers)

#decompose_result = season_decom(air_passengers)

trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.resid

decompose_result.plot();


# We can notice trend and seasonality components separately as well as the residual components. There is a loss of residual in the beginning which is settling later.

# # CHECKING WHETHER TIME-SERIES IS STATIONARY OR NOT

# As we declared above, time-series is stationary when mean, variance, and auto-covariance are in independent of time. We can check mean, variance, and auto-covariance using moving window functions available with pandas. We'll also use a ***Dicky-fuller test*** available with statsmodels to check the stationarity of time-series. If time-series is not stationary then we need to make it stationary.
# 
# Below we have taken an average over moving window of 12 samples. We noticed from the above plots that there is the seasonality of 12 moinths in time-series. We can try different window sizes for testing purposes.

# In[6]:


air_passengers.rolling(window = 12).mean().plot(figsize=(8,4), color="tab:red", title="Rolling Mean over 12 month period");


# In[7]:


air_passengers.rolling(window = 20).var().plot(figsize=(8,4), color="tab:red", title="Rolling variance over 20 month period");


# From the above two plots, we notice that the time-series has some kind of multiplicative effect which seems to be increasing with time period. We can see the low seasonality effect at the beginning which amplifies over time.
# 
# Below, we are also potting an auto-correlation plot for time-series data as well. This plot helps us understand whether present values of time-series are positively correlated, negatively correlated, or not related at all to pass values. ***statsmodels*** library provides ready to use method ***plot_acf*** as part of the module ***statsmodels.graphics.tsaplots***.

# In[8]:


from statsmodels.graphics.tsaplots import plot_acf
plot_acf(air_passengers);


# We can notice from the above chart that after 13 lags, the line gets inside the interval (light blue area). This can be due to seasonality of 12-13 months of our data.

# # DICKY-FULLER TEST FOR STATIONARITY
# 
# Once we have removed trend and seasonality from time-series data then we can test its stationarity using a ***Dicky-fuller test***. It's a statistical test to check the stationary of time-series data.
# 
# We can perfrom ***Dicky-Fuller test*** functionality with the ***statsmodels*** library.
# 
# Below we'll test the stationarity of our time-series with this functionality and try to interpret its results to better understand it.

# In[9]:


from statsmodels.tsa.stattools import adfuller

dftest = adfuller(air_passengers, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# We can interpret the above results based on p-values of results.
# 
# * p-value > 0.05 - This implies that time-series is ***non-stationary***.
# * p-value <= 0.05 - This implies that time-series is ***stationary***.
# 
# We can see from the above results that p-value is greater than 0.05. Hence, our time-series is not stationary. It still has time-dependent components present which we need to remove.

# # REMOVE TREND
# 
# There are various ways to remove trends from data as we have discussed above. We'll try ways like differencing, power transformation, log transformation, etc. 
# 
# ## LOGGED TRASFORMATION
# 
# To apply log transformation, we need to take a log of each individual value of time-series data.

# In[10]:


logged_passengers = air_passengers.apply(lambda x : np.log(x))

ax1 = plt.subplot(121)
logged_passengers.plot(figsize=(12,4) ,color="tab:red", title="Log Transformed Values", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(color="tab:red", title="Original Values", ax=ax2);


# From the above first chart, we can see that we have reduced the variance of time-series data. We can look at y-values of original time-series data and log-transformed time-series data to conclude that the variance of time-series is reduced.
# 
# We can check whether we are successful or not by checking individual components of time-series by decomposing it as we had done above.

# In[11]:


decompose_result = seasonal_decompose(logged_passengers)
decompose_result.plot();


# **NOTE: Please make a NOTE that our time-series has both trend and seasonality. We are trying various techniques to remove trend in this section. We won't be testing for stationarity in this section. The next section builds on this section and explains various technqiues to remove stationarity. In that section, we have tested for stationarity. Please feel free to test stationarity after this section if your time series only has a trend.**

# ## POWER TRANSFORMATIONS
# 
# We can apply power transofrmation in data same way as that of log transformation to remove trend.

# In[12]:


powered_passengers = air_passengers.apply(lambda x : x ** 0.5)

ax1 = plt.subplot(121)
powered_passengers.plot(figsize=(12,4), color="tab:red", title="Powered Transformed Values", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# From the above first chart, we can see that we have reduced the variance of time-series data. We can look at y-values of original time-series and power-transformed time-series data to conclude that the variance of time-series is reduced.
# 
# We can check whether we are successful or not by checking individual components of time-series by decomposing it as we had done above.

# In[13]:


decompose_result = seasonal_decompose(powered_passengers)
decompose_result.plot();


# ## APPLYING MOVING WINDOW FUNCTIONS
# 
# We can calculate rolling mean over a period of 12 months and subtract it from time-series to get de-trended time series.

# In[14]:


rolling_mean = air_passengers.rolling(window = 12).mean()
passengers_rolled_detrended = air_passengers - rolling_mean

ax1 = plt.subplot(121)
passengers_rolled_detrended.plot(figsize=(12,4),color="tab:red", title="Differenced With Rolling Mean over 12 month", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# From the above first chart, we can see that we seem to have removed trend from time-series data.
# 
# We can check whether we are successful or not by checking individual components of time-series by decomposing it as we had done above.

# In[15]:


decompose_result = seasonal_decompose(passengers_rolled_detrended.dropna())
decompose_result.plot();


# ## APPLYING MOVING WINDOW FUNCTION ON LOG TRANSFORMED TIME-SERIES
# 
# We can apply more than one transformation as well. We'll first apply log transformation to time-series, then take a rolling mean over a period of 12 months and then substract rolled time-series from log-transformed time-series to get final time-series.

# In[16]:


logged_passengers = pd.DataFrame(air_passengers.apply(lambda x : np.log(x)))

rolling_mean = logged_passengers.rolling(window = 12).mean()
passengers_log_rolled_detrended = logged_passengers - rolling_mean


ax1 = plt.subplot(121)
passengers_log_rolled_detrended.plot(figsize=(12,4),color="tab:red", title="Log Transformation & Differenced With Rolling Mean over 12 month", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# From the above the first chart, we can see that we are able to remove the trend from the time-series data. We can check whether we are succesful or not by checking individual components of time-series by decomposing it as we had done above.

# In[17]:


decompose_result = seasonal_decompose(passengers_log_rolled_detrended.dropna())
decompose_result.plot();


# ## APPLYING MOVING WINDOW FUNCTION ON POWER TRANSFORMED TIME-SERIES
# 
# We can apply more than one transformation as well. We'll first apply power transformation to time-series, then take a rolling mean over a period of 12 months and then subtract rolled time-series from power-transformed time-series to get final time-series.

# In[18]:


powered_passengers = pd.DataFrame(air_passengers.apply(lambda x : x ** 0.5))

rolling_mean = powered_passengers.rolling(window = 12).mean()
passengers_pow_rolled_detrended = powered_passengers - rolling_mean


ax1 = plt.subplot(121)
passengers_pow_rolled_detrended.plot(figsize=(12,4),color="tab:red", title="Power Transformation & Differenced With Rolling Mean over 12 month", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# From the above the first chart, we can see that we are able to remove the trend from time-series data.
# 
# We can check whether we are successful or not by checking individual components of time-series by decomposing it as we had done above.

# In[19]:


decompose_result = seasonal_decompose(passengers_pow_rolled_detrended.dropna())
decompose_result.plot();


# ## APPLYING LINEAR REGRESSION TO REMOVE TREND
# 
# We can also apply a linear regression model to remove the trend. Below we are fitting a linear regression model to our time-series data. We are then using a fit model to predict time-series values from beginning to end. We are then subtracting predicted values from original time-series to remove the trend.

# In[20]:


from statsmodels.regression.linear_model import OLS

least_squares = OLS(air_passengers.values, list(range(air_passengers.shape[0])))
result = least_squares.fit()

fit = pd.Series(result.predict(list(range(air_passengers.shape[0]))), index = air_passengers.index)

passengers_ols_detrended = air_passengers - fit


ax1 = plt.subplot(121)
passengers_ols_detrended.plot(figsize=(12,4), color="tab:red", title="Linear Regression Fit", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# From the above the first chart, we can see that we are able to remove the trend from the time-series data.
# 
# We can check whether we are successful or not by checking individual components of time-series by decomposing it as we had done above.

# In[21]:


decompose_result = seasonal_decompose(passengers_ols_detrended.dropna())
decompose_result.plot();


# After applying the above transformations, we can say that linear regression seems to have done a good job of removing the trend than other methods. We can confirm it further whether it did good by removing the seasonal component and checking stationary of time-series. 

# # REMOVE SEASONALITY
# 
# We can remove seasonality by differencing technique. We'll use differencing over various de-trended time-series calculated above.
# 
# ## DIFFERENCING OVER LOG TRANSFORMED TIME-SERIES
# 
# We have applied differencing to log-transformed time-series by shifting its value by 1 period and substracting it from original log-transformed time-series.

# In[22]:


logged_passengers_diff = logged_passengers - logged_passengers.shift()

ax1 = plt.subplot(121)
logged_passengers_diff.plot(figsize=(12,4), color="tab:red", title="Log-Transformed & Differenced Time-Series", ax=ax1)
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applying the **Dicky-Fuller test** which we had applied above.

# In[23]:


dftest = adfuller(logged_passengers_diff.dropna()["#Passengers"].values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **NOT STATIONARY** due to the p-value of 0.07 greater than 0.05.

# ## DIFFERENCING OVER POWER TRANSFORMED TIME SERIES
# 
# We have applied differencing to power transformed time-series by shifting its value by 1 period and substracting it from original power transformed time-series.

# In[24]:


powered_passengers_diff = powered_passengers - powered_passengers.shift()

ax1 = plt.subplot(121)
powered_passengers_diff.plot(figsize=(12,4), color="tab:red", title="Power-Transformed & Differenced Time-Series", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applying the **Dicky-Fuller test** which we had applied above.

# In[25]:


dftest = adfuller(powered_passengers_diff.dropna().values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **STATIONARY** due to a p-value of 0.02 less than 0.05.

# ## DIFFERENCING OVER TIME-SERIES WITH ROLLING MEAN TAKEN OVER 12 MONTHS
# 
# We have applied differencing to mean rolled time-series by shifting its value by 1 period and subtracting it from original mean rolled time-series
# 
# **IMPORTANT NOTE: PLEASE MAKE A NOTE THAT WE ARE SHIFTING TIME-SERIES BY 1 PERIOD AND DIFFERENCIATING IT FROM THE DE-TRENDED TIME SERIES. IT'S COMMON TO TRY SHIFTING TIME-SERIES BY DIFFERENT TIME-PERIODS TO REMOVE SEASONALITY AND GETTING STATIONARY TIME-SERIES.**

# In[26]:


passengers_rolled_detrended_diff = passengers_rolled_detrended - passengers_rolled_detrended.shift()

ax1 = plt.subplot(121)
passengers_rolled_detrended_diff.plot(figsize=(8,4), color="tab:red", title="Rolled & Differenced Time-Series", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applying the **Dicky-Fuller test** which we had applied above.

# In[27]:


dftest = adfuller(passengers_rolled_detrended_diff.dropna().values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **STATIONARY** die to a p-value of 0.02 less than 0.05.

# ## DIFFERENCING OVER LOG TRANSFORMED AND MEAN ROLLED TIME SERIES
# 
# We have applied differencing to log-transformed and mean rolled transformed time-series by shifting its value by 1 period and subtracting it from original time-series.

# In[28]:


passengers_log_rolled_detrended_diff = passengers_log_rolled_detrended - passengers_log_rolled_detrended.shift()

ax1 = plt.subplot(121)
passengers_log_rolled_detrended_diff.plot(figsize=(8,4), color="tab:red", title="Log-Transformed, Rolled & Differenced Time-Series", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applying the **Dicky-Fuller test** which we had applied above.

# In[29]:


dftest = adfuller(passengers_log_rolled_detrended_diff.dropna().values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **STATIONARY** due to p-alue of 0.001 less than 0.05.

# ## DIFFERENCING OVER POWER TRANSFORMED AND MEAN ROLLED TIME-SERIES
# 
# We have applied differencing to power transformed and mean rolled time-series by shifting its value by 1 period and subtracting it from orignal time-series.

# In[30]:


passengers_pow_rolled_detrended_diff = passengers_pow_rolled_detrended - passengers_pow_rolled_detrended.shift()

ax1 = plt.subplot(121)
passengers_pow_rolled_detrended_diff.plot(figsize=(8,4), color="tab:red", title="Power-Transformed, Rolled & Differenced Time-Series", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applyign the **Dicky-Fuller test** which we had applied above.

# In[31]:


dftest = adfuller(passengers_pow_rolled_detrended_diff.dropna().values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **STATIONARY** due to a p-value of 0.005 less than 0.05.

# ## DIFFERENCING OVER LINEAR REGRESSION TRANSFORMED TIME-SERIES
# 
# We have applied differencing to linear regression transformed time-series by shifting it's value by 1 period and substracting it from original log-transformed time-series.

# In[32]:


passengers_ols_detrended_diff = passengers_ols_detrended - passengers_ols_detrended.shift()

ax1 = plt.subplot(121)
passengers_ols_detrended_diff.plot(figsize=(8,4), color="tab:red", title="Linear Regression fit & Differenced Time-Series", ax=ax1);
ax2 = plt.subplot(122)
air_passengers.plot(figsize=(12,4), color="tab:red", title="Original Values", ax=ax2);


# We can now test whether our time-series is stationary of now by applying the **Dicky-Fuller test** which we had applied above.

# In[33]:


from statsmodels.tsa.stattools import adfuller

dftest = adfuller(passengers_ols_detrended_diff.dropna().values, autolag = 'AIC')

print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)


# From our **Dicky-Fuller test** results, we can confirm that time-series is **NOT STATIONARY** due to the p-value of 0.054 greater than 0.05.
# 
# This ends this small tutorial on handling the trend and seasonality with time-series data and various ways to remove them.

# # REFERENCES
# 
# * Time-Series : Dates, Times and TimeZone Handling using Pandas
# <br/>https://coderzcolumn.com/tutorials/data-science/dates-times-and-time-zone-handling-in-python-using-pandas
# * Time-Series : Resampling & Moving Window Functions
# <br/>https://coderzcolumn.com/tutorials/data-science/time-series-resampling-and-moving-window-functions
# * Time Series Analysis with Python Intermediate | SciPy 2016 Tutorial | Aileen Nielsen
# <br/>https://www.youtube.com/watch?v=JNfxr4BQrLk&list=PLs0VSVFbl2FLScd2l00ilW_KQEkhQd6nk&index=6&t=0s
# * https://machinelearningmastery.com/time-series-data-stationary-python/
