# FUCNIONES

def menor_diferencia(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

''' Aqui creé una funcion simple llamada 'Menor diferencia' de lo que se encarga es de 
encontrar la menor diiferencia entre los numeros a, b y c. 
usando la palabra reservada abs para que devuelva un valor absoluto

'Return' es otra palabra reservada exlusiva de funciones. 
En Python, return dentro de una función sirve para devolver 
un valor o resultado al lugar donde la función fue llamada.
En otras palabras, el return finaliza la funcion y envía el resultado'''

#Pongamoslo en uso
print(
    menor_diferencia(1,10,100),
    menor_diferencia(1,10,10),
    menor_diferencia(5, 6, 7),
    #Python permite comas al final de los argumentos :)
)

#La 'help' puede explicarte como funciona una funcion (valga la redundancia)
help(menor_diferencia)
#No te creas, python no es tan inteligente como para explicar en perfecto español una funcion en base al codigo
#Pero podemos brindarleuna breve descripción a las funciones y así python lo entendera.

def menor_diferencia(a, b, c):
    """devuelve la menor diferencia entre los numeros entre a, b y c
    ej. menor_diferencia(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

help(menor_diferencia)