setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(f"Set A: {setA}")
print(f"Set B: {setB}")
print(f"Union (A ∪ B): {setA.union(setB)}")
print(f"Intersection (A ∩ B): {setA.intersection(setB)}")
print(f"Difference (A - B): {setA.difference(setB)}")
print(f"Difference (B - A): {setB.difference(setA)}")
print(f"Symmetric Difference (A Δ B): {setA.symmetric_difference(setB)}")
