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
def poner_fondo_gif(archivo):
    gif = Path(archivo).read_bytes()
    gif_base64 = base64.b64encode(gif).decode()

    st.markdown(
        f"""
        <style>

        /* Fondo de toda la aplicación */
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

        /* Ocultar header de Streamlit */
        header {{
            background: transparent !important;
        }}

        /* Ocultar footer */
        footer {{
            visibility: hidden;
        }}

        /* Contenedor principal */
        .block-container {{
            padding-top: 0rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }}

        /* Texto principal */
        .welcome-title {{
            font-size: 64px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 10px;
        }}

        .welcome-subtitle {{
            font-size: 22px;
            color: rgba(255,255,255,0.85);
            text-align: center;
            max-width: 700px;
            margin: auto;
        }}

        /* Centrar todo verticalmente */
        .welcome-container {{
            height: 75vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        /* Botón */
        div.stButton {{
            text-align: center;
        }}

        div.stButton > button {{
            background: rgba(255,255,255,0.15);
            color: white;
            border: 1px solid rgba(255,255,255,0.5);
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
# ESTADO DE LA APLICACIÓN
# --------------------------------------------------
if "inicio" not in st.session_state:
    st.session_state.inicio = False


# --------------------------------------------------
# PANTALLA DE BIENVENIDA
# --------------------------------------------------
if not st.session_state.inicio:

    poner_fondo_gif("fondo.gif")

    st.markdown(
        """
        <div class="welcome-container">

            <div class="welcome-title">
                Personality Quiz
            </div>

            <div class="welcome-subtitle">
                Conoce un poco más sobre tu personalidad,
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