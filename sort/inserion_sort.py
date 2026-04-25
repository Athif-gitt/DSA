# Insertion_sort
# Time = O(n^2)
# Space = O(1)

a = [1, 6, 9, 3, 5, -2, -5]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break


insertion_sort(a)
print(a)


