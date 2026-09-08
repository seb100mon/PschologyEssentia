import streamlit as st
import base64
from pathlib import Path

# --------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------
st.set_page_config(
    page_title="Personality Quiz",
    page_icon="✨",
    layout="wide"
)


# --------------------------------------------------
# FUNCIÓN PARA USAR GIF COMO FONDO
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
            rgba(0, 0, 0, 0.20),
            rgba(0, 0, 0, 0.35)
        ),
        url("data:image/gif;base64,{gif_base64}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Ocultar elementos de Streamlit */
header {{
    background: transparent !important;
}}

footer {{
    visibility: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

/* Quitar márgenes grandes */
.block-container {{
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}}

/* CONTENEDOR DE BIENVENIDA */
.welcome-container {{
    height: 74vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}}

/* TÍTULO */
.welcome-title {{
    font-size: 72px;
    font-weight: 700;
    color: white;
    margin-bottom: 20px;
    letter-spacing: -2px;
    line-height: 1.05;
}}

/* SUBTÍTULO */
.welcome-subtitle {{
    font-size: 22px;
    color: rgba(255,255,255,0.88);
    max-width: 750px;
    line-height: 1.55;
    font-weight: 400;
}}

/* BOTÓN */
div.stButton {{
    text-align: center;
    width: 100%;
}}

div.stButton > button {{
    width: 100%;
    height: 68px;

    background: rgba(255,255,255,0.08);

    color: white;

    border: 1px solid rgba(255,255,255,0.60);

    border-radius: 40px;

    font-size: 18px;
    font-weight: 500;

    transition: all 0.3s ease;

    backdrop-filter: blur(8px);
}}

div.stButton > button:hover {{
    background: rgba(255,255,255,0.95);

    color: black;

    border: 1px solid white;

    transform: scale(1.01);
}}

div.stButton > button:active {{
    transform: scale(0.99);
}}

/* RESPONSIVE PARA CELULAR */
@media (max-width: 768px) {{

    .welcome-title {{
        font-size: 45px;
    }}

    .welcome-subtitle {{
        font-size: 18px;
        padding-left: 15px;
        padding-right: 15px;
    }}

    .block-container {{
        padding-left: 1rem;
        padding-right: 1rem;
    }}

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

    poner_fondo_gif("white.gif")

    st.markdown(
"""
<div class="welcome-container">

    <div class="welcome-title">
        Personality Quiz
    </div>

    <div class="welcome-subtitle">
        Descubre más sobre tu personalidad,<br>
        tu forma de pensar y la manera en que interactúas<br>
        con el mundo.
    </div>

</div>
""",
        unsafe_allow_html=True
    )

    if st.button(
        "Comenzar →",
        use_container_width=True
    ):

        st.session_state.inicio = True

        st.rerun()


# --------------------------------------------------
# TEST
# --------------------------------------------------
else:

    st.title("Personality Quiz")

    st.write(
        "Selecciona la opción que mejor represente tu forma de pensar o actuar."
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