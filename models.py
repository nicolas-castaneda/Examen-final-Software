from datetime import datetime

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

    def historial(self):
        return {
            "saldo" : self.saldo,
            "operaciones" : self.operaciones
        }

    def pagar(self, numero_destino, valor):
        if valor > self.saldo:
            return "Saldo insuficiente"
        if numero_destino in self.contactos:
            operacion = Operacion(self.numero, numero_destino, valor)
            self.operaciones.append(operacion.to_dict())
            self.saldo = self.saldo - valor
            return operacion
        else:
            return "Contacto no encontrado en lista de contactos"


class Operacion:
    def __init__(self, numero_emisor, numero_destino, valor):
        self.numero_emisor = numero_emisor
        self.numero_destino = numero_destino
        self.fecha = datetime.now().strftime('%Y-%m-%d')
        self.valor = valor

    def to_dict(self):
        return {
            'numero_emisor': self.numero_emisor,
            'numero_destino': self.numero_destino,
            'fecha': self.fecha,
            'valor': self.valor
        }
