arr=[4,5,6,4,5,7,8]
res=[]

for i in range(len(arr)):
  count=0
  for j in range(len(arr)):
    if arr[i]==arr[j]:
      count+=1
  if count==1:
    res.append(arr[i])
print(res)