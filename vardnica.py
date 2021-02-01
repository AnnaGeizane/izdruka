#vārdnīcas jeb disctionaries
tel = {"direktors":"67947253","vietnieks":"65634803","sekretāre":"77403965"}
print(tel["direktors"])

cenas={"piens":1.12, "āboli":0.95, "apelsīni":1.89}
print(cenas["piens"])

d={"k1":123, "k2":[10,11,12], "k3":{"atsl1":100, "atsl2":200}}
print(d["k1"])
print(d["k3"]["atsl1"])

print(d["k2"][2])


my_dict= {'key1': ['a','b','c']}
print (my_dict)
my_list= my_dict["key1"]
print(my_list)
burts= my_list[2]
print(burts)
print(burts.upper())
#vien'a rinda
print(my_dict['key1'][2].upper())#izdruk'a lielo b

#pievieno jaunus objektus
new_dict= {'k1':100, 'k2':200 }
print(new_dict)
new_dict['k3']=300 #definē jaunu elementu
print(new_dict)
new_dict['k1'= 'simts']
print(new_dict)

#vārdnīcu metodes
print(new_dict.keys())#izdrukā atslēgas
print(new_dict.values())#izdrukā vērtības
(new_dict.items())#izdrukā pārus