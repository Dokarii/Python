cantidad_huevos = 0
print(cantidad_huevos)

# Llega una orden de guevo, tocino, guevo, guevo, tocino y guevo (4 porciones más de guevo)
cantidad_huevos = cantidad_huevos + 4

if cantidad_huevos > 0:
    print("WTF? NO QUIERO GUEVOS")

cancion = "guevos " * cantidad_huevos
print(cancion)


''' cantidad_huevos = 0

Variable asignada: aquí creé una variable llamada 'cantidad_huevos' y le asigné valor 0 usando =, el cual en Python se llama operador de asignación.

Nota: Python no es como otros lenguajes de programación como: Java, C++ o C#:

- No es necesario declarar cantidad_huevos antes de asignarla.
- Tampoco necesitamos decirle a Python qué tipo de valor tiene 'cantidad_huevos'. De hecho, podemos reasignar la misma variable más adelante (de str a int, por ejemplo), aunque no es una buena práctica.

print(cantidad_huevos)

0 '''


''' Print: la función print es una función de Python que muestra el valor asignado en la pantalla. Para que la función se ejecute correctamente, le colocamos paréntesis después del nombre 'print()' y colocamos dentro de estos el argumento o parámetros.

# Pidiendo huevo, tocino, huevo, huevo, tocino y huevo (4 porciones más de huevo)
cantidad_huevos = cantidad_huevos + 4

La primera línea es un comentario; en Python, para los comentarios se usa #, y estos comentarios solo son visibles en el código.

Aquí usamos un claro ejemplo de reasignación: al darle un nuevo valor a una variable existente (cantidad_huevos), tan simple como colocar el operador de asignación más el nuevo valor.

En este caso, el nuevo valor que le agregamos a 'cantidad_huevos' fue usando una simple ecuación aritmética en su valor previo. 
Cuando el código llega a esta línea con nuevo valor, lo que hace es calcular este nuevo valor a la derecha del operador de asignación (=); entonces, el nuevo valor es: 0 + 4 = 4,
y Python usa este nuevo valor de esa línea en adelante para la variable en cuestión. '''


''' No hablaré mucho de condicionales hasta mas adelante, pero aunque nunca hayas programado antes, seguramente sabes lo que es y si sí has programado con más razón

Todo lo que pertenece al if actual no debe mostrarse a menos que 'cantidad_huevos' sea True. Pero, lo que esté mas adelante del codigo (cacnción) sí se mostrará ya que este no pertenece al If

Nota: si has programado en otros lenguajes antes, seguramente sabrás que se usan corchetes {} cuandos e trata de condicionales, en Python, eso no es necesario'''


''' Las líneas siguientes de 'canción' no hacen parte del condicional, así que estas se imprimirán sí o sí en el programa. 
Más adelante profundizaremos esto; de momento, esta explicación será suficiente.

Las cadenas pueden ser marcadas ya sea con comillas dobles o simples. 
Cuando programas usando el inglés, debes tener cuidado con esto, ya que Python puede confundirse (como por ejemplo con "But I don't want ANY egg!". Tiene comillas dobles y simples).

Con respecto a: "guevos " * cantidad_huevos. En Python podemos usar el asterisco (*) para multiplicar números (3 * 3 = 9)
pero también para multiplicar cadenas de texto ("guevo " * 3 = guevos guevos guevos). '''

# Números y aritmética en Python

# Ya vimos un ejemplo de una variable que contiene un número:
cantidad_huevos = 0

# "Número" es un nombre informal, pero podemos ser más técnicos y preguntarle a Python qué tipo de dato es:
type(cantidad_huevos)  # int

# Es un int (entero). Otro tipo común de número en Python es:
type(19.95)  # float

# Un float es un número con decimales, útil para representar cosas como pesos o proporciones.

# type() es una función incorporada (como print()) y es muy útil para preguntarle a Python: "¿qué tipo de dato es esto?"

# Operadores aritméticos en Python:

# a + b  -> Suma
# a - b  -> Resta
# a * b  -> Multiplicación
# a / b  -> División real (siempre devuelve float)
# a // b -> División entera (elimina los decimales)
# a % b  -> Módulo (residuo de la división)
# a ** b -> Exponenciación (potencia)
# -a     -> Negación

# Ejemplos de división:
print(5 / 2)   # 2.5
print(6 / 2)   # 3.0

# Siempre devuelve float

# División entera:
print(5 // 2)  # 2
print(6 // 2)  # 3

# El resultado se redondea hacia abajo

# Orden de operaciones (como en matemáticas: PEMDAS)
# Paréntesis, Exponentes, Multiplicación/División, Suma/Resta

print(8 - 3 + 2)     # 7
print(-3 + 4 * 2)    # 5

# A veces el orden por defecto no es lo que queremos:
altura_sombrero_cm = 25
mi_altura_cm = 190

# ¿Altura total en metros con sombrero?
altura_total_metros = altura_sombrero_cm + mi_altura_cm / 100
print("Altura en metros =", altura_total_metros, "?")
# Resultado incorrecto: 26.9 (lo que queremos es que devuelva la altura en un flotante)

# Solución: usar paréntesis
altura_total_metros = (altura_sombrero_cm + mi_altura_cm) / 100
print("Altura en metros =", altura_total_metros)
# Resultado correcto: 2.15 (exactamente así)

# Funciones incorporadas útiles:

# min() y max()
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3

# abs() devuelve el valor absoluto
print(abs(32))   # 32
print(abs(-32))  # 32

# int() y float() también son funciones para convertir tipos
print(float(10))     # 10.0
print(int(3.33))     # 3

# Incluso funcionan con strings
print(int('807') + 1)  # 808