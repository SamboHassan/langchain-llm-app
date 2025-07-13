from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

if open_api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.""OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

client = OpenAI(
    api_key=open_api_key
)



def generate_pet_name():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )

    return completion.choices[0].message

if __name__ == "__main__":
    print(generate_pet_name())