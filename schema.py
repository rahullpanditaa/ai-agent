from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Open a file with the given file path and write to it the contents passed in as an argument",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to open and write content to, relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write inside the given file path"
            )
        }
    )
)