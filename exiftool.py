import os
import subprocess

# Get the directory path where the current Python script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Set of allowed characters for input
allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./\\&: ")

# Assign the path of exiftool.exe
tool_path = os.path.join(script_dir, "exiftool.exe")

#Get the file Location
def get_file():
    while True:
        file_path = input("Enter the file path: ")
        #input validation
        if not set(file_path).issubset(allowed_characters):
            print("Invalid characters in input.")
            continue
        else:
            return file_path

choice = int(input("Press 1 to read the metadata \nPress 2 to remove all metadata\n"))
while(True):
    if choice == 1:
        #Reading the metadata
        file_path = get_file()
        read_data = subprocess.run([tool_path, file_path], stdout=subprocess.PIPE)
        print(read_data.stdout.decode('utf-8'))
        break
    elif choice == 2:
        #Deleting the metadata
        file_path = get_file()
        delete_data = subprocess.run([tool_path, "-all=", file_path])
        print("Copy of the original is also created")
        break
    else:
        print("Wrong value entered")
