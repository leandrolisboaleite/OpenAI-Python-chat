import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

question = input("Please enter a question for me to answer: ")

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question,
    temperature=0.5,
    max_tokens=1024,
    n = 1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response["choices"][0]["text"])
