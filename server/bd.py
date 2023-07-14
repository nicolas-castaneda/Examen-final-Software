from models import Cuenta

# Lista de usuarios y contactos
BD = []

def initBD():
    BD.clear()
    BD.append(Cuenta("21345", "Arnaldo", 200, ["123", "456"]))
    BD.append(Cuenta("123", "Luisa", 400, ["456"]))
    BD.append(Cuenta("456", "Andrea", 300, ["21345"]))

def buscar_usuario(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta
    return None

def buscar_nombre(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta.nombre
    return None

def agregar_transaccion(numero, operacion):
    for cuenta in BD:
        if cuenta.numero == numero:
            cuenta.transaccion.append(operacion.to_dict())
            cuenta.saldo = cuenta.saldo + operacion.valor