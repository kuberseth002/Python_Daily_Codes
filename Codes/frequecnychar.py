def count_frequency(s):
  freq={}
  for ch in s:
    if ch not in freq:
      freq[ch]=1
    else:
      freq[ch]+=1
  return freq
s=input("Enter a string:")
print(count_frequency(s))