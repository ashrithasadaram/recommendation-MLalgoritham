import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bf4e90546cb1544ae430b5785d621eae")
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])

    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movies_list[1:6]:
        movie_id=movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster


movie_dict=pickle.load(open("movie_dict.pk1","rb"))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pk1","rb"))

st.title('Movie Recommender System')

option = st.selectbox("How would you like to be contacted?",
                      movies['title'].values )

if st.button("Recommend"):
    names,posters=recommend(option)

    st.image(posters[0], caption=names[0],width=325)
    st.image(posters[1], caption=names[1],width=325)
    st.image(posters[2], caption=names[2],width=325)
    st.image(posters[3], caption=names[3],width=325)
    st.image(posters[4], caption=names[4],width=325)