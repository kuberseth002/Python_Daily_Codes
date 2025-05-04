arr=[1,2,3,4,5,6,7,9,10]

for i in range(len(arr)-1):
  if arr[i+1]!=arr[i]+1:
    print(arr[i]+1)