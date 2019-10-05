import pandas as pd                                                          
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import webbrowser
from sklearn.metrics.pairwise import cosine_similarity
import sys
# def main():
df = pd.read_csv("movie_dataset.csv")

features = ['keywords','cast','genres','director']
for feature in features:
    df[feature] = df[feature].fillna('') 

def combine_features(row):
    return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]

df["combined_features"] = df.apply(combine_features,axis=1)

count_matrix = CountVectorizer().fit_transform(df["combined_features"])
# print(count_matrix)
cosine_sim = cosine_similarity(count_matrix)

cosine_sim.shape

def get_title_from_index(index):
  return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
  return df[df.title == title]["index"].values[0]

movie_user_likes = input()

movie_index = get_index_from_title(movie_user_likes)

similar_movies =  list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

i=0
for element in sorted_similar_movies:
    i=i+1
    if i>=5:
        break
lst=[]
movieUrls=[]
i=0
for i in range( len(sorted_similar_movies)):
  print(get_title_from_index(sorted_similar_movies[i][0]))
  # lst.append(get_title_from_index(sorted_similar_movies[i][0]))
  movieUrls.append(' https://sokt.io/7sDGbgUsxvb1H4pdg19p/personal-tech?Movie_Name='+ get_title_from_index(sorted_similar_movies[i][0]))    
  i=i+1
  if i>=5:

    break
  # return lst
  # return lst
for Urls in movieUrls:
    tech = webbrowser.open(Urls)

# if __name__=="__main__":
  # return main()