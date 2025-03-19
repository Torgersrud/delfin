import streamlit as st
from prompt import get_text
st.title("Bli kjent med Delfin.AI 🐬")
st.markdown("""
Delfin.ai er en innovativ platform som anvender kunstig intelligens (KI)-modeller på sensitive data direkte på Sikkerhetsklarerte Norske servere. Målet er å tilby en sikker, effektiv og skalerbar plattform som møter behovene til bedrifter og organisasjoner som håndterer skjermingsverdig informasjon.
""")

modelvalg = [
    "Llama 8B",
    "Llama 4B",
    "Ocra Mini 3B",
]
models = st.radio("Velg modell", modelvalg)

technical_model = {
    "Llama 8B": "Meta-Llama-3-8B-Instruct-Q6_K.gguf",
    "Llama 4B": "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    "Ocra Mini 3B": "orca-mini-3b-gguf2-q4_0.gguf",
}
model = technical_model[models]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    ki_response = get_text(prompt, model)
    response = f"Delfin: {ki_response}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(ki_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ki_response})
    

