def rotate_array(arr,d):
    n = len(arr)
    d %= n                 # avoid the unnecessary repetation
    
    reverse(arr,0,d-1)     #step-1 reverse up to d-1
    
    reverse(arr,d,n-1)     #step-2:reverse from d to n-1
    
    reverse(arr,0,n-1)    #step -3: reverse rom 0 to n-1
    
    return arr


def reverse(arr,start,end):
    """
    function to reverse internal for the 
    rotation of array
    """
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    
ans = rotate_array([1,2,3,4,5,6],3)

print(ans)
