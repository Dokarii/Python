'''A continuacion viene algo muy poderoso, aunque al principio puede verse confuso'''

def mult_cinco(x):
    return 5 * x  # función sencilla que multiplica cualquier número por cinco

def call(x, y):
    return x(y)   # aplica la función x al argumento y

def al_cuadrado(x, y):
    return x(x(y))  # aplica la función x dos veces seguidas

print(
    call(mult_cinco, 1),        # mult_cinco(1) → 5
    al_cuadrado(mult_cinco, 1), # mult_cinco(mult_cinco(1)) → mult_cinco(5) → 25
    sep='\n', # '\n' es el caracter para una nueva linea
)

'''Las funciones que operan sobre otras funciones se denominan "funciones de orden superior". 
Probablemente no escribirás las tuyas propias por un tiempo. 
Sin embargo, Python incluye funciones de orden superior que podrían resultarte útiles.
Aquí tienes un ejemplo interesante con la función `max`.
Por defecto, `max` devuelve el mayor de sus argumentos. 
Pero si le pasamos una función con el argumento opcional `key`, 
devuelve el argumento `x` que maximiza `key(x)` (también conocido como `argmax`).'''

def residuo_5(x):
    """ devuelve el residuo de x despues de dividirlo entre 5"""
    return x % 5

print(
    'que numero es mayor',
    max(100, 50, 30),
    'que numero tiene el mayor residuo de 5? ',
    max(12, 17, 26, key=residuo_5), # Lo que hace 'key' es aplicar la funcion a cada numero antes de compararlos
    sep='\n'                        # Por esto mismo, devuelve el residuo mayor y no el numero mayor
)