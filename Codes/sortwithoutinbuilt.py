lst=[5,2,1,3,4]

for i in range(len(lst)):
  for j in range(i+1,len(lst)):
    if lst[i]>lst[j]:
      lst[i],lst[j]=lst[j],lst[i]
print(lst)