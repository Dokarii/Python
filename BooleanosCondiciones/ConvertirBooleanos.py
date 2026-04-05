'''Seguramente sabrás que int() convierte cualquier valor a entero y que float() convierte cualquier valor a flotante
Entonces no te debe sorprender que bool() convierta o ma bien trate cualquier valor como booleano'''

print(bool(1)) #Trata todos los numeros como True, exceptuando el 0
print(bool(0))
print(bool('hola')) #Trata todos los strings como True, exeptuando un string en blanco
print(bool('')) #Generalmente, las secuencias vacías (cadenas, listas y otros tipos que aún no hemos visto,
                # como listas y tuplas) son "falsas" y el resto son "verdaderas".



if 0: #Recuerda. Trata todos los numeros como True, exceptuando el 0
    print(0) #Entonces, aqui esta diciendo False
elif "spam": #Trata todos los strings como True, exeptuando un string en blanco
    print("spam")

'''Python y cualquier otro lenguaje de programación siempre van a imprimir True por defecto
a menos que explicitamente se le pida que imprima False'''


"""
¿Para qué sirve esto en la práctica?
En lugar de escribir:"""
if len(nombre) > 0:   # Verifica si el string no está vacío
    print("Hola", nombre)

"""Puedes escribir simplemente:"""
if nombre:            # Un string con contenido ya es True
    print("Hola", nombre)

"""Ambos hacen lo mismo, pero el segundo es más pythonico... xd"""