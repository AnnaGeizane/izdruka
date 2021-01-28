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

#elementu kārtošana
new_list = ["b", "a", "z", "e"]
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
nun_list=[4,8,1,3]
print(nun_list)
nun_list.reverse()
print(nun_list)
nun_list.sort()
print(nun_list)
s = [3.19, 100, 12,8]
s.sort()
print(s)

#saraksts sarakstā (nested)
nested_list = [8,6, [5,7]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[2][1])

#piemēri
augli = ['ābols', 'banāns', 'gurķis']
print(augli[2])
augli [2] = 'apelsīns'
print(augli)

augli.append('bumbieris')
print(aigli)

#iespraust elementu noteiktā vietā
augli.insert(2, "citrons")
print(augli)
#izņemt no saraksta
augli.pop(1)
print(augli)
#izdrukāt pilnā tekumā cuik augļi ir arakstā
print(f"šajā sarakstā ir {len(augli)} augļi ")