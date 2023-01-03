#definir la instancia
class coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    
    #crar acciones de parar y arrancar true y false con sus str
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")
    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "se ha parado")


#definir el objeto coche al tipo de carro con variable
Tesla = coche("Tesla", "Modelo 3")
Laguna = coche("Renault", "Laguna")
#arrancar ambos objetos
Tesla.arrancar()
Laguna.arrancar()
#print(Laguna.arrancado)
#print(Tesla.arrancado)

#print marca y modelo de carro
print(Tesla.marca, Tesla.modelo)
print(Laguna.marca, Laguna.modelo)
#parar ambos objetos
Tesla.parar()
Laguna.parar()
