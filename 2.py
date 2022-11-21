# Given two strings as input, find number of occurrences of last character in second string, in the first string. Don't use string library functions for this program

# Input: “going to go to goa”, “go”
# Output: 5 (last char of str2 is o and it appeared 5 times in str1)

s1,s2 = input().split(",")
s1 = s1[1:-1]
s2 = s2[1:-1]
s = s2[-1]
c = 0
for i in s1:
    if i==s:
        c += 1
print(c)
