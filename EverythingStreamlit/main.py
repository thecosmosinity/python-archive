import streamlit as st
from time import sleep
import datetime
import streamlit_extras as se

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

download = open("assets/soundtrack.wav")

st.download_button("Download an epic file", "oh inky pinky ponky, YOU ARE A STUPID DONKEY")

st.warning("WARNING!: This site uses camera input and saves files based on user input. It's your choice.")
st.title("Welcome to Everything Streamlit!")

left, right = st.columns(2)
with left:
    st.subheader(":wave: Hi!")
    st.write("Wanna check out the source code? Go to- https://github.com/thecosmosinity/python-archive and go to "
             "EverythingStreamlit")
    st.audio("assets\soundtrack.wav")
    st.caption("Audio!")
    with right:
        st.image("assets\image.png")
        st.caption("Epic Picture.")

with st.container():
    l, r = st.columns(2)
    with l:
        checkbox = st.checkbox("This is a checkbox. If you click. Your camera will turn on. Nothing will be saved.")

        if checkbox:
            with r:
                st.camera_input("You...")
        else:
            var = None

with st.container():
    st.file_uploader("Upload something here! (it won't save...)")

    st.video("assets/veedio.mp4")

with st.container():

    l, m, r = st.columns(3)

    with m:
        st.data_editor(df)


