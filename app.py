import streamlit as st
import pickle 


st.header("Movie Recommendation System.")

movies = pickle.load(open("Movies_model.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))


def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    d = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])
    r_movies = []
    for m in d[1:6]:
        movie_id = movies.iloc[m[0]].movie_id
        r_movies.append(movies.iloc[m[0]].title)

    return r_movies


movies_list = movies['title'].values

select_movie = st.selectbox("Type or Select Movie from dropdown",movies_list)


if st.button("Recommend"):
    movies_r = recommend(select_movie)
    for m  in movies_r:
        st.text(m)


footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="/" target="_blank">The Sky </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
