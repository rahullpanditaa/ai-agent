from functions.get_files_info import get_file_content

def test_get_files_info():
    # print(get_file_content("calculator", "lorem.txt"))
    print("Test 1:")
    print("-------")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Test 2:")
    print("-------")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Test 3:")
    print("-------")
    print(get_file_content("calculator", "/bin/cat"))

    

test_get_files_info()