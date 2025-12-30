import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Language Translation Tool")
st.title("🌍 Language Translation Tool")

# Supported languages (gTTS safe)
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Bengali": "bn"
}

# Input text
text = st.text_area("Enter text to translate")

target_lang = st.selectbox("Target Language", list(languages.keys()))

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        try:
            tgt_code = languages[target_lang]
            translated = GoogleTranslator(source="auto", target=tgt_code).translate(text)
            st.session_state.translated_text = translated
            st.success(translated)
        except Exception as e:
            st.error("Translation failed")

# AUDIO (always visible after translation)
if st.session_state.translated_text:
    if st.checkbox("🔊 Play Audio"):
        try:
            mp3_fp = BytesIO()
            tts = gTTS(text=st.session_state.translated_text, lang=languages[target_lang])
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            st.audio(mp3_fp, format="audio/mp3")
        except:
            st.error("Audio not supported for this language")