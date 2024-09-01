import pickle
class Vehiculo():
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = False

    def acelerar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
        "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", 
        self.acelera, "\nFrenando: ", self.frena)

coche1 = Vehiculo("Mazda","MX5")
coche2 = Vehiculo("toyota","MX")
coche3 = Vehiculo("Peuyot","X5")

coches = [coche1,coche2,coche3]

fichero = open("coches","wb")

pickle.dump(coches,fichero)

fichero.close()

del fichero

fichero = open("coches","rb")

misCoches=pickle.load(fichero)

fichero.close()

del fichero

for c in misCoches:
    c.estado()

