#vienkārši piepildīt list ar elementiem
sarakst=list(range(0,11,2))
print(saraksts)#0 2 4 6 8 10

#enumerate- parāda indeksus tuple formā
vārds="pasaule"
for i in enumerate(vārds):
  print(i)#katram burtam iedod indeksu, raksta katru jaunā rindā

for indekss,burts in enumerate(vārds):
  print(indekss)
  print(burts)
  print("\n")

#izmanto zip - sapako vairākus elementus kā tuple
mylist1=[1,2,3]
mylist2=["a","b","c"]
for i in zip(mylist1,mylist2):
  print (i)

mylist3=[100,200,300,400]#400 neņems jo nav pāra
for i in zip(mylist1,mylist2,mylist3):
  print (i)

#izmanto in lai noskaidrotu vai objektā atrodams meklētais elements
print("x" in [1,2,3])#false
print(2 in [1,2,3])#true
print("a" in "pasaule")#true
print("mykey" in {"mykey":345})#true
print("mykey1" in {"mykey":345})#false
d={"mykey":345}
print(345 in d.keys())#false
print(345 in d.values())#true

#min un max
mylist=[10,20,30,40,100]
print(min(mylist))
print(max(mylist))

#bibliotēku importēšana
#random - nejaušs, gadījuma skaitlis
from random import shuffle
mylist[1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,65))