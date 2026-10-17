from openai import OpenAI


client = OpenAI(base_url="http://localhost:1234/v1", api_key="no-needed")

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="local-model",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
    )

    return response.choices[0].message.content

user = "what is capital of France?"
response = ask_chatgpt(user)
print(response)