arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
n = len(arr)
dici = {}
for i in arr:
    if i not in dici:
        dici[i] = 1
    else:
        dici[i] += 1

ans = list()
for j,k in dici.items():
    if k > n/3:
        ans.append(j)
print(ans)