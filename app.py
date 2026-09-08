import streamlit as st


if "inicio" not in st.session_state:
    st.session_state.inicio = False

#Start screen

if not st.session_state.inicio:

    st.title("Personality Quiz")

    st.subheader("Descubre más sobre tu personalidad")

    st.write("""
    Bienvenido/a a este test de personalidad.

    A lo largo del cuestionario encontrarás una serie de afirmaciones
    relacionadas con tu forma de pensar, actuar y relacionarte con otras personas.

    Para cada afirmación deberás indicar qué tan de acuerdo o en desacuerdo estás.
    No existen respuestas correctas o incorrectas.

    Responde de la manera más sincera posible.
    """)

    st.info("""
    Escala de respuestas:

    1 = Totalmente en desacuerdo  
    2 = En desacuerdo  
    3 = Neutral  
    4 = De acuerdo  
    5 = Totalmente de acuerdo
    """)

    if st.button("Comenzar"):
        st.session_state.inicio = True
        st.rerun()

#Prueba

else:

    st.title("Personality Quiz")

    respuesta = st.radio(
        "I enjoy meeting new people.",
        [1, 2, 3, 4, 5],
        horizontal=True
    )

    st.write("Respuesta seleccionada:", respuesta)