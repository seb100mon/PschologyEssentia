import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Personality Quiz",
    page_icon="✨",
    layout="wide"
)

# --------------------------------------------------
# FUNCIÓN PARA COLOCAR GIF COMO FONDO
# --------------------------------------------------
def poner_fondo_gif(nombre_archivo):
    ruta = Path(__file__).parent / nombre_archivo
    gif = ruta.read_bytes()
    gif_base64 = base64.b64encode(gif).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.30),
                    rgba(0, 0, 0, 0.45)
                ),
                url("data:image/gif;base64,{gif_base64}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        header {{
            background: transparent !important;
        }}

        footer {{
            visibility: hidden;
        }}

        .block-container {{
            padding-top: 0rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }}

        .welcome-container {{
            height: 78vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}

        .welcome-title {{
            font-size: 64px;
            font-weight: 700;
            color: white;
            margin-bottom: 15px;
        }}

        .welcome-subtitle {{
            font-size: 22px;
            color: rgba(255,255,255,0.88);
            max-width: 700px;
            line-height: 1.5;
        }}

        div.stButton {{
            text-align: center;
        }}

        div.stButton > button {{
            background: rgba(255,255,255,0.14);
            color: white;
            border: 1px solid rgba(255,255,255,0.55);
            border-radius: 30px;
            padding: 12px 40px;
            font-size: 18px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}

        div.stButton > button:hover {{
            background: white;
            color: black;
            border: 1px solid white;
            transform: scale(1.04);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# ESTADO DE LA APP
# --------------------------------------------------
if "inicio" not in st.session_state:
    st.session_state.inicio = False


# --------------------------------------------------
# PANTALLA DE BIENVENIDA
# --------------------------------------------------
if not st.session_state.inicio:

    poner_fondo_gif("white.gif")

    st.markdown(
        """
        <div class="welcome-container">

            <div class="welcome-title">
                Personality Quiz
            </div>

            <div class="welcome-subtitle">
                Descubre más sobre tu personalidad,
                tu forma de pensar y la manera en que interactúas
                con el mundo.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Comenzar →", use_container_width=True):
        st.session_state.inicio = True
        st.rerun()


# --------------------------------------------------
# TEST
# --------------------------------------------------
else:

    st.title("Personality Quiz")

    st.write("Selecciona la opción que mejor te represente.")

    respuesta = st.radio(
        "I enjoy meeting new people.",
        [1, 2, 3, 4, 5],
        horizontal=True
    )

    st.write("Respuesta seleccionada:", respuesta)