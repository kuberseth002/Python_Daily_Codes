s=list(input("Enter string:"))
res=""
for i in range(len(s)):
  if i%2==0:
    res+=s[i].upper()
  else:
    res+=s[i].lower()
print(res)
    


