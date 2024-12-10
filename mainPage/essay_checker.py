from openai import OpenAI
from .my_open_ai_key import OpenAiKey
import json
from .prompts import Task1_prompt, Task2_prompt
from .prompts import *

client = OpenAI(api_key=OpenAiKey)

def check_essay(essay, task: str):
    if task == "task1":
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": [{"type": "text", "text": Task1_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": essay}]},
            ],
            temperature=1,
            max_tokens=2048,
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": [{"type": "text", "text": Task2_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": essay}]},
            ],
            temperature=1,
            max_tokens=2048,
        )
    data = json.loads(response.choices[0].message.content)
    return data
