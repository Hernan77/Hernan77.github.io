#!/usr/bin/env python
# coding: utf-8

# # TIME SERIES WITH XGBOOST - ADVANCED METHODS
# 
# Ref. https://www.youtube.com/watch?v=z3ZnOW-S550
# <br>This Document Created by: Hernan Chavez<br/>
# Date: 2/29/2024

# # USING MACHINE LEARNING TO FORECAST ENERGY CONSUMPTION

# In[1]:


#pip install xgboost


# In[2]:


#pip install scikit-learn


# In[3]:


#pip install sklearn


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import xgboost as xgb
from sklearn.metrics import mean_squared_error # WE ARE GOING TO USE ROOT MEAN SQUARED ERROR

color_pal = sns.color_palette()
plt.style.use('fivethirtyeight')


# In[5]:


# READ THE DATA SET

df = pd.read_csv('PJME_hourly.csv')
df = df.set_index('Datetime')
df.index = pd.to_datetime(df.index)
df.head() # THE INDEX IS THE DATETIME COLUMN AND THE COLUMN IS THE MEGAWATTS WE ARE TRYING TO PREDICT


# In[6]:


# WE WANT TO VISUALIZE THIS DATA
df.plot(style='.', figsize=(15,5), color=color_pal[0], title='PJME Energy Use in MW')
plt.xticks(rotation=90)
plt.show()


# In[7]:


# WE CAN IDENTIFY SOME REALLY LOW VALUES THAT COULD POTENTIALLY REPRESENT OUTLIERs...MAYBE A BLACKOUT.
# WE MUST BE VERY CAREFUL ABOUT NOT REMOVING THINGS THAT MIGHT EXPLAIN DATA BEHAVIOR, AND THAT WE WOULD LIKE THE MODEL TO LEARN FROM.

df['PJME_MW'].plot(kind='hist', bins=500)


# In[8]:


# WE CAN SEE THAT MOST OF THE TIME VALUES ARE BETWEEN 20,000 AND ABOVE 50,000
# WE WANT TO LOOK AT WHEN VALUES ARE LOWER THAN THIS TO SEE IF THERE ARE ANY EXTREME OUTLIERS 
# THAT WE MIGHT WANT TO REMOVE.

df_outl = df.query('PJME_MW < 20000').plot(figsize=(15,5), style='.')
plt.xticks(rotation=90)
plt.show()


# In[9]:


# WE CAN SEE VALUES UNDER 20,000, 
# THERE IS THAT AREA WHERE WE SEE SOME OUTLIERS THAT DON'T LOOK LIKE THEY ARE LEGITIMATE


# In[10]:


# WE CAN MAKE THIS MORE OBVIOUS BY LOWERING THE THRESHOLD

df_outl = df.query('PJME_MW < 19000').plot(figsize=(15,5), style='.')
plt.xticks(rotation=90)
plt.show()


# In[11]:


# WE COULD USE THINGS LIKE STANDARD DEVIATIONS AND NUMBER OF OUTLIERS, BUT FOR NOW...
# WE WILL SETTLE WITH A VISUAL INSPECTION TO REMOVE OUR OUTLIERS.

df = df.query('PJME_MW >= 19000').copy()

df.plot(style='.', figsize=(15,5), color=color_pal[0], title='PJME Energy Use in MW')
plt.xticks(rotation=90)
plt.show()


# In[12]:


# NOW WE WILL DO A TRAIN/TEST SPLIT USING 'TIME SERIES CROSS VALIDATION'
# THERE IS A TOOL THAT ALLOWS US TO FIND THE MAX TRAINING SIZE (NUMBER OF SPLITS) 
# AND CREATE THOSE SPLITS FOR US.

from sklearn.model_selection import TimeSeriesSplit

tss = TimeSeriesSplit(n_splits=5, test_size=24*365*1, gap=24) #...ASSUMING WE WANT TO PREDICT 1 YEAR
df = df.sort_index() # IF THIS IS NOT SORTED... THEN TIME SPLIT WILL NOT WORK

# WE CAN ALSO DEFINE A GAP BETWEEN THE TRAINING AND THE VALIDATION SET WE ARE SPLITTING ON EACH TIME
# WE SET THAT TO 24 HOURS BETWEEN THE TRAINING SET AND THE TEST

# NOW WE LOOP OVER THE GENERATOR AND APPLYING IT OVER THE DATA SET
for train_idx, val_idx in tss.split(df):
    break

train_idx # THE INDICES IN THE DATAFRAME THAT WILL BE OUR TRAINING SET


# In[13]:


val_idx # THE VALIDATION INDICES


# In[14]:


