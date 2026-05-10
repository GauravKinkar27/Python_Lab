# Program to demonstrate file exception handling
def file_exception_handling():
    print("=== File Exception Handling Demo ===")
    
    # Try to open non-existent file
    filename = "nonexistent.txt"
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: The file '{filename}' does not exist")
    
    # Try to write to a read-only file (simulated)
    filename = "readonly.txt"
    try:
        # Create a file first
        with open(filename, 'w') as file:
            file.write("Initial content")
        
        # Try to open in write mode (should work)
        with open(filename, 'w') as file:
            file.write("New content")
        print(f"Successfully wrote to {filename}")
    except PermissionError:
        print(f"Permission denied for {filename}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Comprehensive file handler
    def safe_file_operation():
        filename = input("\nEnter filename for operation: ")
        operation = input("Choose operation (read/write/append): ").lower()
        
        try:
            if operation == 'read':
                with open(filename, 'r') as f:
                    print("File content:")
                    print(f.read())
            elif operation == 'write':
                data = input("Enter data to write: ")
                with open(filename, 'w') as f:
                    f.write(data)
                print("Write successful")
            elif operation == 'append':
                data = input("Enter data to append: ")
                with open(filename, 'a') as f:
                    f.write(data + '\n')
                print("Append successful")
            else:
                print("Invalid operation")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except PermissionError:
            print(f"Error: Permission denied for '{filename}'")
        except IOError as e:
            print(f"IO Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print("Operation completed successfully")
        finally:
            print("File operation attempt finished")
    
    safe_file_operation()

file_exception_handling()