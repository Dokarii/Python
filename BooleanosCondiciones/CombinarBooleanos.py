'''Se pueden combinar booleanos usando los conceptos basicos: "y", "o" y "no",
curiosamente en python las palabras para esto son: "and", "or", y "not"'''

def postulacion(nacionalidad, edad):
    """La ley dice que para postularse a presidente es necesario nacer en el pais Y tener 30 años"""
    #Todos los ejemplos son hipoteticos
    return nacionalidad and (edad >= 30)
print('¿Rafa de Narnia con 37 años se puede postular a presidente en USA?', postulacion(False, 37))
#Se deben cumplir ambas condiciones, tanto la nacionalidad y la edad, esto gracias a 'and'
print('¿Miguel de USA con 30 años se puede postular a presidente?', postulacion(True, 30))
#En este caso ambas condiciones se cumplen, por ende debe devolver True

def puede_entrar(es_miembro, es_invitado):
    """Puede entrar si es miembro O si fue invitado"""
    return es_miembro or es_invitado
print('Paola es invitada, puede entrar?', puede_entrar(False, True))
#A diferencia de and, con or basta con que una de las dos se cumpla

def es_menor(edad):
    """Verifica si NO es mayor de edad"""
    return not (edad >= 18)
print('Rafa tiene 15 de edad, es menor de edad?', es_menor(15))
#'not' simplemente niega lo que los parametros indican

'''Se puede combinar mas de dos booleanos de manera muy sencilla'''
preparado_para_la_lluvia = sombrilla or (clima < 5 and impermeable) or not (lluvia > 0 and dia_de_trabajo)

#Puede agregar incluso mas parentesis si crees que son necesarios
preparado_para_la_lluvia = sombrilla or ((clima < 5 and impermeable) or not (lluvia > 0 and dia_de_trabajo))

#Incluso, la mejor practica es dividir el contenido entre lineas, denominada 3-part estructure
preparado_para_la_lluvia = (
        sombrilla
        or ((clima < 5) and impermeable)
        or (not (lluvia > 0 and dia_de_trabajo))
)