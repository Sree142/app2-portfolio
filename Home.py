import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Sree Thanneeru")
    content = """
    Hello, I am Sree! I am a python programmer with a specialization 
    in data science and machine learning. I have worked on multiple projects and
    love to work on more! 
    """
    st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")