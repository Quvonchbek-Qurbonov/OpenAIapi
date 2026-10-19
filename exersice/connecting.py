import os
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)
from openai.types.shared import ReasoningEffort
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
            content="You are a helpful assistant to a software developer. Answer user question with 3-5 sentences.",
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=user_message,
        ),
    ]

    effort: ReasoningEffort = "low"

    response = client.chat.completions.create(
        model="gpt-5",
        messages=messages,
        temperature=1,
        reasoning_effort=effort,
    )

    return response.choices[0].message.content or ""

user = "what is indentation error in python"
answer = ask_chatgpt(user)
print(answer)