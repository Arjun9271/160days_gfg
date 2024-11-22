def second_largest_element(arr):
    n = len(arr)
    first = second = float("-inf")
    if n < 2:
        return -1
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float("-inf"):
        return -1
    return second
    
value = second_largest_element([1,4,5,2,3])

print(f"the second largest element is {value} ")

# [1,4,5,2,3]
#ans - 4