import sys
from pathlib import Path
import streamlit as st

# Explicitly force root directory injection to resolve any container path bugs
root_path = Path(__file__).parent.absolute()
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

# Dynamic try-except block to expose any hidden container deployment import errors
try:
    from engine.core import AzerbaijaniEngine  # Adjust class/function name to match core.py
except ModuleNotFoundError as e:
    st.error(f"Execution Error: Missing namespace resolution. Details: {e}")
    st.stop()

# Streamlit UI Setup
st.title("AzTurkTranslit Engine 🇦🇿")
st.caption("Latin ↔ Perso-Arabic Bi-directional Transliteration")

# Initialize the engine
@st.cache_resource
def load_engine():
    return AzerbaijaniEngine()

engine = load_engine()

# 1. UI Input Element
user_input = st.text_input("Enter Azerbaijani Latin text:", key="latin_input")

# 2. Dynamic Execution Trigger
if user_input:
    # Process the text reactively through your compiled pipeline
    try:
        converted_text = engine.convert_latin_to_arabic(user_input)
        
        # 3. UI Output Element
        st.subheader("Perso-Arabic Transliteration:")
        st.markdown(f"### `{converted_text}`")
    except Exception as e:
        st.error(f"Runtime Engine Error: {e}")
else:
    st.info("Type text above to trigger live transliteration.")
