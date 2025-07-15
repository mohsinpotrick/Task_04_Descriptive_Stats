#!/usr/bin/env python
# coding: utf-8

# # Twitter Posts Analysis

# In[4]:


import csv
from statistics import mean,stdev
from collections import Counter
from collections import defaultdict


# In[6]:


with open('./2024_tw_posts_president_scored_anon.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

#Analyzing number of Likes    
likes = [int(row['likeCount']) for row in data if row['likeCount'].isdigit()]

print("\nLikes on Tweets")
print("Like Count:", sum(likes))
print(f"Mean Likes: {mean(likes):.2f}")
print("Min Likes:", min(likes))
print("Max Likes:", max(likes))
print(f"Std Dev of likes: {stdev(likes):.2f}")


#Analyzing retweetCount

retweets = [int(row['retweetCount']) for row in data if row['retweetCount'].isdigit()]

print("\nRetweets on Tweets")
print("Retweet Count:", sum(retweets))
print(f"Mean Retweets: {mean(retweets):.2f}")
print("Min Retweets:", min(retweets))
print("Max Retweets:", max(retweets))
print(f"Std Dev of Retweets: {stdev(retweets):.2f}")

#Analyzing replyCount

replyCount = [int(row['replyCount']) for row in data if row['replyCount'].isdigit()]

print("\nReplies on Tweets")
print("Reply Count:", sum(replyCount))
print(f"Mean Reply Count: {mean(replyCount):.2f}")
print("Min Reply Count:", min(replyCount))
print("Max Reply Count:", max(replyCount))
print(f"Std Dev of Reply Count: {stdev(replyCount):.2f}")


#Analyzing viewCount


viewCount = [int(row['viewCount']) for row in data if row['viewCount'].isdigit()]

print("\nViews on Tweets")
print("Total Views:", sum(viewCount))
print(f"Mean viewCount: {mean(viewCount):.2f}")
print("Min viewCount:", min(viewCount))
print("Max viewCount:", max(viewCount))
print(f"Std Dev of viewCount: {stdev(viewCount):.2f}")



#Categorical variable languages

langs = [row['lang'] for row in data if row['lang']]
freq = Counter(langs)

print(f"\nTotal Unique Languages: {len(freq)}")
print("Most Common Languages (Top 3):")
for lang, count in freq.most_common(3):
    print(f"- {lang}: {count} tweets")
    


#Categorical variable source

tweet_source = [row['source'] for row in data if row['source']]
freq_source = Counter(tweet_source)

print(f"\nTotal Unique Sources: {len(freq_source)}")
print("Most Common Languages (Top 3):")
for source, count in freq_source.most_common(3):
    print(f"- {source}: {count} tweets")


# ## Aggregating source to analyze likes 

# In[7]:


grouped_by_source = defaultdict(list)
for row in data:
    key = row['source']
    val = row['likeCount']
    if val and val.isdigit():
        grouped_by_source[key].append(int(val))

print("\nGrouped by source:")
for key, values in list(grouped_by_source.items()):
    print(f"\nSource: {key} \nCount: {sum(values)} | Mean: {mean(values):.2f} | Min: {min(values)} | Max: {max(values)}")

