''' Si llamamos help(print), podremos ver que 'print' tiene varios argumentos.
Por ejemplo, podemos usar el valor 'sep' para separar el contrenido a imprimir'''

print(1, 2, 3, sep=' | ') #1 | 2 | 3
print("Uno", "Dos", "Tres", sep=', ') #Uno, Dos, Tres
#Si no especificamos 'sep' Python eligirá el separador por defecto que es un espacio vacio ' '

# Agregar argumentos opcionales con valores predeterminados a las funciones que definimos es bastante fácil:
def sujeto(quien="michael"):
    print("Hola,", quien)

sujeto()              # Si no pasas ningún parámetro, Python usará el valor por defecto definido en la función (michael)
sujeto(quien="rafa")  # Si pasas un argumento con nombre (quien="rafa"), se sustituye el valor por defecto.
sujeto("kedi")        # No es necesario escribir el nombre del argumento (quien), porque al ser el primero, Python lo asigna directamente.

