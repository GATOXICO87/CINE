class Cine:
    ASIENTO_LIBRE = "◻️"
    ASIENTO_OCUPADO = "◼️"

    def __init__(self, num_salas):
        self.salas = [[] for _ in range(num_salas)]
        self.reservas = {}
        self.reservas_totales = []

    def agregar_reserva(self, sala, fila, asientos, nombre):
        for asiento in asientos:
            if not self._asiento_valido(sala, fila, asiento):
                print(f"Asiento {asiento} en la fila {fila} de la sala {sala} es inválido.")
                continue
            if self._asiento_reservado(sala, fila, asiento):
                print(f"Asiento {asiento} en la fila {fila} de la sala {sala} ya está reservado.")
                continue
            self.reservas[(sala, fila, asiento)] = nombre
            self.salas[sala - 1][fila - 1][asiento - 1] = self.ASIENTO_OCUPADO
            self.reservas_totales.append((sala, fila, asiento, nombre))
            print(f"Asiento {asiento} en la fila {fila} de la sala {sala} reservado para {nombre}.")
        print("Reserva realizada con éxito.")

    def mostrar_asientos(self):
        for num_sala, sala in enumerate(self.salas, 1):
            print(f"Sala {num_sala}:")
            for num_fila, fila in enumerate(sala, 1):
                fila_str = " ".join(self.ASIENTO_OCUPADO if asiento == self.ASIENTO_OCUPADO else self.ASIENTO_LIBRE for asiento in fila)
                print(f"Fila {num_fila}: {fila_str}")
            print()

    def agregar_sala(self, filas, asientos_por_fila):
        nueva_sala = []
        for _ in range(filas):
            nueva_fila = [self.ASIENTO_LIBRE] * asientos_por_fila
            nueva_sala.append(nueva_fila)
        self.salas.append(nueva_sala)
        print(f"Sala {len(self.salas)} agregada con éxito.")

    def mostrar_reservas(self):
        print("Reservas Totales:")
        for i, reserva in enumerate(self.reservas_totales, 1):
            sala, fila, asiento, nombre = reserva
            print(f"{i}. Sala {sala}, Fila {fila}, Asiento {asiento}: {nombre}")

    def eliminar_reserva(self, indice):
        if indice < 1 or indice > len(self.reservas_totales):
            print("Índice de reserva inválido.")
            return
        sala, fila, asiento, _ = self.reservas_totales.pop(indice - 1)
        del self.reservas[(sala, fila, asiento)]
        self.salas[sala - 1][fila - 1][asiento - 1] = self.ASIENTO_LIBRE
        print(f"Reserva {indice} eliminada con éxito.")

    def _asiento_valido(self, sala, fila, asiento):
        return (1 <= sala <= len(self.salas)) and (1 <= fila <= len(self.salas[sala - 1])) and (1 <= asiento <= len(self.salas[sala - 1][fila - 1]))

    def _asiento_reservado(self, sala, fila, asiento):
        return (sala, fila, asiento) in self.reservas


def mostrar_menu():
    print ("------------------------------------")
    print("\n1. Mostrar asientos disponibles")
    print ("------------------------------------")
    print("2. Reservar asiento")
    print ("------------------------------------")
    print("3. Mostrar reservas")
    print ("------------------------------------")
    print("4. Eliminar reserva")
    print ("------------------------------------")
    print("5. Agregar sala")
    print ("------------------------------------")
    print("6. Salir")
    print ("------------------------------------")


def main():
    cine = Cine(3)

    for sala in cine.salas:
        for _ in range(5):
            sala.append([Cine.ASIENTO_LIBRE for _ in range(10)])

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cine.mostrar_asientos()
        elif opcion == "2":
            sala = int(input("Ingrese el número de sala: "))
            fila = int(input("Ingrese el número de fila: "))
            asientos = input("Ingrese los asientos que gustaria reservar: ").strip().split(",")
            nombre = input("Nombre de quien reserva: ")
            cine.agregar_reserva(sala, fila, [int(asiento) for asiento in asientos], nombre)
        elif opcion == "3":
            cine.mostrar_reservas()
        elif opcion == "4":
            indice = int(input("Ingresa el número de reserva que deseas eliminar: "))
            cine.eliminar_reserva(indice)
        elif opcion == "5":
            filas = int(input("Cuantas filas tendra la nueva sala: "))
            asientos_por_fila = int(input("Cuantos asientos por fila tendra la nueva sala: "))
            cine.agregar_sala(filas, asientos_por_fila)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
