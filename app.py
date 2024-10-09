# import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# load the dataset
df = pd.read_csv('gold_price_data.csv')

df.head()


# find no. of (rows, columns)
print(df.shape)

# dataset infomation (its type and no. of null values)
df.info()

# calculate the no. of missing values
df.isna().sum()

# dataset describtion (statistical details of datasets)
df.describe()

 # check the correlation between features
plt.figure(figsize=(6,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')

# check the correlation for in one features
print(df.select_dtypes(include=[np.number]).corr()['GLD'])

# check the distribution of the GLD price
sns.displot(df['GLD'], color='skyblue')

# spliting the features (select the features for input and target)
X = df.drop(['Date', 'GLD'], axis=1)
y = df['GLD']

# split the data as tarin and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# create and fit the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# find the predict value and error
y_pred = model.predict(X_test)

r2_score = r2_score(y_test, y_pred)
print("R2 Score : ", r2_score)

 # for web not only machine learning models

# libraries
import streamlit as st
from PIL import Image

# web app code
st.title("Gold Price Prediction Model")
img = Image.open('gold_price_image.png')
st.image(img, width=120, use_column_width=True)

st.subheader("Using Random Forest Regressor")
st.write(df)

st.subheader('Model Performance')
st.write(r2_score)
