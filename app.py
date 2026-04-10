import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('spotify_data clean.csv')


st.title("Spotify Data Analysis")

st.subheader("Dataset Overview")
st.write(df.head())


st.subheader("Basic Statistics")

st.write("Total Songs :" , len(df))
st.write("Unique Artists :",df['artist_name'].nunique())

top_artists = df['artist_name'].value_counts().idxmax()
st.write("Most Frequent Artist :", top_artists)

st.subheader("Artist Popularity vs Track Popularity")
fig,ax=plt.subplots()
ax.scatter(df['artist_popularity'],df['track_popularity'],alpha=0.5)
ax.set_xlabel('Artist_Popularity')
ax.set_ylabel('Track_Popularity')
st.pyplot(fig)
st.success("There is a positive correlation between artist popularity and track popularity, indicating that more popular artists tend to have more popular tracks.")    

st.subheader("Explicit vs Non-Explicit Tracks")
explicit_avg=df.groupby('explicit')['track_popularity'].mean()
st.write(explicit_avg)

st.header("Duration vs Popularity")
fig,ax2=plt.subplots()
ax2.scatter(df['track_duration_min'],df['track_popularity'],alpha=0.5)
ax2.set_xlabel('Track Duration (min)')
ax2.set_ylabel('Track Popularity')
st.pyplot(fig)
st.success("There is no strong correlation between track duration and popularity, suggesting that track length does not significantly impact its popularity."   )


st.sidebar.header("Filters")

selected_artist = st.sidebar.selectbox(
    "Select Artist",
    df['artist_name'].unique()
)

filtered_df = df[df['artist_name'] == selected_artist]

st.write("Songs by selected artist:")
st.write(filtered_df[['track_name', 'track_popularity']])