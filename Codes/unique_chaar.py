s="abcdefg"
uniq=True
seen=[]

for ch in s:
  if ch in seen:
    uniq=False
    break
  seen.append(ch)
print(uniq)