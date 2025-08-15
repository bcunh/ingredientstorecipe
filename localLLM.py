#before this script can be executed, ollama must be installed and 'ollama run llama2' must be executed in cmd
import requests

def ollama_chat(prompt, model="llama2"):
    url = "http://localhost:11434/api/generate" #local ollama API
    headers = {"Content-Type": "application/json"} #in JSON format
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False #answer displayed in one chunk
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        raise Exception(f"Ollama API error: {response.text}")
