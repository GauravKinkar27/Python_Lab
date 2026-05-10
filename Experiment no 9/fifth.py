# Program to copy file contents
def copy_file():
    source = input("Enter source filename: ")
    destination = input("Enter destination filename: ")
    
    try:
        with open(source, 'r') as src:
            content = src.read()
        
        with open(destination, 'w') as dest:
            dest.write(content)
        
        print(f"Successfully copied from '{source}' to '{destination}'")
        print(f"Copied {len(content)} characters")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found")
    except Exception as e:
        print(f"Error: {e}")

copy_file()