import pickle

#escribir fichero
lista_nombres = ["Peter","Fatima","Armando","Leonardo"]

fichero_binario = open("misAmigos","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del fichero_binario

#leer fichero
fichero = open("misAmigos","rb")
lista = pickle.load(fichero)
print(lista)