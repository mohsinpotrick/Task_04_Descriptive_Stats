#!/usr/bin/env python
# coding: utf-8

# ## Facebook Posts Analysis

# In[2]:


import pandas as pd

#Load CSV into a DataFrame
fb_posts = pd.read_csv('./2024_fb_posts_president_scored_anon.csv')

#Columns to convert to numeric
numeric_cols = ['Likes', 'Comments', 'Shares', 'Total Interactions', 'Post Views']
fb_posts[numeric_cols] = fb_posts[numeric_cols].apply(pd.to_numeric, errors='coerce')

#Descriptive statistics for numeric columns
print("Descriptive Statistics for Numeric Columns:\n")
print(fb_posts[numeric_cols].describe().round(2))

#Categorical variable Page Category
print("\nPage Category Analysis:")
print(f"Total Unique Page Categories: {fb_posts['Page Category'].nunique()}")
print("Top 5 Most Common Page Categories:")
print(fb_posts['Page Category'].value_counts().head(5))

#Categorical variable Post Type
print("\nPost Type Analysis:")
print(f"Total Unique Post Types: {fb_posts['Type'].nunique()}")
print("Top 5 Most Common Post Types:")
print(fb_posts['Type'].value_counts().head(5))

