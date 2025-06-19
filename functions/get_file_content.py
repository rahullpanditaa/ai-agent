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