#!/usr/bin/env python
# coding: utf-8

# # Twitter Posts Analysis

# In[1]:


import pandas as pd

#Load the dataset with pandas
tw = pd.read_csv('./2024_tw_posts_president_scored_anon.csv')

#Converting numeric columns from string to numbers, coercing errors to NaN
numeric_cols = ['likeCount', 'retweetCount', 'replyCount', 'viewCount']
for col in numeric_cols:
    tw[col] = pd.to_numeric(tw[col], errors='coerce')

#Displaying descriptive statistics using DataFrame.describe()
print("Descriptive statistics:\n")
print(tw[numeric_cols].describe().round(2))

#Counting unique values for categorical columns
print("\nUnique counts for categorical columns:")
print(f"Unique languages: {tw['lang'].nunique()}")
print(f"Unique sources: {tw['source'].nunique()}")

#Displaying the most frequent values using value_counts()
print("\nTop 3 most common languages:")
print(tw['lang'].value_counts().head(3))

print("\nTop 3 most common sources:")
print(tw['source'].value_counts().head(3))

