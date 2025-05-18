s=input("Enter a string:")
compress=""
prev=""
count=0


for ch in  s:
  if ch==prev:
    count+=1
  else:
    if prev!="":
      compress+=prev+str(count)
    prev=ch
    count=1
compress+=prev+str(count)
print(compress)
