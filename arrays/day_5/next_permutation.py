class Solution:
    def next_permutation(self,arr):
        
        n = len(arr)
        pivot = -1
        
        #step-1: finding the index where the break out point
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:           #if none returning the reversed array
            arr.reverse()
            return arr
        
        #step-2:swap the breakout point with next largest num from the end
        for j in range(n-1,pivot,-1):
            if arr[j] > arr[pivot]:
                arr[j],arr[pivot] = arr[pivot],arr[j]
                break
        
        #step-3: now reverse the numbers after the pivot(ascending order)
        start,end = pivot+1,n-1
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1   
        
        return arr
solution = Solution()
arr = [2,4,1,7,6,4]
ans = solution.next_permutation(arr)
print(ans)