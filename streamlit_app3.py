# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:49:40 2024

@author: Tajudeen
"""

from streamlit_echarts import st_echarts
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


st.image('chpc-nithecs.png') 
st.title('CSS Project - Option 2: Streamlit')

df = pd.read_csv("iris.csv")
st.write(df.head())

selected_x = st.selectbox('What do want the x variable to be?', 
  ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']) 
selected_y = st.selectbox('What about the y?', 
  ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']) 

#st.scatter_chart(df,x=selected_x, y=[selected_y])

sns.set_style('darkgrid')
sns.set_style('darkgrid')
markers = {"Versicolor": "X", "Virginica": "s", "Setosa":'o',
           }
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = df, x = selected_x, 
  y = selected_y, hue = 'variety', markers = markers,
  style = 'variety') 
plt.xlabel(selected_x) 
plt.ylabel(selected_y) 
plt.title("Scatterplot of Iris's Data") 
st.pyplot(fig) 

