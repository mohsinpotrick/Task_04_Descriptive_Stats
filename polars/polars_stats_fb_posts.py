#!/usr/bin/env python
# coding: utf-8

# # Facebook Posts Analysis

# In[1]:


import polars as pl


fb_posts = pl.read_csv('./2024_fb_posts_president_scored_anon.csv')

#Columns to convert to numeric
numeric_cols = ['Likes', 'Comments', 'Shares', 'Total Interactions', 'Post Views']

#Clean and convert numeric columns
for col in numeric_cols:
    fb_posts = fb_posts.with_columns([
        pl.col(col).cast(pl.Utf8)  # cast to string first to avoid errors
              .str.strip_chars()
              .cast(pl.Float64, strict=False)  # coerce errors to null
              .alias(col)
    ])

#Function to print descriptive stats for each numeric column
def describe_and_print(df, col_name):
    stats = df.select([
        pl.col(col_name).count().alias("count"),
        pl.col(col_name).mean().alias("mean"),
        pl.col(col_name).std().alias("std"),
        pl.col(col_name).min().alias("min"),
        pl.col(col_name).max().alias("max"),
    ]).to_pandas().round(2)
    
    print(f"Descriptive stats for '{col_name}':")
    print(stats)
    print()

print("Descriptive Statistics for Numeric Columns:\n")
for col in numeric_cols:
    describe_and_print(fb_posts, col)

#Categorical variable Page Category
print("Page Category Analysis:")
unique_page_cat = fb_posts.select(pl.col('Page Category').n_unique()).item()
print(f"Total Unique Page Categories: {unique_page_cat}")

#Top 5 Most Common Page Categories using pandas value_counts
top_page_cats = fb_posts.select('Page Category').to_pandas()['Page Category'].value_counts().head(5)
print("Top 5 Most Common Page Categories:")
print(top_page_cats)

#Categorical variable Post Type
print("\nPost Type Analysis:")
unique_post_type = fb_posts.select(pl.col('Type').n_unique()).item()
print(f"Total Unique Post Types: {unique_post_type}")

#Top 5 Most Common Post Types
top_post_types = fb_posts.select('Type').to_pandas()['Type'].value_counts().head(5)
print("Top 5 Most Common Post Types:")
print(top_post_types)


# In[ ]:




