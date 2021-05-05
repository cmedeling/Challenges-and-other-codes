# -*- coding: utf-8 -*-
"""

This is to check the differences between 2 text files.

Created on Tue May  4 12:55:32 2021

@author: Carl-Michael
"""

# create
oldfile = open("179.001.txt", mode = "r", encoding = "utf8")
newfile = open("180.001.txt", mode = "r", encoding = "utf8")

oldlist = oldfile.read().split("\n")
newlist = newfile.read().split("\n")
#print("'old list' has {} sentences.".format(len(oldlist)))

# -----------------------------------------------------------------------------

# Drop the first line in each document


# Levenshtein Method 

# used to find number of transformations needed to make the 2 strings the same

#!pip install python-Levenshtein
import Levenshtein

#print(Levenshtein.distance("Example Txet", "Example text"))

# Cosine Similarity Method - 

import string
import nltk
#nltk.download('stopwords')          
    # stopwords examples: "I, me, myself", etc.  Removing them makes the angle between the vectors
    # smaller.  If we keep them, the angle between dimension vectors will be bigger, indicating
    # a larger level of dissimilarity.
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words("english")

# Create a function that cleans the text
def clean_string(text):
    
    """This function removes punctuation, makes text lowercase and removes stopwords"""
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords])
    
    return text

cleaned_text = list(map(clean_string, oldlist))
#print(cleaned_text)
          
# Use CountVectorizer to create k vectors in n-dimensional space
# where     k = number of sentences
# and       n = number of unique words in all combined sentences      

vectorizer = CountVectorizer().fit_transform(cleaned_text) 
vectors = vectorizer.toarray()
#print(vectors)  
#print("There are {} sentences and {} unique words.".format(len(vectors), len(vectors[0]))) 

# Use cosine similarity to create a matrix that checks the similarity 
# of each sentence to every other sentence
cos_sim = cosine_similarity(vectors)
#print(cos_sim)
#print("The 'cosine-similarity' checks the similarity of each to every row.")

# Define a function to reshape the 1D input vectors 
# to the 2D array that cosine_similarity() expects

def cosine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    
    return cosine_similarity(vec1, vec2)[0][0]

#print("The cosine similarity between sentences 1 and 1 is {}.".format(cosine_sim_vectors(vectors[0], vectors[0])))

# Now we have 2 ways of comparing 2 text documents.

"""
The Levenshtein Method counts the number of changes required to make 1 sentence the same as another.
This can be used by:
    first, count the total number of characters in the document
    second, use the Levenstein Method to count the number of changes difference.
    third, calculate the dissimilarity:
        ie. ((Number of changes)/(Total number of characters))*100
            gives a percentage difference

The Cosine Similarity Method creates 2 matrices:
    the first, "vectors", with:
        rows = number of sentences
        columns = number of unique words in all sentences
    the second, "cos_sim" with:
        rows = sentences in document 1
        columns = sentences in document 2
    The main diagonal on the second matrix should all be 1's if the sentences are the same. 
"""
# -----------------------------------------------------------------------------
# Levenshtein Method:
    
Lev_Score = []
for i in range(len(oldlist)):
    Lev_Score.append(Levenshtein.distance(oldlist[i], newlist[i]))
# PROBLEM - oldlist and newlist are NOT the same length

# -----------------------------------------------------------------------------
"""
# Cosine-Similarity Method:

# Clean the text from the 2 documents to compare

def clean_string(text):
    
    # This function removes punctuation, makes text lowercase and removes stopwords
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords])
    
    return text 

cleaned_text_old = list(map(clean_string, oldlist))
cleaned_text_new = list(map(clean_string, newlist))

# Create the matrices
    
vectorizer_old = CountVectorizer().fit_transform(cleaned_text_old)
vectorizer_new = CountVectorizer().fit_transform(cleaned_text_new) 
vectors_old = vectorizer_old.toarray()
vectors_new = vectorizer_new.toarray()

# Use cosine similarity to create a matrix that checks the similarity 
# of each sentence to every other sentence
cos_sim_score = cosine_similarity(vectors_old, vectors_new)
#print(cos_sim)

"""
# Define a function to reshape the 1D input vectors 
# to the 2D array that cosine_similarity() expects

'''def cosine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    
    return cosine_similarity(vec1, vec2)[0][0]

    cosine_sim_vectors(vec1, vec2)'''

# -----------------------------------------------------------------------------

# Create text object

oldfile1 = open("179.1-4.oneline.2.txt", mode = "r", encoding = "utf8")
newfile1 = open("180.1-4.online.2.txt", mode = "r", encoding = "utf8")

"""oldfile1 = open("179.001.txt", mode = "r", encoding = "utf8")
oldfile2 = open("179.002.txt", mode = "r", encoding = "utf8")
oldfile3 = open("179.003.txt", mode = "r", encoding = "utf8")
oldfile4 = open("179.004.txt", mode = "r", encoding = "utf8")

newfile1 = open("180.001.txt", mode = "r", encoding = "utf8")
newfile2 = open("180.002.txt", mode = "r", encoding = "utf8")
newfile3 = open("180.003.txt", mode = "r", encoding = "utf8")
newfile4 = open("180.004.txt", mode = "r", encoding = "utf8")"""

# Create readable object (All sentences joined)
oldlist1 = oldfile1.read()
newlist1 = newfile1.read()

# Create readable object (All sentences on new line)
oldlist1split = oldlist1.split("\n")
newlist1split = newlist1.split("\n")

# Remove the first lines from each file
del oldlist1split[0], newlist1split[0]

# Remove the last lines from each file
del oldlist1split[-1], newlist1split[-1]

# join the sentences into one long line
separator = "; "
olddoc = separator.join(oldlist1split)
newdoc = separator.join(newlist1split)

# count the number of characters in the olddoc and newdoc
oldlength = len(olddoc)
newlength = len(newdoc)

#Get the Levenshtein Scores
lev_score = Levenshtein.distance(olddoc, newdoc)

# What is the percentage of similarity?
print("The documents have a dissimilarity percentage of {}.".format((lev_score/max(oldlength, newlength))*100))

# -----------------------------------------------------------------------------

"""# Now that I've proven that this works, let's repeat the process for all the documents.
The process is:
    1. Remove the first and list lines of each documents
    2. Combine all the 179 documents together and all the 180 documents together
    3. 

"""




