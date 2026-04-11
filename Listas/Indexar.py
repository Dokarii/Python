'''Puedes acceder a cualquier elemento dentro de una lista colocando su posicion dentro de los brackets'''

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
print('El planeta mas cercano al Sol es:', planetas[0]) #Venus
'''Python y casi todos los lenguajes enumeran a partir del 0, por eso, 0: Mercurio, 1: Venus, y así sucesivamente'''

'''Tambien podemos elegir el ulimo elemento en una lista, 
pero no siempre las listas son cortas como para contra y saber cual es el ultimo elemento, por eso existe lo siguiente'''

print('El planeta más alejado al Sol es:', planetas[-1]) #Neptuno
#El '-1' directamente se va al ultimo elemento de una lista,
#tambien puede usar '-2' e irá al penultimo, '-3' para el antepenultimo y así sucesivamente

"""SLICING"""
#Se puede seleccionar un rango de elementos en una lista usando algo llamado 'slicing'
print('Los tres primeros planetas del sistema solar son:', planetas[0:3]) #['Mercurio', 'Venus', 'Tierra']

'''Los índices inicial y final son opcionales. Si omito el índice inicial, 
se asume que es 0. Por lo tanto, podría reescribir la expresión anterior como:'''
print('Los tres primeros planetas del sistema solar son:', planetas[:3])

'''Y viceversa asumiría el el indice final es el ultimo elemento de la lista'''
print(planetas[3:]) #['Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

'''Tambien funciona con negativos'''
print('Todos los planetas menos el primero y el último:', planetas[1:-1]) #['Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano']
print('Lo ultimos tres planetas del sistema solar:', planetas[-3:]) #['Saturno', 'Urano', 'Neptuno']

"""SE PUEDEN REEMPLAZAR ELEMENTOS EN UNA LISTA DE MANERA SIMILAR A ESTABLECER EL VALOR DE UNA VARIABLE"""
print(planetas) #Original
#['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

planetas[3] = "Malacandra"
print(planetas) #Modificada
#['Mercurio', 'Venus', 'Tierra', 'Malacandra', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

'''También puedes modificar varios elementos usando Slicing'''
planetas[0:3] = ['Mur', 'Vee', 'Ur']
print('Planetas modificados', planetas)
#['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

#Se ve un poco ambiguo, les voy a devolver sus antiguos nombres
planetas[0:3] = ['Mercurio', 'Venus', 'Tierra']
print('planetas originales',planetas)
#['Mercurio', 'Venus', 'Tierra', 'Malacandra', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']