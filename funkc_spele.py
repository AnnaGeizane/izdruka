piemers = [1,2,3,4,5,6,7]
from random import shuffle
""""
rezult = shuffle(piemers) # shuffle funkcija neatgriež rezultātu
print(rezult) #none
""""
# izveido savu shuffle funkciju, kas atgriež rezultātu
def shuffle_list(mylist):
  shuffle(mylist)
  return mylist

rezult = shuffle_list([1,2,3,4,5])
print(rezult)

#IZVEIDO 3 "GLAZITES", KUR VIENĀ IR BUMBIŅA
mylist = [" ","o"," "]
print(shuffle_list(mylist))

#izveido funkciju, kur spēlētājs noāda savu minējumu
def mans_minejums():
  minejums = ""
  while minejums not in ["1","2","3"]:
    minejums = input("izvēlies skaitli - 1, 2 vai 3: ")
  return int(minejums)
indekss = mans_minejums()

#izveido funkciju, kas pārbauda vai minējums sakrīt
def parbaudi_minejumu(mylist,minejums):
  if mylist[minejums] == "o":
    print("uzminēji!!!")
  else:
    print("neuzminēji... :(")
    print(mylist)
parbaudi_minejumu(mylist, indekss)

# pa soļiem izsauc visas funkcijas 
#norāda asaraskstu
mylist = [" ","o"," "]

#sajauc sarakstu
sajaukts_sarajsts = shuffle_list(mylist)

#spēlētāja minējums
spelet_minejums = mans_minejums()

#pārbauda spēlētāja minējumu
