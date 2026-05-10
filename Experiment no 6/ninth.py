data = {"banana": 3, "apple": 5, "cherry": 1, "date": 2, "elderberry": 4}
print(f"Original: {data}")
sorted_by_keys = dict(sorted(data.items()))
print(f"Sorted by keys: {sorted_by_keys}")
sorted_by_values_asc = dict(sorted(data.items(), key=lambda item: item[1]))
print(f"Sorted by values (ascending): {sorted_by_values_asc}")
sorted_by_values_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted by values (descending): {sorted_by_values_desc}")
