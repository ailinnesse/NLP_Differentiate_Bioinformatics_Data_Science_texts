# Project 3: Differentiate Reddit Bioinformatics and Data Science Subreddits



### Problem statement:

Create a model to differentiate the Bioinformatics and Data Science-related articles. I will focus on differentiating Reddit Bioinformatics and Data Science subreddits in this project. My baseline is 67%. I have imbalanced classes and will use F1 as my primary metric and accuracy score as a secondary to find the best classification model.

---

### Dataset

* [`reddit.csv`](./data/reddit.csv): PushShift Reddit collectred fot two subredits Bioinformatics and Data Science ([source](https://api.pushshift.io/reddit/search/submission))


---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|subreddit|object|reddit.csv|Name of the subreddit|
|selftext|object|reddit.csv|Text of the post|
|title|object|reddit.csv|Title of the post|
|created_utc|integer|reddit.csv|Creation time in Epoch|

---
### Notebooks overview

 - 01_Data_Mining - In this notebook, I collected the data from Bioinformatics and Data Science Subredits.
 - 02_EDA_and_Cleaning -  I explored and cleaned the data. 
 
 
 - 04_Model_Gradient - Several different models to investigate the relationship between the Sale Price and the Gradient of the land.
 - 05_Model_Garage_Area - Models to predict House Prices depending on the Garage Size.
 - 06_Kaggle_Models - Models for Kaggle competition.

---

### Summary of Analysis

PushShift has data from Readdit, I have collected the data from two subreddits Bioinformatics and Data Science. The limit was the number of posts avaliable for bioinformatics - 683.

I have mapped Bioinformatics as 1 and Data Science as 0 for modeling

During EDA I I found that Data Science Post Body Text has substantial amount of missing data.

![Title and Post Body Counts For Each Subreddit](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_post_body_counts.jpeg)

Word counts showed that the most common words for both subreddits are the names of the subreddits. 
I deleted the prevaling words (data, science, ds, bioinformatics) to find the underling difference between subreddits texts.


![Title and Post Body Counts For Each Subreddit](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_post_body_counts.jpeg)



![Title and Post Body Counts For Each Subreddit](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_post_body_counts.jpeg)

---

### Conclusions

My models could not find any significant influence of the gradient of the land on the sale price. The garage area influences the price of the house, with every extra square foot of the Garage Area the house price increases by 0.03%. 
I recommend buying the land with a gradient if the reduction in the price of the land compared with a flat one will cover the additional cost of building on the gradient land and finding the balance between the cost of building a garage and its influence on the sale price of the house.




