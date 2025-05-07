number=int(input("Enter a number:"))
square=number*number

sum=0

while square>0:
  digit=square%10
  sum+=digit
  square//=10
if sum==number:
  print("neon")
else:
  print("not neon")
  