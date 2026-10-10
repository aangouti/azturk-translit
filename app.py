import streamlit as st
from engine.core import AzerbaijaniEngine

# Initialize the modular engine
engine = AzerbaijaniEngine()

st.set_page_config(page_title="AzTurkTranslit Engine", layout="centered")

st.title("AzTurkTranslit Engine 🇦🇿")
st.write("An open-source tool for bi-directional Azerbaijani script conversion.")

# Text input field for testers
user_input = st.text_area("Type text in Latin script (Try typing letters 'b' or 'p'):", value="bp")

if user_input:
    # Process text using the rule core
    output_text = engine.convert_latin_to_arabic(user_input)
    
    st.write("### Perso-Arabic Script Result:")
    # Render with Right-to-Left styling for proper Arabic script orientation
    st.markdown(
        f'<div style="font-size: 28px; direction: rtl; text-align: right; background-color: #f0f2f6; padding: 15px; border-radius: 5px;">{output_text}</div>',
        unsafe_allow_html=True
    )
