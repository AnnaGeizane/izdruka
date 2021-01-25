#lists jeb saraksti
#(1,2,3,4,5)
myList=["teksts", 100, 12,8]
print(myList)
print(len(myList))# bus 3
mylist=["viens", "divi", "trīs", "četri"]
print(mylist[0])# izdrukā tikai viens
print(mylist[1:])# izdrukā no otrā ELEMENTA uz priekšu

# var konkatinēt[apvienot]
cits_lists=("pieci", "seši", "septiņi")
print(mylist + cits_lists)#izdrukā sarakstu apvienojumu, bet nemaina pašus sarakstus
jauns_list=mylist + cits_lists
print(jauns_list)
jauns_list[0]=1
print(jauns_list)#maina viens muz 1

#elementu pievienošana
jauns_list.append("astoņi")
print(jauns_list)

#elementu noņemšana
jauns_list.pop()#noņem pēdējo elementu
print(jauns_list)
pop_elen= jauns_list.pop()
print(pop_elen)
jauns_list.pop(0)#noņem elementu ar norādīto indeksu
print(jauns_list)