import os
import requests
from dotenv import load_dotenv

load_dotenv()

def gpt_turbo_response(prompt):
    api_key = os.getenv('OPENAI_API_KEY')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'model': 'gpt-4o-mini',
        'messages': [
            {
                'role': 'user',
                'content': f'{prompt}',
            }]

    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)

    data = response.json()

    content = data['choices'][0]['message']['content']

    return content
