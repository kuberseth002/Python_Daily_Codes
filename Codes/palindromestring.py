s=input("Enter a string:")
rev=""
for ch in s:
  rev=ch+rev

if rev==s:
  print("palindrome")
else:
  print("not palindrome")