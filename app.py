import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="ESSENTIA",
    page_icon="✨",
    layout="wide"
)

@st.cache_data
def cargar_video(nombre_archivo):
    ruta = Path(__file__).parent / nombre_archivo

    if not ruta.exists():
        return None

    video = ruta.read_bytes()
    return base64.b64encode(video).decode()

def poner_fondo_video(nombre_archivo):
    video_base64 = cargar_video(nombre_archivo)

    if video_base64 is None:
        st.error(f"No se encontró el archivo: {nombre_archivo}")
        st.stop()

    st.markdown(
        f"""
        <video autoplay muted loop playsinline id="background-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>

        <style>

        @import url('https://fonts.googleapis.com/css2?family=Saira+Stencil+One&display=swap');

        #background-video {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            object-position: center;
            z-index: -1;
            pointer-events: none;
        }}

        .stApp {{
            background: transparent !important;
            font-family: 'Saira Stencil One', sans-serif;
        }}

        [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}

        [data-testid="stMain"] {{
            background: transparent !important;
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

        .welcome-title {{
            font-family: 'Saira Stencil One', sans-serif;
            font-size: clamp(70px, 8vw, 120px);
            font-weight: 400;
            color: white;
            text-align: center;
            letter-spacing: 7px;
            line-height: 1;
            margin-bottom: 30px;
            text-shadow: 0px 2px 18px rgba(0,0,0,0.10);
        }}

        .welcome-subtitle {{
            font-family: 'Saira Stencil One', sans-serif;
            font-size: clamp(16px, 1.25vw, 20px);
            color: rgba(255,255,255,0.92);
            text-align: center;
            line-height: 1.8;
            max-width: 780px;
            margin-left: auto;
            margin-right: auto;
            font-weight: 400;
            letter-spacing: 0.5px;
            text-shadow: 0px 2px 12px rgba(0,0,0,0.08);
        }}

        .final-title {{
            font-family: 'Saira Stencil One', sans-serif;
            font-size: clamp(80px, 9vw, 135px);
            font-weight: 400;
            color: white;
            text-align: center;
            letter-spacing: 4px;
            line-height: 1;
            margin-bottom: 30px;
            text-shadow: 0px 2px 18px rgba(0,0,0,0.10);
        }}

        .final-subtitle {{
            font-family: 'Saira Stencil One', sans-serif;
            font-size: clamp(17px, 1.35vw, 22px);
            color: rgba(255,255,255,0.95);
            text-align: center;
            line-height: 1.8;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            font-weight: 400;
            letter-spacing: 0.4px;
            text-shadow: 0px 2px 12px rgba(0,0,0,0.08);
        }}

        div.stButton {{
            margin-top: 30px;
        }}

        div.stButton > button {{
            font-family: 'Saira Stencil One', sans-serif;
            width: 100%;
            height: 56px;
            background: rgba(255,255,255,0.08);
            color: white;
            border: 1px solid rgba(255,255,255,0.62);
            border-radius: 50px;
            font-size: 15px;
            font-weight: 400;
            letter-spacing: 1px;
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
        }}

        div.stButton > button:hover {{
            background: rgba(255,255,255,0.96);
            color: #111111;
            border-color: white;
            transform: translateY(-2px);
        }}

        h1, h2, h3, h4, h5, h6,
        p, span, label, div,
        input, textarea, select, button {{
            font-family: 'Saira Stencil One', sans-serif !important;
        }}

        [data-testid="stMarkdownContainer"],
        [data-testid="stWidgetLabel"] {{
            font-family: 'Saira Stencil One', sans-serif !important;
        }}

        @media (max-width: 768px) {{
            .block-container {{
                padding-left: 1.5rem;
                padding-right: 1.5rem;
            }}

            .welcome-title {{
                font-size: 56px;
                letter-spacing: 4px;
            }}

            .final-title {{
                font-size: 66px;
                letter-spacing: 2px;
            }}

            .welcome-subtitle,
            .final-subtitle {{
                font-size: 16px;
                line-height: 1.65;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "respuesta_1" not in st.session_state:
    st.session_state.respuesta_1 = None

if st.session_state.pantalla == "inicio":

    poner_fondo_video("white2.mp4")

    st.markdown(
        "<div style='height: 27vh;'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='welcome-title'>ESSENTIA</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='welcome-subtitle'>"
        "Descubre más sobre tu personalidad,<br>"
        "tu forma de pensar y la manera en que interactúas<br>"
        "con el mundo."
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        if st.button("Comenzar →", use_container_width=True):
            st.session_state.pantalla = "quiz"
            st.rerun()

elif st.session_state.pantalla == "quiz":

    st.title("Personality Quiz")

    st.write(
        "Selecciona la opción que mejor represente tu forma de pensar o actuar."
    )

    st.session_state.respuesta_1 = st.radio(
        "I enjoy meeting new people.",
        [1, 2, 3, 4, 5],
        horizontal=True
    )

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Finalizar", use_container_width=True):
            st.session_state.pantalla = "final"
            st.rerun()

elif st.session_state.pantalla == "final":

    poner_fondo_video("Final.mp4")

    st.markdown(
        "<div style='height: 25vh;'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='final-title'>Gracias</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='final-subtitle'>"
        "Tus respuestas nos ayudan a mejorar y darte una mejor experiencia.<br><br>"
        "Siéntete libre de comunicarte con nosotros."
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        if st.button("Volver al inicio", use_container_width=True):
            st.session_state.pantalla = "inicio"
            st.rerun()