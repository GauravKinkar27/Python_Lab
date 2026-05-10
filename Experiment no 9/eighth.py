# Program to demonstrate try-except-finally
def file_operation():
    filename = input("Enter filename: ")
    file = None
    
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if file:
            file.close()
            print("File closed successfully")
        else:
            print("File was not opened")
    print("Program execution completed")

file_operation()