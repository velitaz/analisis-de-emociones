import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

st.set_page_config(page_title="Analiza tu estado 💬", page_icon="🧠")

# Encabezado
st.markdown("<h1 style='text-align: center;'>🧠 Analizador de Sentimientos</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Con mensajes especiales según cómo te sientes</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("ℹ️ ¿Qué se analiza?")
    st.markdown("""
    **Polaridad**:
    - Rango de -1 a 1.
    - -1 = muy negativo 😢, 0 = neutral 😐, 1 = muy positivo 😄

    **Subjetividad**:
    - 0 = completamente objetivo 🤖
    - 1 = muy subjetivo 😌
    """)

# Función para mostrar un mensaje personalizado
def respuesta_emocional(polaridad):
    if polaridad >= 0.5:
        st.success("🌟 ¡Eso suena muy positivo! Me alegra que te sientas bien.")
        st.markdown("**💡 Recuerda:** La actitud positiva puede abrir muchas puertas.")
        st.image("https://media.giphy.com/media/xUPGcguWZHRC2HyBRS/giphy.gif", width=300)
    elif polaridad <= -0.5:
        st.error("💔 Parece que estás pasando por un mal momento.")
        st.markdown("**✨ Consejo:** Cada día es una nueva oportunidad para sentirte mejor.")
        st.image("https://media.giphy.com/media/xT0BKiaM2VGJ411ymo/giphy.gif", width=300)
    else:
        st.info("😐 Un sentimiento neutral... tranquilo, a veces así son los días.")
        st.markdown("**🧘 Tip:** Un café, una pausa, y respira. Todo a su ritmo.")
        st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=300)

# --- Análisis principal ---
with st.expander("🔍 Analizar tu frase (en español)"):
    user_text = st.text_area("Escribe lo que estás pensando o sintiendo 👇")

    if user_text:
        translation = translator.translate(user_text, src="es", dest="en")
        translated_text = translation.text

        blob = TextBlob(translated_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown(f"**🧪 Polaridad:** `{polarity}`")
        st.markdown(f"**🧪 Subjetividad:** `{subjectivity}`")

        respuesta_emocional(polarity)

# --- Corrección ortográfica ---
with st.expander("✍️ ¿Tienes texto en inglés? Te lo corrijo"):
    input_english = st.text_area("Escribe aquí tu frase en inglés", key="english_input")

    if input_english:
        corrected = TextBlob(input_english).correct()
        st.write("✅ Frase corregida:")
        st.success(corrected)

# Pie de página
st.markdown("---")
st.markdown("<center><sub>Hecho con ❤️ para ayudarte a entender lo que sientes.</sub></center>", unsafe_allow_html=True)
