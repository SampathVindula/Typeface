
n = 256
arr = list()
for i in range(n):
    l = list(map(int,input().split()))
    arr.append(l)
l = 0
r = n-1
t = 0
b = n-1
for i in range(n):
    if 0 in arr[i]:
        break
    else:
        t += 1
for i in range(n-1,-1,-1):
    if 0 in arr[i]:
        break
    else:
        b -= 1
transposed = list()
for i in range(n):
    row = list()
    for sublist in arr:
        row.append(sublist[i])
    transposed.append(row)
for i in range(n):
    if 0 in transposed[i]:
        break
    else:
        l += 1
for i in range(n-1,-1,-1):
    if 0 in transposed[i]:
        break
    else:
        r -= 1
result = "("+str(t)+","+str(l)+"),("+str(t)+","+str(r)+"),("+str(b)+","+str(l)+"),("+str(b)+","+str(r)+")"
print(result)
