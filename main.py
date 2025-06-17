import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def get_prompt_from_user():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt_for_model>")
        sys.exit(1)
    else:
        return " ".join(sys.argv[1:])

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=get_prompt_from_user()
)

print(response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)