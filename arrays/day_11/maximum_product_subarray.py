arr = [-1,0,2,3,-4]
#
n = len(arr)
pre = 1
suf = 1
ans = float("-inf")

for i in range(n):
    if pre == 0:
        pre = 1
        
    if suf == 0:
        suf = 1
    
    pre *= arr[i]
    suf *= arr[n-i-1]
    
    ans = max(ans,max(pre,suf))
    
print(ans)
    