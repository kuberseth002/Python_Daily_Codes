s=input("Enter a string:")
old=input("Enter old string to replace:")
new=input("Enter a new string:")
res=""

for ch in s:
  if ch==old:
    res+=new
  else:
    res+=ch
print(res)