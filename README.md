# Project 3: Differentiate Reddit Bioinformatics and Data Science Subreddits



### Problem statement:

Create a model to differentiate the Bioinformatics and Data Science-related articles to help bioinformaticians find more relevant sources of information. I will focus on differentiating Reddit Bioinformatics and Data Science subreddits in this project. My baseline is 67%. I have imbalanced classes and will use F1 as my primary metric and accuracy score as a secondary to find the best classification model.

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
 - 03_Naive Bayes Model - Naive Bayes models with Count Vectorize, Tfidf Vectorizer and differnt custom tokenizers.
 - 04_Boosting Models - XGBoost and Gradient Boosting models with Count Vectorize, Tfidf Vectorizer and differnt custom tokenizers
 - 05_Stacking Models - Stacking Models with best Naive Bayes, XGBoost and Gradient Boosting models and best performing custom tokenizer.
 
---

### Summary of Analysis

PushShift has data from Readdit, I have collected the data from two subreddits Bioinformatics and Data Science. The limit was the number of posts avaliable for bioinformatics - 683.

I have mapped Bioinformatics as 1 and Data Science as 0 for modeling

During EDA I I found that Data Science Post Body Text has substantial amount of missing data.

![Title and Post Body Counts For Each Subreddit](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_post_body_counts.jpeg)

Word counts showed that the most common words for both subreddits are the names of the subreddits. 
I deleted the prevaling words (data, science, ds, bioinformatics) to find the underling difference between subreddits texts.


![Title Most Common Words](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_most_common_words.jpeg)
In the title the most common words are different, with only help precent in both subreddits.



For Biotechnology the number of bigrams repeats is very low, less than 5 even for some of the top 10.
![Title Most Common Bigrams](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_common_bigrams.jpeg)

For Post Body text almost all most common bigrams were parts of the links. I removed links and other code and html chunks using custom build function utilizing Regex.

I combined both text columns to one - 'all text' to use it for modeling.
The most common words for it are very similar. Form 10 most common words 6 are the same for both models.

??? change!!
![Title Most Common Bigrams](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_common_bigrams.jpeg)

??? change!!!










---

### Conclusions


My best model for this project is Stacking with Naive Bayes, Gradient Boosting, and XGBoost with Count vectorization and without tokenizing. It has a high F1 score of 0.846 and a test accuracy of 90%. The model with tokenization has about the same scores (0.005 lower F1 score) and it takes considerably more time to fit and score. 
I would recommend training my best model with a broader specter of data from different websites and using more Bioinformatics data to battle imbalanced errors in predictions for further development of the model to differentiate Bioinformatics texts from Data Science texts.







