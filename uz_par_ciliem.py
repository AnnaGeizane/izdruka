#uzd1
#lietot'ajs ievada divus veselus skaitļus. izdrokāt visus intervāla skaitļus. Abus galapunktus ieskaitot.
""""
a=int(input("ievadi sākuma skaitli"))
b=int(input("ievadi beigu skaitli"))
for i in range(a,b+1):
  print(i)
""""
#uzd2
#aprēķini skaitļa faktoriālu izmantojot ciklu. lietotājs ievada veselu skaitli. /faktoriāls= 1*2*3*4...n

a=int(input("ievadi veselu skaitli"))
faktoriāls=1
for i in range(1,a+1):
  faktoriāls=faktoriāls*i
print(F"Skaitļa {a} faktoriāls ir {faktorials}.")

#uzd3
#no lietotāja ievadītā intervāla, izvadi visus veselus skaitlus
#kas dalās ar noteiktu skaitli ko arī norāda lietotājs

a=int(input("ievadi sākuma skaitli"))
b=int(input("ievadi beigu skaitli"))
dalitajs=int(input("ievadi skaitli ar kuru jādala"))
for i in range(a,b+1):
  if i%dalitajs==0:
    print(i)

