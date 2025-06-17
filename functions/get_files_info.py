import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    work_dir_path = os.path.abspath(working_directory)
    search_in_dir = os.path.abspath(directory)
    if not search_in_dir.startswith(work_dir_path):
        return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    
    if not os.path.isdir(directory):
        return f"Error: {directory} is not a directory"


# get_files_info(".", "calculator")