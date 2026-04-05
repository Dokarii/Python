'''Los booleanos tienen mucha mas utilidad cuando son combinados con condicionales
Los condicionales se pueden tomar como 'si o sino' Esto te da mas control en el codigo'''

def tipoNumero(x):
    if x == 0:
        return x,"es un cero..."
    elif x > 0:
        return x,"es un numero positivo"
    else:
        return x,"es un numero negativo"

#¿Por que uso elif y no varios if?
# Con if separados, Python evalúa TODAS las condiciones
# Con elif, en cuanto una se cumple, las demás se saltan, es más eficiente

print(tipoNumero(-8))
print(tipoNumero(0))
print(tipoNumero(8))

'''Las palabras clave `if` y `else` se usan con frecuencia en otros lenguajes; su palabra clave más singular es `elif`, una contracción de "if else". 
En estas condicionales, los bloques `elif` y `else` son opcionales; además, se pueden incluir tantas sentencias `elif` como desees.

Observa especialmente el uso de dos puntos (:) y espacios en blanco para delimitar bloques de código. 
Esto es similar a lo que ocurre al definir una función: el encabezado de la función termina con dos puntos (:)'''

def f(x):
    if x > 0:
        print('Este texto solo es visible con numeros mayor a 0. como por ejemplo:', x)
        print('Así que solo se muestran numero positivos :)')
    print('Siempre se imprime sin importar el valor de x:', x) #Esta fuera del condicional

f(1)
f(0)