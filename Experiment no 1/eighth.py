days = int(input("Enter number of days: "))
years = days // 365
remaining_days = days % 36
weeks = remaining_days // 7
remaining_days = remaining_days % 7
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)
