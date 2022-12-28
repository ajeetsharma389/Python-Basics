import os
### list the current directory
current_dir = os.listdir()

for item in current_dir:
    if os.path.isdir(item):
        print(f"{item} is a directory \n")
    else:
        print(f"{item} is a file \n")

##### EX1: Copy the content of one file into another file
file_path1 = open("sample.txt")

content =  file_path1.read()

print(content)

file_path1.close()

new_file_path2 = open("sample2.txt", 'w')

new_file_path2.write(content)

new_file_path2.close()

