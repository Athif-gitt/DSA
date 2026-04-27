a = [1, 6, 9, 3, 5, -2, -5]

def selection_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_index:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(a)
print(a)

