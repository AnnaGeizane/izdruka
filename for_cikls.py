#iterācija- kādas darbības atkārtota izpildīšana
mainigais=[1, 2, 3, 4]
for elements in mainigais:
  print (elements)

my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in my_list:
  print(x)

for _ in my_list:#var nerakstīt cikla mainīgo
  print(sveiki)

#atrast pŗa skaitļu
for skaitlis in my_list:
  if skaitlis%2==0:
    print(skaitlis)
  else:
    print(f"nepāra skaitlis:{skaitlis}")

#aprēķināt summu
summa=0

for sk in my_list:
  summa=summa + sk
  print(f"pēc {sk}skaitļu pieskaitīšaanas summa ir {summa}")

print (summa)

#drukā tekstu
mystring="sveika pasaule!"
for burts in mystring:
  print(burts)

for burts in "programma":
  print(burts)

#drukā tuple
tup=(1, 2, 3, 4)
for elements in tup:
  print (elements)

my_list=[(1, 2)(3, 4)(5, 6)]
print(len(my_list))

for elements in my_list:
  print(elements)

for (a,b) in my_list:
  print (b)

my_list= [(1,2,3)(4,5,6)(7,8,9)]
for a,b,c in my_list:
  print(c)

#vārdnīcas
d={"k1":11,"k2":12,"k3",13}
for element in d:
  print (elements)#izdrukā tikai atslēgas

for element in d.items():
  print (elements)# izdrukā pārus

for atslēga, vertiba in d.items():
  print (vertiba)

#izdrukā skaitļus ar range()
for skaitlis in range(15):
  print(skaitlis + 1)

for skaitlis in range(4,15):
  print (skaitlis)

for skaitlis in range(4,15,3):
  print(skaitlis)