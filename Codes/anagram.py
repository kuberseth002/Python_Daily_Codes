def anagram(s1,s2):
  if len(s1)!= len(s2):
    return False
  
  count1={}
  count2={}
  
  for ch in s1:
    count1[ch] = count1.get(ch,0)+1  
  for ch in s2:
    count2[ch] = count2.get(ch,0)+1
  return count1==count2
print(anagram("listen","silent"))




