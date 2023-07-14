import unittest

from server import create_app
from server.bd import initBD, buscar_usuario, buscar_nombre

unittest.TestLoader.sortTestMethodsUsing = None

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # Test case: Obtener los contactos de una cuenta
    # Precondition: Cuenta debe existir en la base de datos
    # Test Data: minumero = 21345
    # Expected Results: Devolver los contactos con numero de cuenta y nombre respectivo 
    def test_1_obtener_contactos(self):
        response = self.client.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'123': 'Luisa', '456': 'Andrea'})

    # Test case: Pagar a un numero que no esta en los contactos del emisor
    # Precondition: Cuenta emisora y receptora deben existir en la base de datos
    # Test Data: minumero = 21345, numero_destino = 111, valor = 1
    # Expected Results: Mensaje de error de que el pago no se debe realizar porque el contacto no esta en la lista de contactos del emisor 
    def test_2_pagar_sin_contacto(self):
        response = self.client.get('/billetera/pagar?minumero=21345&numero_destino=111&valor=1')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Contacto no encontrado en lista de contactos'})

    # Test case: Pagar a un numero sin contar con el saldo suficiente para la transaccion
    # Precondition: Cuenta emisora y receptora deben existir en la base de datos
    # Test Data: minumero = 21345, numero_destino = 123, valor = 201
    # Expected Results: Mensaje de error de que el pago no se debe realizar porque el emisor no cuenta con el saldo suficiente para la transaccion 
    def test_3_pagar_saldo_insuficiente(self):
        response = self.client.get('/billetera/pagar?minumero=21345&numero_destino=123&valor=201')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Saldo insuficiente'})

    # Test case: Pedir el historial de una cuenta no registrada
    # Precondition: Cuenta no debe existir en la base de datos
    # Test Data: minumero = 21345
    # Expected Results: Mensaje de error de que no existe historial de una cuenta no registrada  
    def test_4_historial_de_cuenta_no_registrada(self):
        response = self.client.get('/billetera/historial?minumero=21346')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Cuenta no encontrada'})
