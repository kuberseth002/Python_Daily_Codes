words=["apple","dolphin","elephant","dog"]
count=0

for i in range(len(words)):
  length=0
  word=words[i]
  for ch in word:
    length+=1
  if length>5:
    count+=1
print(count)