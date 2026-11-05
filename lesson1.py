# שיעורי בית 1
# תרגילים על מחרוזות

# 1.
st = input("Enter a string: ")
start  = 0
end = len(st)-1
while start < end:
    if st[start] != st[end]:
        print("not palindrome")
        break
    start += 1
    end -= 1
if start >= end:
    print("palindrome!")

# 2.
str = input("Enter a string: ")
print(len(str.split()))

# 3.
str = input("Enter a string: ")
myStr = str.split()
res = myStr[0][:1]
i = 1
while i<len(myStr):
    res +=myStr[i][:1]
    i += 1
print(res)
