import streamlit as st
import openai
from personas import PERSONAS
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🎭 Prompt Playground GPT")
st.write("Choose a GPT persona and enter your prompt!")

persona = st.selectbox("Choose your GPT Persona", list(PERSONAS.keys()))
prompt = st.text_area("Your Prompt", placeholder="e.g. Help me prepare for a job interview...")

if st.button("🔮 Generate"):
    system_msg = PERSONAS[persona]
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=messages,
            temperature=0.9
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown(f"**{persona} says:**")
        st.write(reply)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
