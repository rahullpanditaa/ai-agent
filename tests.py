from functions.run_python import run_python_file

def test_get_files_info():
    print(run_python_file("calculator", "main.py"))

test_get_files_info()