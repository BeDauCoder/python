import numpy as np

arr_a = np.array([1,2,3,4,2,3,5,4,6,7,9])
arr_b = np.array([7,8,9,10,11,12,13,14,15,2,5])

simp_number = np.intersect1d(arr_a,arr_b)

arr_c = np.array(arr_a == arr_b)

print(simp_number)
print(arr_c)