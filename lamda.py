libros= [
    {'Título':'El principito', 'Año':1943},
    {'Título':'El arte de la guerra', 'Año':1772},
    {'Título':'La ciudad de las vestias', 'Año':2002},
    {'Título':'El Hobbit', 'Año':1984},
    {'Título':'La grieta', 'Año':2007},
]

#libros.sort()
#no podemos comparar objetos sin decir algo mas sobre ellos
#libros.sort(key='Año')
#Sort no sabe que debe de buscar dentro del diccionario

def ftitulo(libro):
    return libro['Título'].upper()
def fanio(libro):
    return libro['Año']

#print(ftitulo(libros[0]))
#print(fanio(libros[0]))

print(libros)
print()
print('Libros ordenados por año: ')
#libros.sort(key=fanio)
print(libros)

print('Libros ordenados por título: ')
#libros.sort(key=ftitulo)
print(libros)

libros.sort(key=lambda x:x['Año'])
for libro in libros:
    print(f"El libro {libro['Título']} fue publicado en {libro['Año']}")
#print(libros)

libros.sort(key=lambda x:x['Título'])
#print(libros)