

file_path = 'example.txt'

try:

    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content: ", content)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")

except IOError as e:
    print(f"Error: An I/O error occurred - {e}")

except Exception as e:
    print(f"An unexpected error occurred - {e}")

else:
    print("File reading successful.")

finally:

    file.close()
    print("Execution completed.")