# LET'S VISUALIZE THIS...

fig, axs = plt.subplots(5, 1, figsize = (15, 15), sharex = True)

fold = 0 # WE ARE GOING TO TRACT THE FOLDS
for train_idx, val_idx in tss.split(df):
    train = df.iloc[train_idx]
    test = df.iloc[val_idx]
    train['PJME_MW'].plot(ax=axs[fold], label='Training Set', title=f'Data Train/Test Split Fold {fold}')
    test['PJME_MW'].plot(ax=axs[fold], label='Test Set')
    axs[fold].axvline(test.index.min(), color='black', ls='--')
    fold += 1
plt.show()


# In[15]:


# WE CAN SEE HOW EACH FOLD WORKS...
# WE HAVE ONE YEAR OF VALIDATION SET ON EACH FOLD
# WE ARE TESTING EACH OF THESE FIVE YEARS (RED AREAS IN GRAPHS) INDEPENDENTLY. 
# IT IS IMPORTANT TO DO IT THIS WAY...
# FOR EXAMPLE WE WOULD NOT WANT TO TAKE OUT ONE YEAR AND TRAIN ON DATA AFTER IT
# THAT WOULD BE A LEAK ABOUT OUR TARGET INTO THIS VALIDATION.
# AND WHEN WE ARE RUNNING THIS WE ARE GOING TO BE DOING OUR CROSS VALIDATION WE WANT TO BE LEAK-FREE AS POSSIBLE


# In[16]:


# NOW LETS TALK ABOUT FORECASTING HORIZON (HOW FAR INTO THE FUTURE WE WANT TO PREDICT)

# GENERALLY THE FURTHER OUT INTO THE FUTURE, THE HARDER TO PREDICT

# ALSO, YOU CAN'T ADD LAG FEATURE BACK FURTHER THAN YOUR TIME HORIZON

# BUT FIRST LET'S ADD THE TIME SERIES FEATURES TO OUT DATA

def create_features(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

df = create_features(df)


# In[17]:


# THE WAY LAG FEATURES WORK IS: WE ARE ESSENTIALLY TELLING THE MODEL TO LOOK INTO THE PAST HOWEVER MANY DAYS AND 
# TO USE THE TARGET VALUE FOR THAT MANY DAYS IN THE PAST AS A NEW FEATURE THAT YOU FEED INTO THE MODEL. 

def add_lags(df):
    target_map = df['PJME_MW'].to_dict() # WHY 364 AND NOT 365, BECAUSE 364 IS DIVIDIBLE BY 7, 
    # SO WE ARE TAKING THE SAME DAY OF THE WEEK ONE YEAR INTO THE PAST

    # REMEBER THAT THE LAG CAN'T BE LONGER THAN YOUR FORECASTING HORIZON

    df['lag1'] = (df.index - pd.Timedelta('364 days')).map(target_map) # FOR 1 YEAR
    df['lag2'] = (df.index - pd.Timedelta('728 days')).map(target_map) # FOR 2 YEARS
    df['lag3'] = (df.index - pd.Timedelta('1092 days')).map(target_map) # FOR 3 YEARS
    return df

df = add_lags(df)
df.head()


# In[18]:


df.tail()


# In[19]:


# NOW WE ARE GOING TO PUT IT ALTOGETHER...

# WE HAVE OUR NEW LAG FEATURES,...

# WE HAVE OUR CORSS VALIDATION SETUP, AND...

# WE ARE GOING TO LOOP OVER THESE CROSS VALIDATIONS FOLDS AND TRAIN OUR MODEL,...

# WE ARE GOING TO TRAIN ON THE TRAINING AND TEST SET FROM THIS TRAIN TEST SPLIT FIVE DIFFERENT TIMES, AND...

# WE ARE GOING TO SCORE OUR MODEL USING THE MEAN SQUARE ERROR, AND...

# WE ARE GOING TO SAVE THOSE SCORES TO A LIST SO THAT WE CAN EVALUATE OUR SCORE ACROSS ALL DIFFERENT FOLDS...

# SO LET'S GO AHEAD AND RUN THIS TRAINING LOOP SO WE CAN SEE IT

fold = 0
preds = []
scores = []

for train_idx, val_idx in tss.split(df):
    train = df.iloc[train_idx]
    test = df.iloc[val_idx]
    
    train = create_features(train)
    test = create_features(test)
    
    FEATURES = ['dayofyear', 'hour', 'dayofweek', 'quarter', 'month', 'year', 'lag1', 'lag2', 'lag3']
    TARGET = 'PJME_MW'
    
    x_train = train[FEATURES]
    y_train = train[TARGET]
    
    x_test = test[FEATURES]
    y_test = test[TARGET]
    
    reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree', n_estimators=1000, early_stopping_rounds=50,
                          objective='reg:linear', max_depth=3, learning_rate=0.01)
    
    reg.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_test, y_test)], verbose=100)
    
    y_pred = reg.predict(x_test)
    preds.append(y_pred)
    score = np.sqrt(mean_squared_error(y_test, y_pred))
    scores.append(score)


