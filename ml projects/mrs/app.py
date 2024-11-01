import streamlit as st
import pickle
import pandas as pd
import requests

def find_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e0b88c44bf655621591fcafe0d92e077&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def suggest(movie):

    # Proceed if the movie exists
    movie_index = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similar[movie_index])), reverse=True, key=lambda x: x[1])

    suggested_movies = []
    suggested_movies_posters = []

    for i in dist[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        suggested_movies.append(movies.iloc[i[0]].title)
        #poster fetching
        suggested_movies_posters.append(find_poster(movie_id))

    return suggested_movies,suggested_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similar = pickle.load(open('similar.pkl','rb'))


st.title('Movies Recommender System')

chosen_movie = st.selectbox('Select a movie',
                      movies['title'].values)

if st.button('Suggest'):
    names,poster = suggest(chosen_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    #col6, col7, col8, col9, col10 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    # with col6:
    #     st.text(names[5])
    #     st.image(poster[5])
    #
    # with col7:
    #     st.text(names[6])
    #     st.image(poster[6])
    # with col8:
    #     st.text(names[7])
    #     st.image(poster[7])
    # with col9:
    #     st.text(names[8])
    #     st.image(poster[8])
    # with col10:
    #     st.text(names[9])
    #     st.image(poster[9])

