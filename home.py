import streamlit as st
from gemini_wrapper import generate_text

st.title('Gemini-Wrapper Project')

st.header('Gemini API')
gemini_prompt = st.text_input('Please type your prompt')
gemini_tokens = int(st.number_input('Please select number of tokens', min_value=0, max_value=1000))
if st.button('Send'):
    generate_text(gemini_prompt, gemini_tokens)
    st.success('Content Generated')
else:
    st.warning('Please enter a prompt')
