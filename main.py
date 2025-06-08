import streamlit as st
from prompt import get_text



st.title("Bli kjent med Zert!")
st.markdown("""
Zert er en platform som anvender kunstig intelligens (KI)-modeller på sensitive data direkte på Sikkerhetsklarerte Norske servere. Målet er å tilby en sikker, effektiv og skalerbar plattform som møter behovene til bedrifter og organisasjoner som håndterer skjermingsverdig informasjon.
""")


modelvalg = [
    "Llama 8B",
    "Llama 4B",
    "Ocra Mini 3B",
    "Deepseek R1",
]
models = st.radio("Velg modell", modelvalg)

technical_model = {
    "Llama 8B": "Meta-Llama-3-8B-Instruct-Q6_K.gguf",
    "Llama 4B": "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    "Ocra Mini 3B": "orca-mini-3b-gguf2-q4_0.gguf",
    "Deepseek R1": "deepseek-ai_DeepSeek-R1-0528-Qwen3-8B-Q4_1.gguf",
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
        if "skygard" in prompt:
            st.image("mediabank/skygard.jpg")
        st.markdown(ki_response)
        if "video" in prompt:
            st.page_link("pages/visual.py", use_container_width=False, label="Computer Vision", help="Click here to see the video", icon="👀", )
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ki_response})
    

