# Program to count lines, words, and characters
def count_file_stats():
    filename = input("Enter filename: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        lines = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
        words = len(content.split())
        characters = len(content)
        
        print(f"\nStatistics for '{filename}':")
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {characters}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

count_file_stats()