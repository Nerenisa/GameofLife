# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os

try:
	os.chdir(os.path.join(os.getcwd(), '..'))
	print(os.getcwd())
except:
	pass

from IPython import get_ipython



import pandas as pd

# Read datasets/papers.csv into papers
lens = pd.read_csv('datasets/lens_transportation_14-19.csv',sep=';', )

# Print out the first rows of papers
lens.head(3)



# Remove the columns
#lens.drop(['ISSNs'],axis=1,inplace=True)
#lens.drop(['Publisher'],axis=1,inplace=True)
#lens.drop(['Source URLs'],axis=1,inplace=True)
#lens.drop(['Patent Citation Count'],axis=1,inplace=True)
#lens.drop(['PMID'],axis=1,inplace=True)
#lens.drop(['DOI'],axis=1,inplace=True)
#lens.drop(['Microsoft Academic ID'],axis=1,inplace=True)
#lens.drop(['References'],axis=1,inplace=True)
#lens.drop(['title'],axis=1,inplace=True)
#lens.drop(['fields of study'],axis=1,inplace=True)

#lens.drop(['Volume'],axis=1,inplace=True)
#lens.drop(['MeSH Terms'],axis=1,inplace=True)
#lens.drop(['Chemicals'],axis=1,inplace=True)
#lens.drop(['PMCID'],axis=1,inplace=True)

#lens.drop(['Keywords'],axis=1,inplace=True)
#lens.drop(['Funding'],axis=1,inplace=True)
#lens.drop(['Issue Number'],axis=1,inplace=True)
#lens.drop(['Start Page'],axis=1,inplace=True)
#lens.drop(['End Page'],axis=1,inplace=True)



# Print out the first rows of papers
#lens.head(3)


# Group the papers by year
groups = lens.groupby(['Publication Year'])

# Determine the size of each group
counts = groups.size()

# Visualise the counts as a bar plot
import matplotlib.pyplot
get_ipython().run_line_magic('matplotlib', 'inline')
counts.plot(kind ="bar")


# Load the regular expression library
import re

# Print the titles of the first rows 
print(lens['Title'].head())

# Remove punctuation
lens['title_processed'] = lens['Title'].map(lambda x: re.sub(r'[,\.!?:]', '', str(x)))

# Convert the titles to lowercase
lens = lens.apply(lambda x: x.astype(str).str.lower())

# Print the processed titles of the first rows 
print(lens['title_processed'].head())


# Import the wordcloud library
import wordcloud
#from wordcloud import WordCloud
#import WordCloud

# Join the different processed titles together.
long_string = ' '.join(lens['title_processed'])  # - new!!

# Create a WordCloud object
wordcloud = wordcloud.WordCloud()
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image()


#%%
# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Helper function
def plot_30_most_common_words(count_data, count_vectorizer):
    import matplotlib.pyplot as plt
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts+=t.toarray()[0]
    
    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x:x[1], reverse=True)[0:30]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words)) 

    plt.bar(x_pos, counts,align='center')
    plt.xticks(x_pos, words, rotation=90) 
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.title('30 most common words')
    plt.show()

# Initialise the count vectorizer with the English stop words
count_vectorizer = CountVectorizer(stop_words='english')
#from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as esw
#count_vectorizer = ["fig", "figure", "et", "al", "table",  
        #"data", "analysis", "analyze", "study",  
        #"method", "result", "conclusion", "author",  
        #"find", "found", "show", "perform",  
        #"demonstrate", "evaluate", "discuss", "google", "scholar",   
        #"pubmed",  "web", "science", "crossref", "supplementary"] + list(esw) 
# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(lens['title_processed'])

# Visualise the 30 most common words

print(count_vectorizer.get_feature_names()[:10])
print(count_vectorizer.get_feature_names()[11:20])
print(count_vectorizer.get_feature_names()[21:30])
plot_30_most_common_words (count_data, count_vectorizer)


#%%
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA
 
# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        
# Tweak the two parameters below (int values below 15)
number_topics = 20
number_words = 3

# Create and fit the LDA model
lda = LDA(n_components=number_topics)
lda.fit(count_data)

# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)


#%%



