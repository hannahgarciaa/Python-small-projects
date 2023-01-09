import time

print('Buenas tardes!')
time.sleep(2)
nombre = input('Cual es tu nombre? ')

pregunta = input('Quiere cafe? ')

if pregunta =='no':
    print('Esta bien, regrese pronto')
if pregunta == 'si':
    hay = input('hay cafe? ')
    if hay == 'no':
       time.sleep(2)
       print('Buscando cafe...')
    if hay == 'si':
        print('calentando cafe...')

    time.sleep(3)
    print('sirviendo cafe...')
    time.sleep(2)

    dulce = input('esta dulce? ')

    while dulce == 'no':
        print('poniendo azucar...')
        time.sleep(2)
        dulce = input('esta dulce? ')

    
    print('sirviendo cafe...')
    time.sleep(3)

    print('Aqui esta su cafe, ',nombre,'☕')



