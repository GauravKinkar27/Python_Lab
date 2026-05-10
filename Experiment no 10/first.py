# Program to create a simple GUI window
import tkinter as tk

# Create main window
root = tk.Tk()

# Set window properties
root.title("My First GUI Window")
root.geometry("400x300")
root.configure(bg="lightblue")

# Add a label
label = tk.Label(root, text="Welcome to GUI Programming!", 
                 font=("Arial", 16), bg="lightblue")
label.pack(pady=50)

# Add a button
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_click, 
                   font=("Arial", 12), bg="yellow")
button.pack(pady=20)

# Run the application
root.mainloop()