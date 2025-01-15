import google.generativeai as genai
import streamlit as st

def generate_text(prompt, tokens):
    google_api_key = st.secrets['gemini_api_key']
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
            max_output_tokens=tokens,
            temperature=0.1,
        )
    )

    st.text(response.text)