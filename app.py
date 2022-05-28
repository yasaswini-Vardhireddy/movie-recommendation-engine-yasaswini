#<<--importing libraries which are neede-->

import streamlit as st
import pandas as pd
import pickle
import requests


#<--Function to fetch poster from movie_id-->

def fetch_poster(movie_id):
    def get_name(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        return poster_path
        
    full_path = "https://image.tmdb.org/t/p/w500/"+get_name(movie_id)
    return full_path


#<--function to recommend movies with posters-->

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:17]:
        
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


#<--Header and selectbox to select movie from which our app is going to recommend movies similar to it-->

st.header('🎬MOVIE RECOMMENDATION ENGINE🎬')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    key="na_upper"
)

#<--Displaying recommended movies after clicking the button show recommendation-->

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    
    
    #first row of recommended movies
    
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])  
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        
        
    #second row of recommended movies
    
    col5, col6, col7, col8= st.columns(4)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
        
        
    #third row of recommended movies
    
    col9, col10, col11, col12= st.columns(4)
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])

    with col11:
        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col12:
        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
        
    
    #forth row of recommended movies
    
    col13, col14, col15, col16= st.columns(4)
    with col13:
        st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
    with col14:
        st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])

    with col15:
        st.text(recommended_movie_names[14])
        st.image(recommended_movie_posters[14])
    with col16:
        st.text(recommended_movie_names[15])
        st.image(recommended_movie_posters[15])
        
   

# Displaying Trending movies all over world
        
    st.subheader('TRENDING MOVIES')
    col17, col18, col19,col20 = st.columns(4)
    with col17: 
        st.text("Docter Strange in the Multiuniverse of Madness")
        st.image("https://m.media-amazon.com/images/M/MV5BNWM0ZGJlMzMtZmYwMi00NzI3LTgzMzMtNjMzNjliNDRmZmFlXkEyXkFqcGdeQXVyMTM1MTE1NDMx._V1_FMjpg_UX1000_.jpg")
    with col18:
        st.text("Top Gun: Maverick")
        st.image("https://upload.wikimedia.org/wikipedia/en/1/13/Top_Gun_Maverick_Poster.jpg")
    
    with col19:
         st.text("The Northman")
         st.image("https://m.media-amazon.com/images/M/MV5BMzVlMmY2NTctODgwOC00NDMzLWEzMWYtM2RiYmIyNTNhMTI0XkEyXkFqcGdeQXVyNTAzNzgwNTg@._V1_.jpg")
    
    with col20:
         st.text("Everything Everywhere all at once")
         st.image("https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyMTgtYzk5Y2M3ZDVmMDk1XkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_FMjpg_UX1000_.jpg")
    
    
# Displaying Trending movies in india

    st.subheader('TRENDING MOVIES IN INDIA')
    col17, col18, col19,col20 = st.columns(4)
    with col17: 
        st.text("KGF Chapter 2")
        st.image("https://m.media-amazon.com/images/M/MV5BMjMwMDgyOGQtMWZjNC00MDUwLTllZDYtZWM3NDBmN2YzNGZmXkEyXkFqcGdeQXVyMTQzNjkzMzEw._V1_.jpg")
    with col18:
        st.text("RRR")
        st.image("https://upload.wikimedia.org/wikipedia/en/7/7b/RRR_Album.jpeg")
    with col19:
         st.text("Gangubhai Kathiawadi")
         st.image("https://cdn.99images.com/photos/movies-tv/gangubai-kathiawadi/gangubai-kathiawadi-movie-latest-hd-photos-posters-wallpapers-download-sxa7.jpg")
    with col20:
         st.text("The Kashmir Files")
         st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/The_Kashmir_Files_poster.jpg/220px-The_Kashmir_Files_poster.jpg")
    #<--Note of thanks--> 
    
    st.info("          😃 Thank u for visiting movie recommandation engine 😃  ") 
    st.info("           📑For more information about above recommended movies check sidebar 📑")   
         
                 
#<--SIDEBAR-->

st.sidebar.header(" 🎥 MORE INFORMATION 🎥 ")
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.sidebar.info(" Wanted to know more information like tagline, overview, runtime, budget and revenue, release date, genre, production companies and more about particular movie that are recommended on Home page ")
movie_list1 = movies['title'].values
slider_selectbox = st.sidebar.selectbox(
    "Please Select the movie from below and please click on know more ",
    movie_list1,
    key="na_lower"
)


#<--fetching all the details needed to display information about the selected movie on slider-->
 
#fetching movie_id from movie name
id_=movies[movies['title']==slider_selectbox]
index =id_.index[0]
id=id_.movie_id[index]

#fetching movie_poster from movie_id
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
recommended_movie_posters = []
recommended_movie_posters.append(fetch_poster(id))

#fetching  tagline from movie_id
def fetch_tagline(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     tagline=data['tagline']
     return tagline

#fetching overview from movie_id
def fetch_overview(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     overview = data['overview']
     return overview
 
#fetching runtime from movie_id
def fetch_runtime(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     runtime = data['runtime']
     return runtime
 
#fetch budget and revenue from movie_id
def fetch_budget(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     budget = data['budget']
     revenue=data['revenue']
     return budget,revenue
 
#fetch release date from movie_id
def fetch_release_date(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     date=data['release_date']
     return date

#fetching genres from movie_id
def fetch_genre(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    genre = data['genres']
    return genre
genres=[]
x=len(fetch_genre(id))
for i in range (0,x):
 genres.append(fetch_genre(id)[i]['name'])
 
#fetch production campanies from movie_id
def fetch_production_companies(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    campanies = data['production_companies']
    return campanies
production_companies=[]
x=len(fetch_production_companies(id))
for i in range (0,x):
 production_companies.append(fetch_production_companies(id)[i]['name'])
  
#fetching homepage from movie_id
 def fetch_homepage(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=619556e14be3ada179f80811e3fbd0cd&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     homepage=data['homepage']
     return homepage
   

#<--Displaying information about the selected movie on slider-->

if st.sidebar.button('know more'):
    st.image(recommended_movie_posters[0])
    
    st.subheader("MOVIE NAME")
    st.error(slider_selectbox)
    
    st.subheader("MOVIE TAGLINE")
    st.error(fetch_tagline(id))
    
    st.subheader("OVERVIEW ")
    st.error(fetch_overview(id))
    
    st.subheader("RUNTIME")
    st.error(fetch_runtime(id))
    st.write("(In Minutes)")
    
    st.subheader("BUDGET AND REVENUE")
    st.error(fetch_budget(id))
    st.write("(In Rupees)")
    
    st.subheader("RELEASE DATE")
    st.error(fetch_release_date(id))
    
    st.subheader("GENRE")
    st.error(genres)
    
    st.subheader("PRODUCTION COMPANIES")
    st.error(production_companies)
    
    st.subheader("HOMEPAGE")
    st.error("Follow the link to get more details like Cast, Crew, Movie streaming platform ,Vedios, Movie gallery ,Music and explore more about the movie")
    st.write(fetch_homepage(id))
    
    

        
  
     
    
 
         
        
       