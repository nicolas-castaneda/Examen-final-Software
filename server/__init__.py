from flask import Flask, request, jsonify
from server.bd import initBD, buscar_usuario, buscar_nombre, agregar_transaccion

def create_app(test_config=None):
    initBD()
    app = Flask(__name__)

    @app.route('/billetera/contactos', methods=['GET'])
    def obtener_contactos():
        minumero = request.args.get('minumero')
        if minumero == None:
            return jsonify({'error': 'minumero no encontrado'}), 404

        cuenta = buscar_usuario(minumero)
        if cuenta:
            contactos = cuenta.contactos
            resultado = {}
            for contacto in contactos:
                resultado[contacto] = buscar_nombre(contacto)
            return jsonify(resultado)
        else:
            return jsonify({'error': 'Cuenta no encontrada'}), 404

    @app.route('/billetera/pagar', methods=['GET'])
    def pagar():
        minumero = request.args.get('minumero')
        numero_destino = request.args.get('numero_destino')
        valor = int(request.args.get('valor'))

        if minumero == None:
            return jsonify({'error': 'minumero no encontrado'}), 400
        
        if numero_destino == None:
            return jsonify({'error': 'numero_destino no encontrado'}), 400
        
        if valor == None:
            return jsonify({'error': 'valor no encontrado'}), 400
        
        cuenta = buscar_usuario(minumero)
        if cuenta:
            operacion = cuenta.pagar(numero_destino, valor)
            if type(operacion) != str:
                agregar_transaccion(numero_destino, operacion)
                return jsonify({
                    'numero_emisor' : operacion.numero_emisor,
                    'numero_destino' : operacion.numero_destino,
                    'fecha': operacion.fecha,
                    'valor': operacion.valor,
                    'mensaje': f'Realizado el {operacion.fecha}.'
                })
            else:
                return jsonify({'error': operacion}), 400
        else:
            return jsonify({'error': "Cuenta no encontrada"}), 404
        
    @app.route('/billetera/historial', methods=['GET'])
    def obtener_historial():
        minumero = request.args.get('minumero')
        if minumero == None:
            return jsonify({'error': 'minumero no encontrado'}), 404
        minumero = buscar_usuario(minumero)
        if minumero:
            response = {}
            historial = minumero.historial()

            saldo = historial["saldo"]

            response["nombre"] = buscar_nombre(minumero)
            response["saldo"] = saldo

            transacciones = historial["operaciones"]
            operaciones = []
            for transaccion in transacciones:
                if transaccion["numero_emisor"] == minumero:
                    operaciones.append(f"Pago realizado de {transaccion['valor']} a {buscar_nombre(transaccion['numero_destinatario'])}")
                else:
                    operaciones.append(f"Pago recibido de {transaccion['valor']} de {buscar_nombre(transaccion['numero_emisor'])}")
            
            response["operaciones"] = operaciones
            return jsonify(response)
        else:
            return jsonify({'error': 'Cuenta no encontrada'}), 404

    return app