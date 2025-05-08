arr=[5,4,0,2,1,0,6]
res=[]


for i in arr:
  if i!=0:
    res.append(i)
    # print(res)

add=len(arr)-len(res)

for i in range(add):
  res.append(0)
print(res)