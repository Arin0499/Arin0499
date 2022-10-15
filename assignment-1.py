import numpy as np

print("Array before sorting")

unsorted_array = np.random.randint(1,40, size = (4,6))  

print(unsorted_array)

print("\nArray after row-wise sorting ascending")

sorted_array = np.sort(unsorted_array)

print(sorted_array)

print("\nArray after row-wise sorting descending")

sorted_desc = np.fliplr(sorted_array)

print(sorted_desc)

print("All index value is: ", np.where(unsorted_array))
