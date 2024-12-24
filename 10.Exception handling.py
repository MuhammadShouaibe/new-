try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block runs no matter what.")
    if 'file' in locals():
        file.close()
