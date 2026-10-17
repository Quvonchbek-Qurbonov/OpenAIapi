import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please check your .env file")

client = OpenAI(api_key=api_key)

def ask_chatgpt():
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": "what is capital of france"},
                  {"role": "assistant", "content": "The capital of France is Paris."},
                  {"role": "user", "content": "what is an interesting fact about Paris?"},],
        temperature=0.0,
    )

    return response

response = ask_chatgpt()
print("ChatId: ", response.id)
for i in response.choices:
    print("Choices: ",i)
print("Created: ", response.created)
print("LLM Model: ", response.model)
print("Object: ", response.object)
print("System fingerprint: ", response.system_fingerprint)
print("Completion tokens: ", response.usage.completion_tokens)
print("Prompt tokens: ", response.usage.prompt_tokens)
print("Total tokens: ", response.usage.total_tokens)