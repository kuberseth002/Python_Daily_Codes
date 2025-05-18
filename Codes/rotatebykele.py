num=[1,2,3,4,5]
k=3
n=len(num)
rotate=[]

for i in range(n):
  rotate.append(num[(i-k)%n])
print(rotate)