import streamlit as st
from prompt import get_text
st.title("Hello!")
models = ["orca-mini-3b-gguf2-q4_0.gguf", 
          "en annen modell",
          "en tredje modell",
          ]

chosen_model = st.radio("choose model", models)
prompt = st.text_input("Prompt")
response = get_text(prompt, chosen_model)
st.write(response)
