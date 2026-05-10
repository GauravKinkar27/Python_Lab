# Program to append data into a file
def append_to_file():
    filename = input("Enter filename: ")
    data = input("Enter data to append: ")
    
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
        print(f"Data successfully appended to {filename}")
        
        # Display updated content
        with open(filename, 'r') as file:
            print("\nUpdated file content:")
            print(file.read())
    except Exception as e:
        print(f"Error: {e}")

append_to_file()