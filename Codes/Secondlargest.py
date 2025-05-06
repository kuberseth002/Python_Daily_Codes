arr=[4,5,9,6,2,1,3]
max_val=arr[0]

for i in arr:
  if i>max_val:
    max_val=i
  
  sec_max=0
  for i in arr:
    if i>sec_max and i<max_val:
      sec_max=i
print(sec_max)