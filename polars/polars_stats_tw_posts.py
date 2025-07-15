#!/usr/bin/env python
# coding: utf-8

# # Twitter Posts Analysis

# In[1]:


import polars as pl

tw = pl.read_csv('./2024_tw_posts_president_scored_anon.csv')

#Columns to convert to numeric
numeric_cols = ['likeCount', 'retweetCount', 'replyCount', 'viewCount']

#Clean and convert numeric columns
for col in numeric_cols:
    tw = tw.with_columns([
        pl.col(col).cast(pl.Utf8)
              .str.strip_chars()
              .cast(pl.Float64, strict=False)
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

print("Descriptive statistics:\n")

for col in numeric_cols:
    describe_and_print(tw, col)

#Categorical variable languages and sources
print("Unique counts for categorical columns:")
unique_lang = tw.select(pl.col('lang').n_unique()).item()
unique_source = tw.select(pl.col('source').n_unique()).item()
print(f"Unique languages: {unique_lang}")
print(f"Unique sources: {unique_source}")


#Top 3 Most Common Languages
top_langs = tw.select("lang").to_pandas()["lang"].value_counts().head(3)
print("\nTop 3 most common languages:")
print(top_langs)

#Top 3 Most Common Sources
top_sources = tw.select("source").to_pandas()["source"].value_counts().head(3)
print("\nTop 3 most common sources:")
print(top_sources)
