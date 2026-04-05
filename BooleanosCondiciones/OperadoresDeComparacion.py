'''
Operacion	Descripcion
a == b	    a igua a b
a < b	    a menor que b
a != b	    a no es igual que b
a > b	    a mayor que b
a <= b	    a menor o igual que b
a >= b	    a mayor o igual que b
'''

#Ejemplo practico
def edad_persona(x):
    """Esta funcion determina si una persona de cierta edad puede postularse para presidente
    La edad minima para dicha accion es de 30 años"""
    return x >= 30

print('¿Puede una una persona de 19 años postularse como presidente?', edad_persona(19)) #False
print('¿Puede una una persona de 34 años postularse como presidente?', edad_persona(34)) #True


print(3.0 == 3) #True
print('3' == 3) #False
print('3' == '3') #True

#Ejemplo practico
def numero_inpar(n):
    """cualquier número o es exactamente divisible entre 2 (residuo 0) o le sobra 1 (residuo 1).
    No hay otra opción, porque si sobraran 2, eso significaría que cabía una vez más el 2."""
    return(n % 2) == 1

print('¿100 es un numero inpar? ',numero_inpar(100))
print('¿9 es un numero inpar?',numero_inpar(9))