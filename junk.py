import os

file_path = r"C:\Users\Daniel\PycharmProjects\pythonProject\words.txt"



# file_path = "words.txt"
#
# if os.path.exists(file_path):
#     print("The file exists, ready to go!")
# else:
#     print("The file does not exist, please create it")

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
