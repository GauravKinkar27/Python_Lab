# Program to demonstrate variable scope
# Global variable
global_var = "I am global"

def demo_scope():
    # Local variable
    local_var = "I am local"
    print("\nInside function:")
    print(f"  Accessing global_var: {global_var}")
    print(f"  Accessing local_var: {local_var}")
    
    # Modifying global variable (requires global keyword)
    global global_var
    global_var = "Modified global"
    print(f"  Modified global_var inside function: {global_var}")

print("Outside function (before call):")
print(f"  {global_var}")
demo_scope()
print("\nOutside function (after call):")
print(f"  {global_var}")
# print(local_var)  # This will cause error - local_var not accessible