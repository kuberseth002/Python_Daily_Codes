s=input("Enter a string:")
vowels="aeiouAEIOU"
count=0

for ch in s:
  if ch in vowels:
    count+=1
print(f"vowels:{count}")