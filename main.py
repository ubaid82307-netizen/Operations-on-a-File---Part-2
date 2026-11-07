# open a file and write something in the file
with open("sample_doc.txt", "w") as f:
    f.wrie("hello world!!!")
    
# close the file
f.close()

# open a file and split the file into word
with open("sample_doc.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
        
# close the file
file.close()