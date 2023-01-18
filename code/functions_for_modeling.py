
import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from xgboost import XGBClassifier


def plot_residuals(model, X_test, y_test, model_name, file_name):
    '''
    Plots Residuals of the model predictions
    Input:
    Model
    X_test
    y_test
    Model Name for the plot title
    File name to save plot (without .jpeg)

    Outputs:
    Histogram of residuals
    '''
    preds = model.predict(X_test)
    resids = y_test - preds
    plt.figure(figsize = (14, 8))
    plt.hist(resids, color = 'lightseagreen');
    plt.title(f'{model_name} Residuals of Predictions (Test Data)', size = 20);
    plt.xticks([-1, 0, 1], labels = ['Incorrectly Predicted \n Bioinformatics', 'Correct Prediction', 'Incorrectly Predicted \n Data Science'], fontsize = 20)
    plt.ylabel('Count', fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.tight_layout()
    plt.savefig(f'../images/{file_name}.jpeg');


def model_fit_scores(model, X_train, y_train, X_test, y_test, best_params = True):
    '''
    Fits the model and prints the scores
    Input:
    Model
    X_train
    y_train
    X_test
    y_test
    
    Outputs:
    Prints - Cross Validation score, Best Paramenets, Train Accuracy, Test Accuracy, F1 score
    Returns - fitted model
    '''
    print(f'Cross Validation Score: {cross_val_score(model, X_train, y_train).mean()}')
    model.fit(X_train, y_train)
    if best_params:
        print(f'Best Parameters: {model.best_params_}')
    print(f'Train accuracy: {model.score(X_train, y_train)}')
    print(f'Test accuracy: {model.score(X_test, y_test)}')
    preds = model.predict(X_test)
    print(f'F1 score: {f1_score(y_test, preds)}')
    return model


# Adapted from https://git.generalassemb.ly/dsir-1128/5.03-lesson-NLP-i/blob/main/starter-code-Hank-Copy.ipynb
def tokenizer_lemmatizer(text):
    '''
    Tokenizers using NLTK library and Lemmatizers the text. Removes Stopwords using NLTK stop words list
    Input:
    Text
    
    Outputs:
    List of Tokenized and Lemmatized Words from Text
    '''
    word_token = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens_lem = [lemmatizer.lemmatize(word) for word in word_token if word not in stopwords.words('english')]
    return tokens_lem


# Adapted from https://git.generalassemb.ly/dsir-1128/5.03-lesson-NLP-i/blob/main/starter-code-Hank-Copy.ipynb
def tokenizer_stemmer(text):
    '''
    Tokenizers using NLTK library and Stems the text. Removes Stopwords using NLTK stop words list
    Input:
    Text
    
    Outputs:
    List of Tokenized and Stemmed words from the text
    '''
    word_token = word_tokenize(text) 
    p_stemmer = PorterStemmer()
    tokens_stem = [p_stemmer.stem(word) for word in word_token if word not in stopwords.words('english')]
    return tokens_stem

# Use TextBlob from (https://jonathansoma.com/lede/algorithms-2017/classes/more-text-analysis/counting-and-stemming/)
def textblob_tokenizer(str_input):
    '''
    Tokenizers using Text Blob library and Lemmatizers the text. Removes Stopwords using NLTK stop words list
    Input:
    Text
    
    Outputs:
    List of Tokenized and Stemmed words from the text
    '''
    blob = TextBlob(str_input)
    words = [token.lemmatize() for token in blob.words if token not in stopwords.words('english')]
    return words

def model_tokenazer(model, model_name, tokenizer, min_df, max_features, max_df, X_train, y_train, X_test, y_test):
    '''
    Makes Pipeline with Count Vectorizer using chosen tokenizer and Model.
    Fits the model and prints the scores.
    Input:
    Model
    Model Name for Pipe
    Tokenizer
    min_df for Count Vectorizer
    max_features for Count Vectorizer 
    max_df for Count Vectorizer
    X_train
    y_train
    X_test
    y_test
    
    Outputs:
    Prints - Cross Validation score, Train Accuracy, Test Accuracy, F1 score
    Returns - fitted model
    '''
    model = Pipeline([
    ('cvec', CountVectorizer(tokenizer=tokenizer, max_df=max_df, max_features=max_features, min_df=min_df)),
    ('model_name', model)
    ])

    return model_fit_scores(model, X_train, y_train, X_test, y_test, best_params = False)