# In[20]:


# SO ITS DONE TRAINING 5 FOLDS...

# WE HAVE RAN FIVE DIFFERENT EXPERIMENTS AND WE CAN SEE HOW THE SCORES ARE FOR EACH ONE OF THE FIVE, AND...

# IDEALLY THE MORE WE START HYPERPARAMETER TUNNING AND THE MORE FEATURES WE ADD, 

# WE WANT TO SEE THE SCORE GET BETTER ACROSS ALL OF THESE FOLDS,... 

# SO THERE ARE A FEW DIFFERENT WAYS OF JUST EVALUATING THIS

# THESE WOULD BE THE VALIDATION SCORES WE WOULD LIKE TO APPROVE UPON

print(f'Score across folds {np.mean(scores):0.4f}')
print(f'Fold scores: {scores}')


# In[21]:


# NOW WE'LL SHOW HOW TO PREDICT INTO THE FUTURE...

# BUT BEFORE, WE WANT TO TRAIN THE MODEL ONE MORE TIME WITH ALL THE TRAINING DATA...

# THIS IS IMPORTANT BECAUSE AFTER WE HAVE DONE THIS TRAIN VALIDATION FOR TIME SERIES
# WE STILL WANT TO LEVERAGE ALL THE DATA WE HAVE FOR OUR MODEL, THAT WE WILL BE USING TO
# FORECAST INTO THE FUTURE. 

# SO INSTEAD OF BEFORE WHERE WE CREATED THE X AND Y VALUE FROM THE TRAIN AND VALIDATION SEPARATELY,... 
# THIS TIME WE ARE GOING TO CREATE THE FEATURES ON ALL OF OUR DATA.

# WE HAVE ALSO CHANGED THE NUMBER OF ESTIMATORS THAT WE WILL TRAIN TO 500. 
# THE REASON FOR THAT IS BECAUSE WE CAN SEE ON THE RUNS FROM THE FOLDS 
# WHEN WE DID CROSS VALIDATION THAT AROUND THE 500th ITERATION
# IS WHEN THE MODELS START TO OVERFIT 
# SO YOU COULD ACTUALLY TAKE THE AVERAGE VALUE ACROSS FOLDS WHEN IT START TO OVERFIT...
# THIS WILL BE GOOD JUST FOR TRAINING HERE...
# AFTER 500 ITERATIONS THERE IS CHANCE THAT IT MIGHT BE OVERFITTING A LITTLE BIT TOO MUCH...

# SO WE'LL RUN  THIS TRAINING AGAIN ONE LAST TIME SO WE HAVE OUR REGRESSOR THAT WE WILL CALL REG

# RETRAIN ON ALL DATA
df = create_features(df)

FEATURES = ['dayofyear', 'hour', 'dayofweek', 'quarter', 'month', 'year', 'lag1', 'lag2', 'lag3']
TARGET = 'PJME_MW'

x_all = df[FEATURES]
y_all = df[TARGET]

reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree', n_estimators=500,
                          objective='reg:linear', max_depth=3, learning_rate=0.01)
    
reg.fit(x_all, y_all, eval_set=[(x_all, y_all)], verbose=100)


# In[22]:


# WE CAN CALL THE REGRESSOR REG AND PREDICT IN THE FUTURE...BUT FIRST WE NEED TO MAKE THIS FUTURE DATAFRAME
# AND WE CAN DO THAT PRETTY EASILY BY USING PANDA'S DATE RANGE FUNCTION...
# IF WE USE PD RANGE DATE WE CAN GIVE IT A START DATE AND END DATE AND...
# OTHER THINGS LIKE FREQUENCY, WHICH WILL BE IMPORTANT FOR US TO USE.

# IF WE LOOK AT OUR DATAFRAME  AND OUR INDEX MAX VALUE GOES UP TO 2018 SO WE'LL TAKE THIS DATE 
# AND ACTUALLY MAKE THIS THE FIRST DAY OF OUR FUTURE DATAFRAME THAT WE ARE GOING TO CREATE...
# JUST TO BE SAFE WE WILL JUST GO UP UNTIL THE FIRST DAY OF THAT MONTH AS OUR LAST DATE SO THIS IS 
# THE END DATE RANGE NOW...
# IF WE JUST RUN THIS YOU CAN TSEE THAT WE HAVE A LIST OF DATES FROM THE START TO THE END DATE

