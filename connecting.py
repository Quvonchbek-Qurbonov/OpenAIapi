import os
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please check your .env file")

client = OpenAI(api_key=api_key)

def ask_chatgpt(user_message: str) -> str:
    messages: list[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(
            role="system",
            content="You are a helpful assistant.",
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=user_message,
        ),
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content or ""

user = "what is the weather today"
answer = ask_chatgpt(user)
print(answer)