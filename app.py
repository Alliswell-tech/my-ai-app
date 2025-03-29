import streamlit as st
import google.generativeai as genai

st.title("🔒 My Private AI")
api_key = st.text_input("Enter Google AI Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    if prompt := st.chat_input("Ask anything"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            st.write(response.text)