# BUT REMEMBER THAT WE WANT TO PREDICT HOURLY!!!!!
# SO WE ARE GOING TO ADD 'FREQ=1HOUR'
# NOW WE'LL HAVE HOURLY TIMESTAMPS BETWEEN THESE TWO DIFFERENT DATES
# NOW WE WANT TO CREATE A DATAFRAME OFF THIS AND WE WILL PASS THE INDEX AS THIS FUTURE DATES TIME STAMPS 
# WE CAN CALL THIS FUTURE_DF FOR FUTURE DATAFRAME

# BECAUSE WE HAVE LAG FEATURES WE WANT TO STICK THESE FEATURES DATAFRAME ONTO THE END OF OUR EXISTING DATA, SO
# WE CAN ADD THOSE LAG FEATURES CORRECTLY AND BEFORE WE DO THAT WE CREATE A COLUMN CALLED 'isFuture'...
# SO WE CAN EASILY IDENTIFY WHICH OF THE VALUES ARE FUTURE AND WHICH OF THE VALUES ARE NOT

# THEN WE WILL CREATE A NEW DATAFRAME WHICH IS JUST THE CONCATENATION OF OUR DATAFRAME WITH FUTURE AND 
# NOW IF WE LOOK AT DF_AND_FUTURE WE CAN SEE THAT IT GOES ALL THE WAY OUT TO THIS 2019 DATE.
# WE NEED TO REMEMBER TO CREATE OUR FEATURES ON TOP OF THIS AND ALSO CREATE OR ADD OUR LAG FEATURES
# AND THAT'S WHY IT'S NICE THAT WE CREATED THOSE FUNCTIONS. 

# NOW THAT WE HAVE ADDED OUR LAGS, WE CAN NOW EXTRAXT JUST THE FUTURE DATA BY USING DF_AND_FUTURE 
# AND QUERYING WHERE DF AND FUTURE "isFuture"....
# WE ARE GOING TO COPY IT AND CALL IT future_w_features. YOU CAN SEE IT GOES ALL THE WAY OUT INTO 2019.

# IT OBVIOUSLY DOESN'T HAVE THE TARGET BECAUSE WE DON'T KNOW THE TRUTH OF THAT...


# In[23]:


df.index.max()


# In[24]:


# Create future dataframe
future = pd.date_range('2018-08-03', '2019-08-01', freq='1h')
print(future)


# In[25]:


future_df = pd.DataFrame(index=future)
future_df['isFuture'] = True
df['isFuture'] = False
df_and_future = pd.concat([df, future_df])
df_and_future.head()


# In[26]:


df_and_future = create_features(df_and_future)
df_and_future = add_lags(df_and_future)
df_and_future.head()


# In[27]:


future_w_features = df_and_future.query('isFuture').copy()
future_w_features.tail()


# In[28]:


# NOW LET'S GO AHEAD AND TAKE OUR REGRESSOR AND PREDICT ON THIS FUTURE...
# OF COURSE WE NEED TO PROVIDE THE FEATURES THAT WE TRAINED OUR MODEL ON

future_w_features['pred'] = reg.predict(future_w_features[FEATURES])

future_w_features['pred'].plot(figsize=(10, 5),
                              color = color_pal[4],
                              ms=1,
                              lw=1,
                              title = 'Future Predictions')


# In[29]:


# NOW,... HOW TO SAVE OUR XGBOOST MODEL FOR LATER?
# LET'S SAY WE DIDN'T WANT TO RETRAIN THIS EVERY TIME WE WANT TO PREDCIT EVERY NEW DAY OR NEW HOUR
# WE CAN ACTUALLY SAVE THIS MODEL VERY EASILY USING SAVE MODEL METHOD ON THIS REGRESSOR
# SO WE ARE GOING TO SAVE THIS MODEL AS MODEL.JSON 

# Save model
reg.save_model('model.json')


# In[30]:


# WE CAN SHOW THAT WE CAN LOAD THIS BACK IN BY USING XGBOOST REGRESSOR 
# JUST LIKE WE DID BEFORE BY CALLING THIS OUR REG_NEW

reg_new = xgb.XGBRegressor()
reg_new.load_model('model.json')
future_w_features['pred'] = reg_new.predict(future_w_features[FEATURES])
future_w_features['pred'].plot(figsize=(10, 5),
                              color = color_pal[4],
                              ms=1,
                              lw=1,
                              title = 'Future Predictions')

