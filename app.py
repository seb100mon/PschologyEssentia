import streamlit as st

st.title("Personality Quiz")

st.write("Bienvenido al test de personalidad")

respuesta = st.radio(
    "I enjoy meeting new people.",
    [1, 2, 3, 4, 5],
    horizontal=True
)

st.write("Respuesta seleccionada:", respuesta)