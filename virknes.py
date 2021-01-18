"""
vards=input("kā tevi sauc? ")
print(f"tavs vārds ir {vards}.")

gadi=int{input("cik tev ir gadu? ")}
print(f"tev ir {gadi} gadi.")
print(f"tavs dzimšanas gads ir {2021-gadi}.")

T=int{input("ievadi temperatūru grādos celsija")}
print(f"tie ir {T*9/5+32} grādi pēc fārenheita skalas")

#strings {rakstzīmju virknes}
print("sveiki")
print('sveiki')
print("sveika\ pasaule")#izdrukā divā rindās
print("sveika, \tpasaule")#izdrukā ar atkāpi tab

#sting garus- len()
print(len("sveiki"))
print(len("es esmu šeit"))# atstarpes arī skaitās
"""

# [sākums:beigas:solis]
myString="sveika paaule"
print(myString)
print(myString[0])#izdrukā pirmo rakstzīmi
print(myString[8])#izdrukā 9. rakstzīmi
print(myString[-3])#izdruā 14. rakstzīmi
print(mySting[-1])#izdruā pēdējo rakstzīmi

myString= "abcdefghijklmnoprstuvz"
print(myString[2])#izdrukā c
print(myString[2:])#izdrukā no c uz priekšu
print(myString[:3])#izdrukā līdz 2. rakstzīmej (galapunktu neietver)
print(myString[3:6])#izdrukā no 4. līdz 6. rakstzīmej
print(myString[::])#izdrukā visu
print(myString[::2])#izdrukā katru otro
print(myString[2:7:2])#izdrukā no trešās rakstzīmes līdz 7. rakstzīmej katru atro
print(mySring[::-1])#izdrukā otrā virzienā