prices = [7,1,5,3,6,4]
n = len(prices)

res = 0
for i in range(1,n):
    if prices[i] > prices[i-1]:
        res += prices[i] - prices[i-1]
print(res)
    