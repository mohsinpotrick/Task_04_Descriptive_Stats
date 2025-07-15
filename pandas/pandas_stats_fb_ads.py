#!/usr/bin/env python
# coding: utf-8

# ## Facebook Ads Analysis

# In[2]:


import pandas as pd

#Load CSV into a DataFrame
ads = pd.read_csv('./2024_fb_ads_president_scored_anon.csv')

# Convert 'estimated_spend' and 'estimated_impressions' directly
ads['estimated_spend'] = pd.to_numeric(ads['estimated_spend'], errors='coerce')
ads['estimated_impressions'] = pd.to_numeric(ads['estimated_impressions'], errors='coerce')

audience_clean = (
    ads['estimated_audience_size']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.strip()
)

#Converting to float and keep only positive values
ads['estimated_audience_size'] = pd.to_numeric(audience_clean, errors='coerce')
audience_filtered = ads['estimated_audience_size'][ads['estimated_audience_size'] > 0]

#Displaying descriptive statistics
print("Descriptive statistics:\n")
print("Estimated Spend:")
print(ads['estimated_spend'].describe().round(2), "\n")

print("Estimated Impressions:")
print(ads['estimated_impressions'].describe().round(2), "\n")

print("Estimated Audience Size (only positive values):")
print(audience_filtered.describe().round(2))

#Analyzing categorical columns page_id and ad_id
print("\nPage ID counts:")
print(f"Unique page_ids: {ads['page_id'].nunique()}")
print("Top 3 most frequent page_ids:")
print(ads['page_id'].value_counts().head(3))

print("\nAd ID counts:")
print(f"Unique ad_ids: {ads['ad_id'].nunique()}")
print("Top 3 most frequent ad_ids:")
print(ads['ad_id'].value_counts().head(3))

