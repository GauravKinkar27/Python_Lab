# Program to create student information form GUI
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    roll = entry_roll.get()
    branch = branch_var.get()
    year = year_var.get()
    
    if not name or not roll:
        messagebox.showerror("Error", "Name and Roll Number are required")
        return
    
    messagebox.showinfo("Success", f"Student {name} registered successfully!")
    
    # Clear form
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(root, text="STUDENT REGISTRATION FORM", 
                 font=("Arial", 14, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Form frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Name
tk.Label(frame, text="Name:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, pady=5, sticky="w")
entry_name = tk.Entry(frame, font=("Arial", 11), width=25)
entry_name.grid(row=0, column=1, pady=5)

# Roll Number
tk.Label(frame, text="Roll No:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, pady=5, sticky="w")
entry_roll = tk.Entry(frame, font=("Arial", 11), width=25)
entry_roll.grid(row=1, column=1, pady=5)

# Branch
tk.Label(frame, text="Branch:", font=("Arial", 11), bg="#f0f0f0").grid(row=2, column=0, pady=5, sticky="w")
branch_var = tk.StringVar(value="CS")
branches = [("Computer Science", "CS"), ("Information Technology", "IT"), 
            ("Electronics", "EC"), ("Mechanical", "ME")]
for i, (text, value) in enumerate(branches):
    tk.Radiobutton(frame, text=text, variable=branch_var, value=value, 
                   bg="#f0f0f0").grid(row=2, column=i+1, pady=5, sticky="w")

# Year
tk.Label(frame, text="Year:", font=("Arial", 11), bg="#f0f0f0").grid(row=3, column=0, pady=5, sticky="w")
year_var = tk.StringVar(value="1")
years = ["1st", "2nd", "3rd", "4th"]
for i, year in enumerate(years):
    tk.Radiobutton(frame, text=year, variable=year_var, value=year,
                   bg="#f0f0f0").grid(row=3, column=i+1, pady=5, sticky="w")

# Submit button
submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"),
                       bg="green", fg="white", command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()