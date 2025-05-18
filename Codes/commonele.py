lst=[1,2,3,4,5]
lst1=[3,4,5,6,7]
common=[]

for item in lst1:
  if item in lst and item not in common:
    common.append(item)

print(common)