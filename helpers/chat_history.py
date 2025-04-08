from helpers.sessions import save_history
from helpers.sessions import load_history

chat_history=load_history()

def save_chat(role,content):
    chat_history.append({"role":role,"content":content})
    save_history(chat_history)

def get_chat():
    return chat_history
