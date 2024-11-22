def reverse_array(arr):
    n = len(arr)
    start = 0
    end = n-1
    
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    
    return arr
    
arr = [1,7,2,9] 
p = reverse_array(arr)
print(p)