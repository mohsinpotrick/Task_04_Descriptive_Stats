#!/usr/bin/env python
# coding: utf-8

# # Facebook Ads Analysis

import polars as pl

#Load CSV
ads = pl.read_csv('./2024_fb_ads_president_scored_anon.csv')

#Cleaning and converting numeric columns
ads = ads.with_columns([
    pl.col('estimated_spend')
      .cast(pl.Utf8)
      .str.replace_all(',', '')
      .str.strip_chars()
      .cast(pl.Float64, strict=False),
    pl.col('estimated_impressions')
      .cast(pl.Utf8)
      .str.replace_all(',', '')
      .str.strip_chars()
      .cast(pl.Float64, strict=False),
])

ads = ads.with_columns([
    pl.col('estimated_audience_size')
      .cast(pl.Utf8)
      .str.replace_all(',', '')
      .str.strip_chars()
      .cast(pl.Float64, strict=False)
      .alias('estimated_audience_size'),
])

#Filtering only positive audience sizes
audience_filtered = ads.filter(pl.col('estimated_audience_size') > 0).select('estimated_audience_size')

#Function to describe a numeric column
def describe_column(ads, col_name):
    stats = ads.select([
        pl.col(col_name).count().alias("count"),
        pl.col(col_name).mean().alias("mean"),
        pl.col(col_name).std().alias("std"),
        pl.col(col_name).min().alias("min"),
        pl.col(col_name).max().alias("max"),
    ])
    print(f"Descriptive stats for '{col_name}':")
    print(stats.to_pandas().round(2))
    print()

#Print descriptive statistics
print("Descriptive statistics:\n")

describe_column(ads, "estimated_spend")
describe_column(ads, "estimated_impressions")
describe_column(audience_filtered, "estimated_audience_size")

#Categorical analysis for page_id and ad_id
print("\nPage ID counts:")
unique_page_ids = ads.select(pl.col('page_id').n_unique()).item()
print(f"Unique page_ids: {unique_page_ids}")
print("Top 3 most frequent page_ids:")
counts = (
    ads.select("page_id")
    .to_pandas()
    ["page_id"]
    .value_counts()
    .head(3)
)
print(counts)

print("\nAd ID counts:")
unique_ad_ids = ads.select(pl.col('ad_id').n_unique()).item()
print(f"Unique ad_ids: {unique_ad_ids}")
print("Top 3 most frequent ad_ids:")
adcounts = (
    ads.select("ad_id")
    .to_pandas()
    ["ad_id"]
    .value_counts()
    .head(3)
)
print(adcounts)

