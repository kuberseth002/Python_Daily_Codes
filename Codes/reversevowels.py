s=input("Enter a string:")
vowels="aeiouAeiou"

val=[]

for ch in s:
  if ch in vowels:
    val.append(ch)


reverse=[]
for i in range(len(val)-1,-1,-1):
  reverse.append(val[i])


res=""
idx=0

for ch in s:
  if ch in vowels:
    res+=reverse[idx]
    idx+=1
  else:
    res+=ch
print(res)






