# sourcery skip: remove-redundant-if
import random

while True:
    try:
        nivel = int(input("nivel: "))
        if nivel > 0:
            break
    except Exception:
        pass


n = random.randint(1, nivel)
op = 10
print("Tienes 10 oportunidades")
while True:
    
    try:
        guess = int(input("Adivina nivel: "))
        if guess < 0:
         continue
        if guess != n:
            op -= 1
        if op == 0:
           print(f"La respuesta era {n}. Reinicia el juego ")
           break
        if guess < n:
            print("El nivel es mas alto")
        elif guess > n:
            print("El nivel es mas bajo")
        elif guess == n:
            print("Adivinaste!")
            break
    except ValueError:
        continue

    