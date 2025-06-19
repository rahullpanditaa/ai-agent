import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

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
    
    if response.function_calls:
        for func in response.function_calls:
            print(f"Calling function : {func.name}({func.args})")
    else:
        print(response.text)


def get_prompt_from_user():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt_for_model>")
        sys.exit(1)
    else:
        return " ".join(sys.argv[1:])

# SCHEMEA FOR get_files_info function
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieve the contents of the given file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to read, relative to the working directory"
            )
        }
        
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the given .py file using the given arguments, if no arguments given assume it does not take any",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the .py file to run, relative to the working directory"
            )
        }
        
    )
)

# functions available to the LLM
available_functions = types.Tool(function_declarations=[schema_get_files_info])

def generate_response(conversation_history):
    return client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=conversation_history,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

if __name__ == "__main__":
    main()