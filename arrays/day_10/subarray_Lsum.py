# we need to find the subarray with the largest sum
# arr = [2, 3, -8, 7, -1, 2, 3]
# n = len(arr)

# ans = float("-inf")
# for i in range(n-1):
#     su = arr[i]
#     for j in range(i+1,n):
#         su += arr[j]
#     ans = max(ans,su)

# print(ans)

arr = [2, 3, -8, 7, -1, 2, 3]
n = len(arr)
stn = 0
ans = float("-inf")
for i in range(n):
    stn += arr[i]
    ans = max(ans,stn)
    
    if stn < 0:
        stn = 0
        
print(ans)
    
    
    
    

        
        

