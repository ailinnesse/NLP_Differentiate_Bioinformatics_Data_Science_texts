# Project 3: Differentiate Reddit Biotech and Bioinformatics Subreddits



### Problem statement:

Training the model to deffirintiate the biotech and bioinformatics related articles. In this project I will focus on deffirintiating Reddit Biotech and Bioinformatics subreddits. My base line is 55%. I have balanced classes and will use accuracy as my mane metric and F1 score as helper to find the best model.


---

### Dataset

* [`reddit.csv`](./data/reddit.csv): PushShift Reddit collectred fot two subredits Biotech and Bioinformatics ([source](https://api.pushshift.io/reddit/search/submission))


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

 - 01_Data_Mining - In this notebook, I collected the data from Biotech and Bioinformatics Subredits
 - 02_EDA_and_Cleaning -  I explored and cleaned the data. 
 - 02_Visualisations - Visualize relationships between the Gradient of the land, Garage Area, and Sale Price. Checking Sale Price correlation with features and between each other.
 - 03_Preprocessing_and_Feature_Engineering - Log scale Sale price, process features for modeling 
 - 04_Model_Gradient - Several different models to investigate the relationship between the Sale Price and the Gradient of the land.
 - 05_Model_Garage_Area - Models to predict House Prices depending on the Garage Size.
 - 06_Kaggle_Models - Models for Kaggle competition.

---

### Summary of Analysis

PushShift has data from Readdit, I have collected almost equal ammount of data from two subreddits biotech and bioinformatics. The limit was the number of posts avaliable for bioinformatics - 650.

I have mapped bioinformatics as 0 and biotech as 1 for modeling

![Distribution os Sale Price](https://git.generalassemb.ly/ailinnesse/project-2/blob/main/images/Sale_Price_distribution.jpeg)


Build and evaluated the models to find the influence of Gradient and Garage Area on the price of the house.


Gradient Model:
- Model with only Gradient data as features.
This model did not predict any variation in Sale Price (𝑅2 is only 0.2%)
- Better predictive model and check the influence of adding Gradient data to it and coefficient for the gradient.
The model predicts that the houses with a gradient are 0.1% more expensive than the houses without a gradient.

![Compare_Predictions_Gradient](https://git.generalassemb.ly/ailinnesse/project-2/blob/main/images/Compare_Predictions_Gradient.jpeg)

- Split the data into houses on gradient and houses on flat land and compare model predictions.
Almost no difference in predictions in model fitted on gradient data and fitted on flat data


Garage Area Model:
- Model with only Garage Area as a feature to get graphs of the relationship.

![Residuals_vs_Predictions_Garage](https://git.generalassemb.ly/ailinnesse/project-2/blob/main/images/Residuals_vs_Predictions_Garage.jpeg)

The Residuals plot does not show any clear relationship. However, the model described only 46% of Sale Price variation.

![Garage_Area_and_Sale_Price_Predictions](https://git.generalassemb.ly/ailinnesse/project-2/blob/main/images/Garage_Area_and_Sale_Price_Predictions.jpeg)

The variability of the data is high, however, the model looks good in capturing the trend.
- Model with other features to get a better prediction of the influence of the Garage Area on the House Price.
This model predicted that for each square foot increase in Garage Area the Sale Price will increase by 0.03%
---

### Conclusions

My models could not find any significant influence of the gradient of the land on the sale price. The garage area influences the price of the house, with every extra square foot of the Garage Area the house price increases by 0.03%. 
I recommend buying the land with a gradient if the reduction in the price of the land compared with a flat one will cover the additional cost of building on the gradient land and finding the balance between the cost of building a garage and its influence on the sale price of the house.




