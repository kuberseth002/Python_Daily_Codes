num=int(input("Enter a number:"))
sum=0

for i in range(1,num):
  if num%i==0:
    sum+=i

if sum==num:
  print("it is perfect number")
else:
  print("it is not")
  
