# Project 3: Differentiate Reddit Bioinformatics and Data Science Subreddits



### Problem statement:

Create a model to differentiate the Bioinformatics from Data Science-related articles to help Bioinformaticians find more relevant sources of information. I will focus on differentiating Reddit Bioinformatics and Data Science subreddits in this project. My baseline is 67%. I have imbalanced classes and will use F1 as my primary metric and accuracy score as a secondary to find the best classification model.

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

![All Text Most Common Words](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/all_most_common_words.jpeg)


Finished EDA and cleaning I moved to modeling.

First I used Naive Bayes model with only title, the resulting scores were a bit low. I have tryed Tdidf Vectorizer instead of Count Vectorizer but the scores went even lower.

I decided to try and fit the model on all text and it elevated all scores.
To futher improve my model I used three different Tokenizers - NLTP Word Tokenizer with Stemming, NLTP Word Tokenizer with Lemmatizing, Text Blob Tokenizer with Stemming.

Text Blob tokenizer improved the scores and reduced overfitting.
I used Random Search to find better hyperparameters for model with Text Blob Tokenizer ................................................

My best Naive Bayes uses Count Vectorizer and Text Blob Tokenizing with Stemming fitted on both Title and Body Texts.
![Naive Bayes Best Model Residuals of Predictions](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/nb_residuals.jpeg)    !!! Update

Then I moved to Boosting models. I explored XGBoost and Gradient Boosting models. Fitted both using Count Vectoriser and Tfidf Vectoriser, as with Naive Bayes model Count Vectoriser performed better.
Gradient Boosting model had higher scores than XGBoost, but lower, than Naive Bayes.

To futher improve my model I used three different Tokenizers - NLTP Word Tokenizer with Stemming, NLTP Word Tokenizer with Lemmatizing, Text Blob Tokenizer with Stemming.

Text Blob tokenizer improved the scores and reduced overfitting for XGBoost.
For Gradient Boosting model NLTP Word Tokenizer with Stemming performed better. 

My best Boosting model is Gradient Boosting with Count Vectorizer and NLTP Word Tokenizer with Stemming fitted on both Title and Body Texts.
![Gradient Boosting Best Model Residuals of Predictions](https://git.generalassemb.ly/ailinnesse/project-3/blob/main/images/gb_residuals.jpeg)    !!! Update if XGBoost better ????


For Stacking I used Count Vectorizer, as it performed better for all models.
I chose three best models from Naive Bayes, XGBoost and Gradient Boosting and inputed their hyperparameters.

The Stacking model had higher scores but did not improve overfitting.

I chose two best performing Tokenizers - NLTP Word Tokenizer with Stemming (worked better for Gradient Boosting) and Text Blob Tokenizer with Stemming (worked better for all other models).
Text Blob Tokenizer further improved the scores of the model.

---

### Conclusions


My best model for this project is Stacking with Naive Bayes, Gradient Boosting, and XGBoost with Count vectorization and without tokenizing. It has a high F1 score of 0.846 and a test accuracy of 90%. The model with tokenization has about the same scores (0.005 lower F1 score) and it takes considerably more time to fit and score. 
I would recommend training my best model with a broader specter of data from different websites and using more Bioinformatics data to battle imbalanced errors in predictions for further development of the model to differentiate Bioinformatics texts from Data Science texts.







