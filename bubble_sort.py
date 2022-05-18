def bubble_Sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

a = [2,1,5,9,4,14]
print(bubble_Sort(a))