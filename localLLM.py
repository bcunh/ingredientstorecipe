#bevor dieses script auszuführen ist, muss ollama installiert und "ollama run llama2" in cmd ausgeführt werden
import requests

def ollama_chat(prompt, model="llama2"):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False #Antwort wird in einem ausgegeben
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        raise Exception(f"Ollama API error: {response.text}")
