def saskaiti_skaitlus(sk1, sk2):
  rez = sk1 + sk2# va bez 's'is rindas bet rez viet'a uzreiz liek sk1+sk2
  return rez

rez1=print(saskaiti_skaitlus(5,11))
rez2=print(saskaiti_skaitlus(52,1.1))
print(rez1,rez2)#tagad raksta rind'a


#noskaidro vai tas ir p'ara skaitlis
def parbaudi_pari(skaitlis):
  return skaitlis % 2==0

print(parbaudi_pari(45))#false
print(parbaudi_pari(12))#true
print(parbaudi_pari(7))

#atgriež true, ja sarakstā ir kaut viens pāra skaitlis
def parbaudi_pari_list(saraksts):
  for skaitlis in saraksts:
    if skaitlis % 2==0:
      return True
#true

print(parbaudi_pari_list(1,3,5))#none
