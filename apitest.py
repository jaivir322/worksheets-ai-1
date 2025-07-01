import os

from dotenv import load_dotenv  # Add this import
load_dotenv()  # Load environment variables from .env

from openai import OpenAI
print("API KEY:", os.getenv("OPENAI_API_KEY"))
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
