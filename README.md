# 2024 U.S. Presidential Election Social Media Analysis

A descriptive statistical analysis of social media activity related to the 2024 U.S. Presidential Election is presented in this project. Three sizable datasets that record Facebook ads, Facebook posts, and Twitter posts are the main focus of the investigation.

The objective is to provide an overview of political communication's scale, structure, and behavioral tendencies by:
1.  Summaries of statistics (mean, standard deviation, minimum)
2.  Analysis of categorical frequency
3.  grouped analysis of categorical variables
4.  Simple visual aids for spotting patterns, skews, and outliers

Three tools are used for all work: Polars, Pandas, and Pure Python (no additional libraries).

## Dataset Overview

The datasets are private and were made available as part of a research project.

**To obtain the information:**

1. Visit the following URL: https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing

2. Extract the CSV files after downloading the ZIP file.

3. Read the files before running the code.



**Files included:**

 `2024_fb_ads_president_scored_anon.csv`
 - Ad-level data including metrics such as estimated_spend, estimated_audience_size and estimated_impressions.
 
 `2024_tw_posts_president_scored_anon.csv`     
 - Post-level data of twitter, the file includes metrics like the views, likes, retweets and replies of every single tweet.
 
 `2024_fb_posts_president_scored_anon.csv`     
 - Post-level data of facebook, the file includes data such as likes, engagement, post type and so on of each and every post made related to the elections.
 
---

## Requirements

Install dependencies (Python 3.8+):

pip install pandas, polars, matplotlib, seaborn, pyarrow


## Instructions to run the code

Any Python IDE or Jupyter Notebook can be used to run the code.

This repository contains visualization.py, README.md and .gitignore.

Additionally, there are 3 folders containing 3 files each corresponding to the dataset and the ways they were implemented, the folder structure present in the repository is as follows:

pure_python (folder)
    1. pure_python_stats_fb_ads.py
    2. pure_python_stats_fb_posts.py
    3. pure_python_stats_tw_posts.py

pandas (folder)
    1. pandas_stats_fb_ads.py
    2. pandas_stats_fb_posts.py
    3. pandas_stats_tw_posts.py
    
polars (folder)
    1. polars_stats_fb_ads.py
    2. polars_stats_fb_posts.py
    3. polars_stats_tw_posts.py


### 1. pure_python

Open the .py files in this directory.
Run the script and use the built-in `csv`, `statistics`, and `collections` modules to create descriptive statistics.
The following are among the outputs: 
1. Count, Mean, Min, Max, and Std Dev for numeric columns
2. For categorical columns, the highest frequencies and unique counts
3. Aggregations for ads by `page_id` and `(page_id, ad_id)`


### 2. pandas

Open the .py files in this directory.
Execute the script to compute, functions include:
1. '.describe()' for numeric columns
2. '.value_counts()' for categorical columns
3. '.groupby()' for summaries


### 3. polars

Launch the .py files in this directory.
Then, use the Polars library to quickly and effectively do the same descriptive and group-level analysis.

## Key Findings

### Facebook Ads

- **Volume & Activity:**
  - **Total Ads Analyzed:** 246,745
  - **Unique Advertisers (Pages):** 4,475
- **Spend Insights:**
  - **Average Spend per Ad:**  USD 1,061
  - **Total Spend:** USD 261.8 million  
  - **Max Spend:** USD 475,000 
- **Reach & Exposure:**
  - **Average Audience Size per Ad:** 557,772
  - **Average Impressions per Ad:** 45,601
- **Strategic Behavior Observed:**
  - **Over 90K ads** are seen on a select few pages (top 3), indicating the usage of **micro-targeting** techniques for a limited demographic or geographic reach.
  - The distribution of spending is **very skewed**, with certain advertisements fetching astronomically large budgets.
  
  
 **Actionable Insight:**
More research should be directed toward the **top 1% of advertisers**. Their tactics could resemble organized influence efforts or campaigns for politics
  
  

### Twitter Posts

- **Engagement Summary:**
  - **Total Likes:** 188.7 million | **Average Likes per Tweet:** 6,914
  - **Total Retweets:** 36.1 million | **Replies:** 29 million
  - **Average Views per Tweet:** 507,085
- **Device/Source Analysis:**
  - **Top Platforms:** 
    - Twitter Web App (14.9K tweets)
    - iPhone (8.5K tweets)
    - Sprout Social (2.9K tweets)
  - Tweets posted through **Sprout Social** and **TweetDeck Web App** had the most engagement**, demonstrating **agency-level content scheduling**.
  

**Actionable Insight:** 
There is a consistent increase in interaction for content generated using **agency tools**. Think about using these sites to demonstrate organizational behavior or virality on Twitter.



### Facebook Posts

- **Interaction Totals:**
  - **Total Likes:** 45.2M | **Avg per Post:** 2,378
  - **Comments:** 17.1M | **Shares:** 6.1M | **Total Interactions:** 31.8M
- **Top Performing Categories:**
  - **Page Category:** 
    - *Political Candidates* (Avg Likes: 11,402)
    - *Politicians* (Avg Likes: 2,538)
  - **Post Type:**
    - *Live Video* (Avg Comments: 6,581; Shares: 1,717)
    - *Photo* (High engagement across all metrics)
- The range of likes, which is **0 to 351,979**, shows that **some postings become viral** while others get little attention. This suggests that engagement is **skewed.

**Actionable Insight:** 
Posts with **visual content** tend to receive a lot more interaction, particularly *live videos* and *photos*. For the analysis of campaign impact, focus on these formats.


## Summary of Visualizations

Using `matplotlib` and `seaborn`, descriptive visualizations were produced for each of the three datasets:

- **Histograms** for distribution of numeric fields (ads spends, ads impressions)
- **Bar Charts** for engagement grouped by:
  - *Source* (Twitter) 
  - *Post Type* (Facebook Posts) 
  - *Page Category* (Facebook Posts)
- **Boxplots** to investigate the range of user involvement and outliers(Twitter)

