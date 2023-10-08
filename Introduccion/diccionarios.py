#Creando un diccionario vacio

diccionario= {}

#print(diccionario)
#print(type(diccionario))

#asignar valorant al diccionario

diccionario["nombre" ] = "Gregory"
diccionario["edad"]="22"
#print(diccionario) 

#obtener valor vinculado a una llave
#print(diccionario["edad"])
#print(diccionario.get("edad"))

#Crear diccionario asignando valorant desde un princio
diccionario2= {5.1: 10, "vocales": ["a","e","i","o","u"], (7,2): 50 }
#print(diccionario2)

#print(len(diccionario2))

#del

del(diccionario2[(7,2)])
print(diccionario2)