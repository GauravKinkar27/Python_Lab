def read_from_file():
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nFile content:")
        print("-" * 30)
        print(content)
        print("-" * 30)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")
read_from_file()
