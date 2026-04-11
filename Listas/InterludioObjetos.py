'''No sé si durante la lectura de este repositorio hayas investigado o te haya surgido la pregunta de qué es un objeto,
la realidad es que todo en python es un objeto'''

'''Por ejemplo: En Python, los números llevan asociada una variable llamada `imag` que representa su parte imaginaria.'''

x = 12
#x es un numero real, así que su parte imaginaria es 0
print(x.imag) #0

#En caso de que seas curioso, aquí como hacer un numero complejo
c = 12 + 3j
print(c.imag)

"""Los elementos que contiene un objeto también pueden incluir funciones. 
Una función asociada a un objeto se denomina método. 
(Los elementos que no son funciones, como las imágenes, se denominan atributos).
Por ejemplo, los números tienen un método llamado `bit_length`. 
De nuevo, accedemos a él mediante la sintaxis de punto:"""

print(x.bit_length)

#Para llamarla necesaitamos parentesis
print(x.bit_length())

#De igual manera al ser algo dentro de python, podemos usar la funcion help()
help(x.bit_length)