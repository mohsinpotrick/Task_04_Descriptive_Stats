#!/usr/bin/env python
# coding: utf-8

# ## Facebook Posts Analysis

# In[19]:


import csv
from statistics import mean,stdev
from collections import Counter
from collections import defaultdict


# In[20]:


with open('./2024_fb_posts_president_scored_anon.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)


def convert_to_int(val):
    try:
        return int(val)
    except:
        return None

#Analyzing Likes
likes = [convert_to_int(row['Likes']) for row in data if convert_to_int(row['Likes']) is not None]
print("\nFacebook Post Likes")
print("Total Likes:", sum(likes))
print(f"Mean Likes: {mean(likes):.2f}")
print("Min Likes:", min(likes))
print("Max Likes:", max(likes))
print(f"Std Dev Likes: {stdev(likes):.2f}")

#Analyzing Comments
comments = [convert_to_int(row['Comments']) for row in data if convert_to_int(row['Comments']) is not None]
print("\nFacebook Post Comments")
print("Total Comments:", sum(comments))
print(f"Mean Comments: {mean(comments):.2f}")
print("Min Comments:", min(comments))
print("Max Comments:", max(comments))
print(f"Std Dev Comments: {stdev(comments):.2f}")

#Analyzing Shares
shares = [convert_to_int(row['Shares']) for row in data if convert_to_int(row['Shares']) is not None]
print("\nFacebook Post Shares")
print("Total Shares:", sum(shares))
print(f"Mean Shares: {mean(shares):.2f}")
print("Min Shares:", min(shares))
print("Max Shares:", max(shares))
print(f"Std Dev Shares: {stdev(shares):.2f}")

#Analyzing Total Interactions
interactions = [convert_to_int(row['Total Interactions']) for row in data if convert_to_int(row['Total Interactions']) is not None]
print("\nTotal Interactions")
print("Total:", sum(interactions))
print(f"Mean: {mean(interactions):.2f}")
print("Min:", min(interactions))
print("Max:", max(interactions))
print(f"Std Dev: {stdev(interactions):.2f}")

#Analyzing Post Views
views = [convert_to_int(row['Post Views']) for row in data if convert_to_int(row['Post Views']) is not None]
if views:
    print("\nPost Views")
    print("Total Views:", sum(views))
    print(f"Mean Views: {mean(views):.2f}")
    print("Min Views:", min(views))
    print("Max Views:", max(views))
    print(f"Std Dev Views: {stdev(views):.2f}")

#Categorical variable Page Category
page_categories = [row['Page Category'] for row in data if row['Page Category']]
cat_counts = Counter(page_categories)
print(f"\nTotal Unique Page Categories: {len(cat_counts)}")
print("Most Common Page Categories (Top 5):")
for category, count in cat_counts.most_common(5):
    print(f"- {category}: {count} posts")

#Categorical variable Post Type
post_types = [row['Type'] for row in data if row['Type']]
type_counts = Counter(post_types)
print(f"\nTotal Unique Post Types: {len(type_counts)}")
print("Most Common Post Types (Top 5):")
for t, count in type_counts.most_common(5):
    print(f"- {t}: {count} posts")


# ## Aggregating page category for likes, comments, and shares

# In[21]:


#Convert string to int
def convert_to_int(val):
    try:
        return int(val.replace(',', '').strip())
    except:
        return None

#Group by Page Category for Likes
grouped_likes = defaultdict(list)

for row in data:
    key = row['Page Category']
    val = convert_to_int(row['Likes'])
    if key and val is not None:
        grouped_likes[key].append(val)

print("Likes Grouped by Page Category:")
for key, values in list(grouped_likes.items())[:3]:
    print(f"Category: {key} \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")

#Group by Page Category for Comments
grouped_comments = defaultdict(list)

for row in data:
    key = row['Page Category']
    val = convert_to_int(row['Comments'])
    if key and val is not None:
        grouped_comments[key].append(val)

print("\nComments Grouped by Page Category:")
for key, values in list(grouped_comments.items())[:3]:
    print(f"Category: {key} | \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")

#Group by Page Category for Shares
grouped_shares = defaultdict(list)

for row in data:
    key = row['Page Category']
    val = convert_to_int(row['Shares'])
    if key and val is not None:
        grouped_shares[key].append(val)

print("\nShares Grouped by Page Category:")
for key, values in list(grouped_shares.items())[:3]:
    print(f"Category: {key} | \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")


# In[22]:


#Group by Type for Likes
grouped_likes_type = defaultdict(list)
for row in data:
    key = row['Type']
    val = convert_to_int(row['Likes'])
    if key and val is not None:
        grouped_likes_type[key].append(val)

print("Likes Grouped by Post Type:")
for key, values in list(grouped_likes_type.items())[:3]:
    print(f"Type: {key} \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")

#Group by Type for Comments
grouped_comments_type = defaultdict(list)
for row in data:
    key = row['Type']
    val = convert_to_int(row['Comments'])
    if key and val is not None:
        grouped_comments_type[key].append(val)

print("\nComments Grouped by Post Type:")
for key, values in list(grouped_comments_type.items())[:3]:
    print(f"Type: {key} \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")

#Group by Type for Shares
grouped_shares_type = defaultdict(list)
for row in data:
    key = row['Type']
    val = convert_to_int(row['Shares'])
    if key and val is not None:
        grouped_shares_type[key].append(val)

print("\nShares Grouped by Post Type:")
for key, values in list(grouped_shares_type.items())[:3]:
    print(f"Type: {key} \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")


# In[ ]:




