# Program to create a GUI calculator
import tkinter as tk

def click(button):
    current = entry.get()
    if button == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), justify="right", bg="white")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        b = tk.Button(frame, text=btn, font=("Arial", 14), width=5, height=2,
                      command=lambda x=btn: click(x))
        b.grid(row=i, column=j, padx=2, pady=2)

root.mainloop()