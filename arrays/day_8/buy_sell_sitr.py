prices = [7,1,5,3,6,4]

n = len(prices)
ans = 0
min_val = prices[0]

for i in range(1,n):
    min_val = min(min_val,prices[i])
    ans = max(ans,prices[i]-min_val)

print(ans)