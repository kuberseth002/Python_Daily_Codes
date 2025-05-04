arr=[7,2,4,6,3,1,8]
n=int(input("Enter nth element:"))

unique_arr=[]

for i in arr:
  if i not in unique_arr:
    unique_arr.append(i)


for i in range(len(unique_arr)):
  count=0
  value=0
  for j in range(len(unique_arr)):
    if unique_arr[j]>unique_arr[i]:
      count+=1
    elif unique_arr[j]==unique_arr[i]:
      value+=1
  
  if count<n<=count+value:
    print(unique_arr[i])
    
    

