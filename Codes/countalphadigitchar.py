string=input("Enter a string:")
alpha=char=digit=0

for ch in string:
  if 'a'<=ch<='z' or 'A'<=ch<='Z':
    alpha+=1
  elif '0' <= ch <= '9':
    digit+=1
  else:
    char+=1
print(f"alpha:{alpha},char:{char},digit:{digit}") 