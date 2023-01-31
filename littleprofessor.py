import random
# rejects level of 0 
# rejects level of 4 
# rejects level of "one" :) 
# accepts valid level 
# generates addition problems using 0-9 level 1
# generates addition problems using 10-99 level 2
# generates addition problems using 100-999 level3
mylist = ["Correcto!", "Muy Bien!", "Sigue asi!"]

while True:
    cal = input("Operacion en signo que desea realizar?: ")
    if cal in ("+", "-"):
        break
    print("Intenta de nuevo")
    continue
while True:
    nivel= input("Nivel: ")
    if nivel not in ["1", "2", "3"]:
      print("Solo hay tres niveles. Reinicia el juego")
      break

    while True:
        for _ in range(10):
           if nivel == "1":
             x = random.randint(1, 9)
             y = random.randint(1, 9)
           elif nivel == "2":
             x = random.randint(10, 99)
             y = random.randint(10, 99)
           else:
             x = random.randint(100, 999)
             y = random.randint(100, 999)


        if cal == "+":
          answer = input(f"{x} + {y} = ")
          if answer == str(x + y):
            print(random.choice(mylist))
          else:
            print("Incorrecto. Comienza de nuevo")
            break

        elif cal == "-":
          res = input(f"{x} - {y} = ")
          if res == str(x - y):
            print(random.choice(mylist))
          else:
            print("Incorrecto. Comienza de nuevo")
            break
        else:
          break
