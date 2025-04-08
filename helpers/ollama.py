import requests

MODEL_NAME = "llama3.2"
OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    print(prompt)
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    # print(response)
    result = response.json()
    return result['response']
