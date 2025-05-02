import random
lst1=["spade","heart","diamond","club"]
lst2=['A','1','2','3','4','5','6','7','8','9','10','11','K','Q','J']

deck=[]

for i in lst1:
  for j in lst2:
    deck.append(i+ " " +j)

random.shuffle(deck)
for card in deck:
  print(card) 
    