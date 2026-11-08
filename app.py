import sys
import urllib.parse
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

# -------------------------------------------------------------------------
# 4. Interactive Feedback Block
# -------------------------------------------------------------------------
st.markdown("---")

with st.expander("💡 Report a Mis-transliteration / Give Feedback"):
    st.write(
        "Notice a broken phonetic rule or an irregular Arabic loanword spelling? "
        "Submit it below to help update the core lexicon dictionary!"
    )
    
    with st.form("feedback_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            word_latin = st.text_input("Azerbaijani Word (Latin)", placeholder="e.g., həyat")
        with col2:
            suggested_perso_arabic = st.text_input("Correct Perso-Arabic Spelling", placeholder="e.g., حیات")
            
        additional_notes = st.text_area(
            "Etymological Notes / Reference", 
            placeholder="e.g., Arabic loanword, breaks phonetic 'ə' rule due to historical spelling."
        )
        
        submitted = st.form_submit_button("Generate GitHub Correction Issue")
        
        if submitted:
            if not word_latin or not suggested_perso_arabic:
                st.error("Please fill in both the Latin word and the suggested Perso-Arabic script.")
            else:
                # IMPORTANT: Update these string parameters with your actual GitHub path
                GITHUB_USER = "aydin" # Replace with your actual GitHub profile name if different
                GITHUB_REPO = "azturk-translit"
                
                # Format the Issue Title and Markdown template payload
                issue_title = f"Lexicon Update Request: {word_latin}"
                issue_body = (
                    f"### 📑 Lexicon Correction Report\n\n"
                    f"- **Word (Latin):** `{word_latin}`\n"
                    f"- **Suggested Perso-Arabic:** `{suggested_perso_arabic}`\n\n"
                    f"### 📝 Context & Notes\n"
                    f"{additional_notes if additional_notes else 'No additional context provided.'}\n\n"
                    f"--- \n"
                    f"*Generated automatically via AzTurkTranslit Engine Web UI feedback form.*"
                )
                
                # Safe URL encoding to handle spaces and Persian characters in query string
                encoded_title = urllib.parse.quote(issue_title)
                encoded_body = urllib.parse.quote(issue_body)
                
                github_url = f"https://github.com{GITHUB_USER}/{GITHUB_REPO}/issues/new?title={encoded_title}&body={encoded_body}"
                
                st.success("🎉 Issue payload structured successfully!")
                st.markdown(
                    f'Next step: Click below to review and open the issue directly inside your repo workflow.'
                )
                st.markdown(
                    f'<a href="{github_url}" target="_blank" style="text-decoration:none;">'
                    f'<div style="background-color:#238636;color:white;text-align:center;padding:10px 20px;'
                    f'border-radius:6px;cursor:pointer;font-weight:bold;display:block;">'
                    f'🚀 Open & Submit Correction Issue on GitHub'
                    f'</div></a>',
                    unsafe_allow_html=True
                )
