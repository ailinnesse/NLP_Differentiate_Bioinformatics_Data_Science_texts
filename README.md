# Project 3: Differentiate Reddit Bioinformatics and Data Science Subreddits



### Problem statement:

Create a model to differentiate Bioinformatics from Data Science-related articles to help Bioinformaticians find more relevant sources of information. I will focus on differentiating Reddit Bioinformatics and Data Science subreddits in this project. My baseline is 67%. I have imbalanced classes and will use F1 as my primary metric and accuracy score as a secondary to find the best classification model.

---

### Dataset

* [`reddit.csv`](./data/reddit.csv): PushShift Reddit collected for two subreddits Bioinformatics and Data Science ([source](https://api.pushshift.io/reddit/search/submission))


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

 - 01_Data_Mining - In this notebook, I collected the data from Bioinformatics and Data Science Subreddits.
 - 02_EDA_and_Cleaning -  I explored and cleaned the data. 
 - 03_Naive Bayes Model - Naive Bayes models with Count Vectorize, Tfidf Vectorizer, and different custom tokenizers.
 - 04_Boosting Models - XGBoost and Gradient Boosting models with Count Vectorize, Tfidf Vectorizer, and different custom tokenizers
 - 05_Stacking Models - Stacking Models with best Naive Bayes, XGBoost, Gradient Boosting models, and Ada Boost and best-performing custom tokenizer.
 
---

### Summary of Analysis

PushShift has data from Reddit, I have collected the data from two subreddits Bioinformatics and Data Science. The limit was the number of posts available for bioinformatics - 683.

I have mapped Bioinformatics as 1 and Data Science as 0 for modeling

EDA revealed that Data Science Post Body Text has a substantial amount of missing data.

![Title and Post Body Counts For Each Subreddit](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_post_body_counts.jpeg)

Word counts showed that the most common words for both subreddits are the names of the subreddits. 
I deleted the prevailing words (data, science, ds, bioinformatics) to find the underlying difference between subreddits texts.


![Title Most Common Words](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_most_common_words.jpeg)
In the title, the most common words are different, with only ‘help’ present in both subreddits.



For Biotechnology, the number of bigrams repeats is very low, less than 5 even for some of the top 10.
![Title Most Common Bigrams](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/title_common_bigrams.jpeg)

For Post Body text almost all the most common bigrams were parts of the links. I removed links and other code and HTML chunks using a custom build function utilizing Regex.

I combined both text columns into one - 'all text' to use it for modeling.
The most common words for it are very similar. Form 10 most common words 6 are the same for both models.

![All Text Most Common Words](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/all_most_common_words.jpeg)


Finished EDA and cleaning I moved to models.

First I used the Naive Bayes model with only Title, the resulting scores were a bit low. I have tried Tdidf Vectorizer instead of Count Vectorizer but the scores went even lower.

I decided to try and fit the model on all text and it elevated the scores.
To further improve my model I used three different Tokenizers - NLTP Word Tokenizer with Stemming, NLTP Word Tokenizer with Lemmatizing, and Text Blob Tokenizer with Stemming.

Text Blob tokenizer improved the scores and reduced overfitting.
I used Random Search to find better hyperparameters for the model with Text Blob Tokenizer, however, the scores went down.

My best Naive Bayes uses Count Vectorizer and Text Blob Tokenizing with Stemming fitted on both Title and Body Texts.
![Naive Bayes Best Model Residuals of Predictions](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/nb_residuals.jpeg)    

Then I moved to Boosting models. I explored XGBoost, Gradient Boosting, and Ada Boost models. Fitted the first two using Count Vectoriser and Tfidf Vectoriser, as with the Naive Bayes model Count Vectoriser performed better. For Ada Boost I used only Count Vectorizer.
The Gradient Boosting model had higher scores than XGBoost and Ada Boost, but lower, than Naive Bayes.

To further improve my model I used three different Tokenizers - NLTP Word Tokenizer with Stemming, NLTP Word Tokenizer with Lemmatizing, and Text Blob Tokenizer with Stemming.

Text Blob tokenizer improved the scores and reduced overfitting for XGBoost and Ada Boost.
For the Gradient Boosting model NLTP Word Tokenizer with Stemming performed better. 

My best-Boosting model is Gradient Boosting with Count Vectorizer and NLTP Word Tokenizer with Stemming fitted on both Title and Body Texts.
![Gradient Boosting Best Model Residuals of Predictions](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/gb_residuals.jpeg) 


For Stacking, I used Count Vectorizer, as it performed better for all models.
I chose the three best models from Naive Bayes, XGBoost, and Gradient Boosting and their hyperparameters from previous notebooks.

Then I added the Ada Boost model, however, the scores went down.
I decided to swap XGBoost and Ada Boost as they had almost the same scores, but the scores went even lower.

The Stacking model with Naive Bayes, XGBoost, and Gradient Boosting had higher scores, I used its hyperparameters for Tokenized models.

I chose two best-performing Tokenizers - NLTP Word Tokenizer with Stemming (worked better for Gradient Boosting) and Text Blob Tokenizer with Stemming (worked better for Naive Bayes and XGBoost).

Text Blob Tokenizer further improved the scores of the model.

My best model for this project is Stacking with Count Vectorizer and NLTP Word Tokenizer with Stemming fitted on both Title and Body Texts.
![Stacking Best Model Residuals of Predictions](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/st_residuals.jpeg) 

---

### Conclusions


My best model for this project is Stacking with Naive Bayes, Gradient Boosting, and XGBoost with Count vectorization and Text Blob Tokenizing and Stemming. It has a high F1 score of 0.85 and a test accuracy of 91%, which is a great improvement from my baseline model with 67%. My model still has predicted 48 texts wrong, mostly assigning Data Science to Bioinformatics texts.
I would recommend training my best model with a broader specter of data from different websites and using more Bioinformatics data to battle imbalanced errors in predictions for further development of the model to differentiate Bioinformatics texts from Data Science texts. Stacking brought only moderate improvement to the Naive Bayes model, I would consider time constraints, as Naive Bayes by itself fits much faster and for the huge amount of data it might be crucial to reduce time, in that case, I would recommend Naive Bayes Text Blob Tokenizer and Stemmer.




