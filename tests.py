from functions.write_file import write_file

def test_get_files_info():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

test_get_files_info()