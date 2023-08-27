import streamlit as st
import pandas as pd
import pickle

st.title('Movie Recommender System')

def recommend(movie):
    movie_index = movies[movies['title_x']==movie].index[0]
    #finding cosine distance of the given movie from other moives
    distances = similarity[movie_index]
    #sorted movie list according to the similarity
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title_x)
    return recommended_movies
    
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
'Name the movie you liked',
movies['title_x'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
