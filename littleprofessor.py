# sourcery skip: remove-unnecessary-else
import random

mylist = ["Correcto!", "Muy Bien!", "Sigue asi!"]


while True:
    cal = input("Operacion en signo que desea realizar?: ")
    if cal in ("+", "-"):
        break
    print("Intenta de nuevo")
    continue
while True:
    nivel= input("Nivel: ")
    if nivel in ["1", "2", "3"]:
      break
    else:
      print("Solo hay tres niveles. Intenta de nuevo")
      continue

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
            print("Incorrecto. Comienza desde cero")
            break

        elif cal == "-":
          res = input(f"{x} - {y} = ")
          if res == str(x - y):
            print(random.choice(mylist))
          else:
            print("Incorrecto. Comienza desde cero")
            break
        else:
          break
