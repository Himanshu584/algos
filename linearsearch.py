def linear_search(l,n,key):
    for i in range(0,n):
        if l[i] == key:
            return i
    return -1

a = [1,3,2,7,9,36]
n = len(a)
key = 2
x = linear_search(a,n,key)
if x == -1:
    print("element not found in list")
else:
    print(f"element found at index {x}")
