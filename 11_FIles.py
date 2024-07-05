'''
11.FILES 
1. Write a program to read text file 
2. Write a program to write text to .txt file using  InputStream 
3. Write a program to read a file stream 
4. Write a program to read a file stream supports random access 
5. Write a program to read a file a just to a particular index using seek() 
6. Write a program to check whether a file is having read access and write access permissions
'''

# 1. Write a program to read text file 
def read_text_file():
    file = open("./Assets/file.txt", "r")
    print(file.read())
    file.close()

# 2. Write a program to write text to .txt file using  InputStream 
def write_text_file():
    file = open("./Assets/file.txt", "w")
    file.write("Hello World")
    file.close()

# 3. Write a program to read a file stream 
def read_file_stream():
    file = open("./Assets/file.txt", "r")
    print(file.read())
    file.close()

# 4. Write a program to read a file stream supports random access 
def read_file_stream_random_access():
    file = open("./Assets/file.txt", "r")
    print(file.read(5))
    file.close()

# 5. Write a program to read a file a just to a particular index using seek() 
def read_file_seek():
    file = open("./Assets/file.txt", "r")
    file.seek(6)
    print(file.read())
    file.close()

# 6. Write a program to check whether a file is having read access and write access permissions
def check_file_access():
    file = open("./Assets/file.txt", "r")
    print(file.readable())
    print(file.writable())
    file.close()

def main():
    read_text_file() 
    write_text_file() 
    read_file_stream() 
    read_file_stream_random_access()
    read_file_seek()  
    check_file_access() 

if __name__ == "__main__":
    main()

