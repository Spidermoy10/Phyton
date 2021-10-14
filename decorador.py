def decora(f):
    def envuelve():
        print('Cobija')
        f()
        print('Sabana')
    return envuelve

@decora
def hola():
    print('Hola mundo')

hola()
