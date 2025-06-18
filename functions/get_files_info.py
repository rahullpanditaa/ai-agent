import os

def get_files_info(working_directory, directory=None):
    work_dir_path = os.path.abspath(working_directory)
    target_dir = work_dir_path

    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    
    if not target_dir.startswith(work_dir_path):
        return f"Error: Cannot list {directory} as it is outide the permitted working directory"
    
    if not os.path.isdir(target_dir):
        return f"Error: {directory} is not a directory"
    

    files_in_directory_info = []

    try:            
        for file_name in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file_name)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_in_directory_info.append(
                f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_in_directory_info)
    except Exception:
        return "Error getting contents of the directory"

def get_file_content(working_directory, file_path):
    work_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory,file_path))

    if not target_file_path.startswith(work_dir_path):
        return f"Error: Cannot read {file_path} as it is outside the permitted working directory"
    
    if not os.path.isfile(target_file_path):
        return f"Error: File not found or is not a regular file: {file_path}"
    
    with open(target_file_path) as file:
        file_contents = file.read(10000)
        if len(file_contents) == 10000:
            file_contents += f"\n[...File \"{file_path}\" truncated at 10000 characters]"
        return file_contents