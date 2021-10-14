class Vuelo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    def getDisponibles (self):
        return self.capacidad - len (self.pasajeros)

    def addPasajero (self, nombre):
        if self.getDisponibles ():
            self.pasajeros.append(nombre)
            return True
        else:
            return False
vuelo = Vuelo (3)

personas =['Paulina','Moises','Hector','Raul','Jocelyn']

for persona in personas:
    if vuelo.addPasajero(persona()):
        print(f'Se agrego a {persona} al vuelo')
    else:
        print(f'No hay asientos disponibles para {persona}')

print (vuelo.getDisponibles())       
