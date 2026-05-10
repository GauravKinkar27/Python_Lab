def write_to_file():
    filename = input("Enter filename: ")
    data = input("Enter data to write: ")
    try:
        with open(filename, 'w') as file:
            file.write(data)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"Error: {e}")
write_to_file()
