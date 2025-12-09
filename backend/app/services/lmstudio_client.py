import requests

def query_llm(prompt: str, url="http://localhost:1234/v1/chat/completions"):
    payload = {"messages":[{"role":"user","content":prompt}], "model":"local-model"}
    return requests.post(url, json=payload).json()