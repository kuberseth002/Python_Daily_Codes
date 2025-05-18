lst=[1,2,1,3,4,1,6,4,2,5,7]
freq={}

for i in lst:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
print(freq)