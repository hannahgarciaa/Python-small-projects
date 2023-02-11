import random
import time

while True:
    try:
        nivel = int(input("nivel: "))
        if nivel > 0:
            break
    except Exception:
        pass


n = random.randint(1, nivel)
op = int(input("Elige un numero de oportunidades: "))
print(f"Tienes {op} oportunidades")
print("Que comience el juego...🃏")
time.sleep(2)
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

    
