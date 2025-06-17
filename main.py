import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    prompt = get_prompt_from_user()
    messages =  [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = generate_response(messages)

    if prompt.endswith("--verbose"):
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print(response.text)


def get_prompt_from_user():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt_for_model>")
        sys.exit(1)
    else:
        return " ".join(sys.argv[1:])


def generate_response(conversation_history):
    return client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=conversation_history
    )

if __name__ == "__main__":
    main()