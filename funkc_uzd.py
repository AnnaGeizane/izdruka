#funkcija atgrie'z 10% no a un 20% no skait'la b
def procenti(a,b):
  a/10 b*0.20

print(procenti(100, 100))

#1. Uzraksti funkciju var_pagulet, kas atgriie'z True, ja ir br'ivdiena un False, ja ir darbadiena. (Dienas no 1 - 7)

def var_pagulet(diena):
  if diena <=5:
    return False
  else:
    return True

print(var_pagulet(4))

#pērtiķi


def ir_problema(a_smile,b_smile):
  if a_smile==b_smile:
    return True
  else:
    return False

print (ir_problema(True, True))#True

#skaitļi

def summa(skaitlis1, skaitlis2):
  if skaitlis1==skaitlis2:
    return (skaitlis1 + skaitlis2)*2
  else:
    return skaitlis1 + skaitlis2

print(skeitlis(1,2))