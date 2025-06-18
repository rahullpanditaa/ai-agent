import os

def write_file(working_directory, file_path, content):
    work_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(work_dir_path):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    # if not os.path.exists(target_file_path):
    #     with open(target_file_path, "w") as file:
    #         file.write(content)
        
    #  file path already exists
    with open(target_file_path, "w") as file:
        file.write(content)


    if os.path.exists(target_file_path):
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    