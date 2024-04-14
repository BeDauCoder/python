import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr_chan = arr[arr % 2 == 0]
arr_le = arr[arr % 2 != 0]


print(arr_le)
print(arr_chan)
print(arr.size)