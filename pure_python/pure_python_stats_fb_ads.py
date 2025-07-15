#!/usr/bin/env python
# coding: utf-8

# # Facebook Ads Analysis

# In[1]:


import csv
from statistics import mean,stdev
from collections import Counter

#Load CSV
with open('./2024_fb_ads_president_scored_anon.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

#Analyzing estimated_spend
values = [float(row['estimated_spend']) for row in data if row['estimated_spend']]

print("Analyzing estimated amount spent on Ads")
print("No. of Ads:", len(values))
print("Total Amount Spent on Ads", sum(values))
print("Mean Amount Spent on Ads:", mean(values))
print("Min Amount Spent on Ads:", min(values))
print("Max Amount Spent on Ads:", max(values))
print("Std Dev Amount Spent on Ads:", stdev(values))


#Analyzing estimated_audience_size
values_ea = []

for row in data:
    val = row['estimated_audience_size']
    if val:
        try:
            clean_val = val.replace(',', '').strip()
            float_val = float(clean_val)
            if float_val > 0:
                values_ea.append(float_val)
        except ValueError:
            continue  


print("\nAnalyzing estimated audience size for the Ads")
print("Total Audience:", sum(values_ea))
print(f"Mean Audience: {mean(values_ea):.2f}")
print("Min Audience:", min(values_ea))
print("Max Audience:", max(values_ea))
print(f"Std Dev Audience: {stdev(values_ea):.2f}")


#Analysizng estimated_impressions

values_ei = [float(row['estimated_impressions']) for row in data if row['estimated_impressions']]
print("\nAnalyzing estimated impressions of the Ads")
print("Total Impressions", sum(values_ei))
print(f"Mean Impressions:{mean(values_ei):.2f}")
print("Min Impressions:", min(values_ei))
print("Max Impressions:", max(values_ei))
print("Std Dev Impressions:", stdev(values_ei))


#Categorical variable page_id
page_ids = [row['page_id'] for row in data if row['page_id']]
freq = Counter(page_ids)
print("\nCount of Unique page_ids:", len(freq))
print("Most common page_ids and no. of ads running:", freq.most_common(3))



#Categorical variable ad_id
ads_ids = [row['ad_id'] for row in data if row['ad_id']]
freq_ads = Counter(ads_ids)
print("\nCount of Unique ad_ids:", len(freq_ads))
print("Most common ad_ids:", freq_ads.most_common(3))



# ## Aggregating By page id

# In[2]:


from collections import defaultdict

#Grouping data by page_id
group_by_page = defaultdict(list)
for row in data:
    if row['page_id']:
        group_by_page[row['page_id']].append(row)

#Storing aggregated totals per page
spend_list, impr_list, aud_list = [], [], []

for rows in group_by_page.values():
    spend = sum(float(r['estimated_spend']) for r in rows if r['estimated_spend'])
    impr = sum(float(r['estimated_impressions']) for r in rows if r['estimated_impressions'])

    audience = []
    
    for row in rows:
        val = row['estimated_audience_size']
        if val:
            try:
                clean_val = val.replace(',', '').strip()
                float_val = float(clean_val)
                if float_val > 0:
                    audience.append(float_val)
            except ValueError:
                continue 
   
    if audience:
        aud = sum(audience)
        aud_list.append(aud)

    spend_list.append(spend)
    impr_list.append(impr)
    aud_list.append(aud)

print("\nAggregated by page_id")
print(f"Unique Pages: {len(group_by_page)}")

print("\nEstimated Spend")
print(f"Mean Spend per Page: {mean(spend_list):.2f}")
print(f"Min Spend per Page: {min(spend_list):.2f}")
print(f"Max Spend per Page: {max(spend_list):.2f}")
print(f"Std Dev Spend per Page: {stdev(spend_list):.2f}")

print("\nEstimated Impressions")
print(f"Mean Impressions per Page: {mean(impr_list):.2f}")
print(f"Min Impressions per Page: {min(impr_list):.2f}")
print(f"Max Impressions per Page: {max(impr_list):.2f}")
print(f"Std Dev Impressions per Page: {stdev(impr_list):.2f}")

print("\nEstimated Audience")
print(f"Mean Audience per Page: {mean(aud_list):.2f}")
print(f"Min Audience per Page: {min(aud_list):.2f}")
print(f"Max Audience per Page: {max(aud_list):.2f}")
print(f"Std Dev Audience per Page: {stdev(aud_list):.2f}")


# ## Aggregating by page_id and ad_id

# In[3]:


#Grouping data by (page_id, ad_id)
group_by_page_ad = defaultdict(list)
for row in data:
    if row['page_id'] and row['ad_id']:
        group_by_page_ad[(row['page_id'], row['ad_id'])].append(row)

#Storing aggregated totals per (page, ad)
spend_list, impr_list, aud_list = [], [], []

for rows in group_by_page_ad.values():
    spend = sum(float(r['estimated_spend']) for r in rows if r['estimated_spend'])
    impr = sum(float(r['estimated_impressions']) for r in rows if r['estimated_impressions'])
    
    audience = []
    for r in rows:
        val = r['estimated_audience_size']
        if val:
            try:
                clean_val = val.replace(',', '').strip()
                float_val = float(clean_val)
                if float_val > 0:
                    audience.append(float_val)
            except ValueError:
                continue 
   
    if audience:
        aud = sum(audience)
        aud_list.append(aud)

    spend_list.append(spend)
    impr_list.append(impr)
    aud_list.append(aud)


print("\nAggregated by (page_id, ad_id)")
print(f"Unique (Page, Ad) Pairs: {len(group_by_page_ad)}")

print("\nEstimated Spend")
print(f"Mean Spend per Pair: {mean(spend_list):.2f}")
print(f"Min Spend per Pair: {min(spend_list):.2f}")
print(f"Max Spend per Pair: {max(spend_list):.2f}")
print(f"Std Dev Spend per Pair: {stdev(spend_list):.2f}")

print("\nEstimated Impressions")
print(f"Mean Impressions per Pair: {mean(impr_list):.2f}")
print(f"Min Impressions per Pair: {min(impr_list):.2f}")
print(f"Max Impressions per Pair: {max(impr_list):.2f}")
print(f"Std Dev Impressions per Pair: {stdev(impr_list):.2f}")

print("\nEstimated Audience")
print(f"Mean Audience per Pair: {mean(aud_list):.2f}")
print(f"Min Audience per Pair: {min(aud_list):.2f}")
print(f"Max Audience per Pair: {max(aud_list):.2f}")
print(f"Std Dev Audience per Pair: {stdev(aud_list):.2f}")

