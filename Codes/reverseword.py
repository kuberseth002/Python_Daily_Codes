s=input("Enter a string:")
words=s.split()
result=""

for word in words:
  reverse=""
  for ch in word:
    reverse=ch+reverse
  result+=reverse+" "
print(result)