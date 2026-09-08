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

/* VIDEO A PANTALLA COMPLETA */
#background-video {{
    position: fixed;
    top: 0;
    left: 0;

    width: 100vw;
    height: 100vh;

    object-fit: cover;
    object-position: center;

    z-index: 0;
    pointer-events: none;
}}


/* APP ENCIMA DEL VIDEO */
.stApp {{
    background: transparent !important;
}}

/* Contenido encima del video */
[data-testid="stAppViewContainer"] {{
    background: transparent !important;
}}

[data-testid="stMain"] {{
    position: relative;
    z-index: 1;
    background: transparent !important;
}}


/* HEADER */
header {{
    background: transparent !important;
    z-index: 2;
}}


/* FOOTER */
footer {{
    visibility: hidden;
}}


/* MENU */
#MainMenu {{
    visibility: hidden;
}}


/* CONTENEDOR PRINCIPAL */
.block-container {{
    max-width: 100%;

    padding-top: 0rem;
    padding-bottom: 2rem;

    padding-left: 4rem;
    padding-right: 4rem;
}}


.welcome-title {{
    font-size: clamp(55px, 6vw, 95px);

    font-weight: 500;

    color: white;

    text-align: center;

    letter-spacing: -3px;

    line-height: 1;

    margin-bottom: 24px;

    text-shadow:
        0px 2px 20px rgba(0,0,0,0.12);
}}


.welcome-subtitle {{
    font-size: clamp(18px, 1.5vw, 24px);

    color: rgba(255,255,255,0.92);

    text-align: center;

    line-height: 1.6;

    max-width: 720px;

    margin-left: auto;
    margin-right: auto;

    font-weight: 300;

    text-shadow:
        0px 2px 15px rgba(0,0,0,0.12);
}}


div.stButton {{
    margin-top: 25px;
}}


div.stButton > button {{

    width: 100%;

    height: 56px;

    background: rgba(255,255,255,0.10);

    color: white;

    border:
        1px solid rgba(255,255,255,0.70);

    border-radius: 50px;

    font-size: 17px;

    font-weight: 500;

    backdrop-filter: blur(8px);

    transition: all 0.3s ease;
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

</style>
""",
        unsafe_allow_html=True
    )


if "inicio" not in st.session_state:
    st.session_state.inicio = False


#welcome Screen

if not st.session_state.inicio:

#Video de fondo
    poner_fondo_video("white2.mp4")

    # Espacio superior
    st.markdown(
        "<div style='height: 27vh;'></div>",
        unsafe_allow_html=True
    )

#Título
    st.markdown(
        "<div class='welcome-title'>ESSENTIA</div>",
        unsafe_allow_html=True
    )

#Subtítulo
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

        if st.button(
            "Comenzar →",
            use_container_width=True
        ):
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
