# sourcery skip: remove-redundant-if
import time
#dict con comidas y calorias
#acceder a las calorias del menu segun su especie
menu = {
    "apple": 130,
    "avocado": 50,
    "banana":110,
    "contaloupe": 50,
    "grapefruite":60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime" : 20,
    "nectarine": 60,
    "orange" : 80,
    "peach":60,
    "pear": 100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries": 100,
    "tangerine":50,
    "watermelon":80,
    }
#bienvenida
print("Bienvenido al contador de calorias!")
time.sleep(0.5)
print("Llene las preguntas para averiguar su deficit calorico")
time.sleep(1)

s = str(input("Sexo: "))
t = float(input("Peso en kg: "))
x = float(input("Estatura en cm: "))
n = float(input("Edad: "))


if s == "mujer":
    C_d = (10 * t + 6.25 * x - 5 * n - 161)
else :
    C_d = (10 * t + 6.25 * x - 5 * n + 5)

print("Tu deficit calorico es", C_d , "al dia")

inp = 0

time.sleep(1)

print("Escriba 'break' cuando termine de escribir sus alimentos")
time.sleep(1)

while True:
    #restar el valor de item a cd
    item = input("Ingresa una fruta: ").lower()
    if item in menu:
       inp += menu[item]
       C_d -= menu[item]
       
    elif item == "break":
        print("Calorias consumidas:", inp)
        print(f"Quedan {C_d} calorias")
        break 
    
    else:
        print("Opcion no en inventario")
        continue
