import os

base_path = r"C:\Users\Gaurav\OneDrive\Desktop\Resources\college\Python_lab"

file_names = [
    "first.py", "second.py", "third.py", "fourth.py", "fifth.py",
    "sixth.py", "seventh.py", "eighth.py", "ninth.py", "tenth.py"
]

for i in range(1, 11):
    folder_name = f"Experiment no {i}"
    folder_path = os.path.join(base_path, folder_name)

    # Create folder if not exists
    os.makedirs(folder_path, exist_ok=True)

    # 🔴 Step 1: Delete existing .py files in folder
    for file in os.listdir(folder_path):
        if file.endswith(".py"):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)

    # 🟢 Step 2: Create 10 new files in each folder
    for name in file_names:
        file_path = os.path.join(folder_path, name)
        with open(file_path, "w") as f:
            f.write(f"# {name} file for {folder_name}\n")

print("All old files deleted and new files created successfully!")