import os
import requests
from config.config import API_KEY, BASE_URL, MODEL

class AIService:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.model = MODEL
    
    def ask_question(self, question: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        }
        
        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()  # 返回问答内容
        else:
            return {"error": response.text}

