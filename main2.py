new_file = open('New_file.txt', 'x')
new_file.close()

import os
print("checking if my_file exists or not ......")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")
    
my_file = open("my_file.txt", "w")
my_file.write("hi! I am penguin and I am 1  year old.")
my_file.close()

os.remove('condingle.txt')

os.rmdir('folder')