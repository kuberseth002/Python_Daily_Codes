lst=[1, 2, 2, 3, 3, 3, 4]
max_ele=0
max_item=None
freq={}

for i in lst:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1

if freq[i]>max_ele:
  max_ele=freq[i]
  max_item=i
print(max_item)