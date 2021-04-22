import pandas as pd
import cufflinks as cf
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import seaborn as sns
cf.go_offline()
nltk.download('stopwords')
nltk.download('wordnet')

README = " Deleted un used columns. Added a row at the top of csv file and gave it Date, Amount, Description columns names for the df."

def text_process(text):
    '''
    https://medium.com/@rohithramesh1991/unsupervised-text-clustering-using-natural-language-processing-nlp-1a8bc18b048d
    '''
    stemmer = WordNetLemmatizer()
    nopunc = [ char for char in text if char not in string.punctuation]
    nopunc = ''.join([i for i in nopunc if not i.isdigit()])
    nopunc = [word.lower() for word in nopunc.split() if word not in stopwords.words('english')]
    return [ stemmer.lemmatize(word) for word in nopunc]

df = pd.read_csv('Checking2.csv' , index_col='Date')
df = df[::-1] # Reverse so its in correct order, last date to most recent date.
X_Train = list(df['Description'])

# Pre processing the Text
tfidfconvert = TfidfVectorizer(analyzer=text_process).fit(X_Train)
X_Transformed = tfidfconvert.transform(X_Train)

# Creating the model
modelkmeans = KMeans(algorithm='auto' , copy_x=True , init='k-means++' , max_iter = 300 , n_clusters=28 , n_init = 100 ,  random_state=None , tol=0.0001 , verbose = 0)
modelkmeans.fit(X_Transformed)

# Reassigning the category to the dataframe
df['Category'] = modelkmeans.labels_

df.head()