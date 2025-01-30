import os
import requests
from config.config import API_KEY, BASE_URL,MODEL

def ask_ai(question):
    url = f"{BASE_URL}/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,  # 使用通义千问提供的模型
        "messages": [
            {"role": "system", "content": "你是一只猫娘，回复会以“喵”结尾"},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("choices")[0].get("message").get("content")
    else:
        return "Error: " + response.text
