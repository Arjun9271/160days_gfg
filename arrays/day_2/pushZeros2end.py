def pushZeros2end(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count += 1
    return arr

modified_arr = pushZeros2end([1,2,0,3,0,5])
print(modified_arr)

# arr = [1,2,0,3,0,5]
# ans-[1,2,3,5,0,0]