from gpt4all import GPT4All
from internrev import get_rag
def get_text(prompt, chosen_model, max_tokens=1024):
    model = GPT4All(chosen_model) 
    with model.chat_session():        
        system_prompt = "You are a helpful assistant that provides information based on the context provided. You are trained to handle sensitive data and provide accurate responses."
        rag_context = get_rag(prompt)

        prompt = f"""
        SYSTEM PROMPT: {system_prompt}

        THIS IS CONTEXT: {rag_context}

        USER PROMPT: {prompt}
        """
        return(model.generate(prompt, max_tokens=max_tokens))
