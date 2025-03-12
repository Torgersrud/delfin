from gpt4all import GPT4All
def get_text(prompt, chosen_model):
    model = GPT4All(chosen_model) 
    with model.chat_session():
        return(model.generate(prompt, max_tokens=1024))