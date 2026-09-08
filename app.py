import streamlit as st
import base64
from pathlib import Path

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="ESSENTIA",
    page_icon="",
    layout="wide"
)


def poner_fondo_gif(nombre_archivo):

    ruta = Path(__file__).parent / nombre_archivo

    if not ruta.exists():
        st.error(f"No se encontró el archivo: {nombre_archivo}")
        st.stop()

    gif = ruta.read_bytes()
    gif_base64 = base64.b64encode(gif).decode()

    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/gif;base64,{gif_base64}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
        }}

        header {{
            background: transparent !important;
        }}

        footer {{
            visibility: hidden;
        }}

        #MainMenu {{
            visibility: hidden;
        }}

        .block-container {{
            max-width: 100%;
            padding-top: 0rem;
            padding-bottom: 2rem;
            padding-left: 4rem;
            padding-right: 4rem;
        }}

        /* Título */
        .welcome-title {{
            font-size: clamp(55px, 6vw, 95px);
            font-weight: 600;
            color: white;
            text-align: center;
            letter-spacing: -3px;
            line-height: 1;
            margin-bottom: 24px;
            text-shadow: 0px 2px 20px rgba(0,0,0,0.18);
        }}

        /* Subtítulo */
        .welcome-subtitle {{
            font-size: clamp(18px, 1.5vw, 24px);
            color: rgba(255,255,255,0.90);
            text-align: center;
            line-height: 1.6;
            max-width: 720px;
            margin-left: auto;
            margin-right: auto;
            font-weight: 300;
            text-shadow: 0px 2px 15px rgba(0,0,0,0.20);
        }}

        /* Botón */
        div.stButton {{
            display: flex;
            justify-content: center;
            margin-top: 25px;
        }}

        div.stButton > button {{
            width: 100%;
            height: 56px;

            background: rgba(255,255,255,0.10);

            color: white;

            border: 1px solid rgba(255,255,255,0.65);

            border-radius: 50px;

            font-size: 17px;
            font-weight: 500;

            backdrop-filter: blur(8px);

            transition:
                background 0.3s ease,
                transform 0.3s ease,
                color 0.3s ease;
        }}

        div.stButton > button:hover {{
            background: white;
            color: black;
            border-color: white;
            transform: translateY(-2px);
        }}

        @media (max-width: 768px) {{

            .block-container {{
                padding-left: 1.5rem;
                padding-right: 1.5rem;
            }}

            .welcome-title {{
                letter-spacing: -1px;
            }}
        }}

        </style>""",
        unsafe_allow_html=True
    )


if "inicio" not in st.session_state:
    st.session_state.inicio = False


#Welcome Screen

if not st.session_state.inicio:

    poner_fondo_gif("white.gif")

    # Espacio superior
    st.markdown(
        "<div style='height: 27vh;'></div>",
        unsafe_allow_html=True
    )

    # Título
    st.markdown(
        "<div class='welcome-title'>Personality Quiz</div>",
        unsafe_allow_html=True
    )

    # Subtítulo
    st.markdown(
        "<div class='welcome-subtitle'>"
        "Descubre más sobre tu personalidad,<br>"
        "tu forma de pensar y la manera en que interactúas<br>"
        "con el mundo."
        "</div>",
        unsafe_allow_html=True
    )

    # ----------------------------------------------
    # BOTÓN CENTRADO
    # ----------------------------------------------
    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        if st.button("Comenzar →", use_container_width=True):
            st.session_state.inicio = True
            st.rerun()


#Preguntas
else:

    st.title("Personality Quiz")

    st.write(
        "Selecciona la opción que mejor represente "
        "tu forma de pensar o actuar."
    )

    respuesta = st.radio(
        "I enjoy meeting new people.",
        [1, 2, 3, 4, 5],
        horizontal=True
    )

    st.write(
        "Respuesta seleccionada:",
        respuesta
    )
