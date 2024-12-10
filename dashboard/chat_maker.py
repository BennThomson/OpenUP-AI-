from openai import OpenAI
from mainPage.my_open_ai_key import OpenAiKey
import json

Key = OpenAiKey
client = OpenAI(api_key=Key)


def chat_maker(question: str) -> json:
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "So, accept any question and write no more than 200 words answer to them. Be precise and brief!",
                    }
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": question}]},
        ],
        response_format={"type": "text"},
        temperature=1,
        max_tokens=2048,
    )
    return response.choices[0].message.content
