class Sala:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos

    def imprimir_salas(self):
        print(f"Numero de Sala: {self.numero}\nAsientos disponibles: {self.asientos}")
        print("")