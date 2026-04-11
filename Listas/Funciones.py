'''Python tiene algunas funciones utiles para usar en listas'''
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
primos = [2,3,5,7]

#len()
print('¿Cuantos planetas hay en el sistema solar?', len(planetas)) #8

#sorted()
print('Planetas ordenados alfabeticamente:', sorted(planetas))

#sum()
print('Suma de los numeors primos:', sum(primos)) #17

#max() y min()
print('Mayor numero primo:', max(primos),'\n''Menor numero primo:', min(primos))

