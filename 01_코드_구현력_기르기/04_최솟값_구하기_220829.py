arr = [5, 3, 7, 9, 2, 5, 2, 6]

# solution 1
arr_min = float('inf')
for i in range(len(arr)):
    if arr[i] < arr_min:
       arr_min = arr[i]
print(arr_min)

# solution 2
arr_min = float('inf')
for i in arr:
    if i < arr_min:
        arr_min = i
print(arr_min)

# solution 3
arr_min = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
print(arr_min)
