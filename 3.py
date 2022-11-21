d = [0,1,2,5,6,8,9]
def check(n):
    s = str(n)
    c = 0
    for i in s:
        if int(i) in d:
            c += 1
    if c==len(s):
        return True
    else:
        return False
l = [1]
n = input()
num = 2
while(1):
    if(check(num)):
        l.append(num)
    if(int(len(l))==int(n)):
        break
    num += 1
print(l[-1])
