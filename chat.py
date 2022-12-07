import os
import openai

# Set the API key for OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Prompt the user for a question
question = input("Please enter a question for me to answer: ")

# Make a request to OpenAI's GPT-3 model to generate a response to the question
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question,
    temperature=0.5,
    max_tokens=1024,
    n = 1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(response["choices"][0]["text"])
