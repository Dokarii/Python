# ¿Qué pasa si no colocamos el 'return' en una función?
# En Python, si no hay 'return', la función devuelve None por defecto.

def difference(a, b, c):
    """devuelve la menor diferencia entre los numeros entre a, b y c """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

#En teoria va a devolver None None None, ¿Por qué? porque la función no devuelve nada
print(
    difference(1, 10, 100),  # None
    difference(1, 10, 10),   # None
    difference(5, 6, 7),     # None
)

#None = Null en otros lenguajes

#Esto no solo aplica a funciones, Otro ejemplo de funciones sin uso es cuando un 'print' no devuelve nada
#Si bien no dice explicitamente 'return' en este caso, los parentesis son el return
mystery = print()
print(mystery) #None
