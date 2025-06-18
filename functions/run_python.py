import os
from subprocess import run

def run_python_file(working_directory, file_path, args=None):
    work_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(work_dir_path):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory."
    
    if not os.path.exists(target_file_path):
        return f"Error: File \"{file_path}\" not found."
    
    if not target_file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."
    
    commands = ["python3", target_file_path]
    if args:
        commands.extend(args)

    result = run(commands, capture_output=True, text=True, timeout=30, cwd=work_dir_path)

    output = []

    if result.stdout:
        output.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        output.append(f"STDERR:\n{result.stderr}")

    if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

    if output:
        return "\n".join(output)
    else:
        return "No output produced"
