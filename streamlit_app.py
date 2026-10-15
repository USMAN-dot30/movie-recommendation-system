import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Welcome! The app is running successfully.")

movie = st.text_input("Enter a movie name")

if movie:
    st.success(f"You selected: {movie}")
