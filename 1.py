# Given an integer as input. Write a function to convert that to base 3 number

# Input: 10 
# Output: 101

n = int(input())
ans = ""
while(n>0):
    ans = str(n%3) + ans
    n //= 3
print(ans)
