arr = [2, 3, 5, 7, 2, 2]
prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = arr[i-1] + arr[i]

print(prefix)

l=1
r=3

s = prefix[r]-prefix[l-1]
print(s)
