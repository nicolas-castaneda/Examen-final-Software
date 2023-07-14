# Pregunta 3

Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles atransferir por día.

## Qué cambiaría en el código(Clases/Metodos)

Dentro de la clase Cuenta se agregaría un atributo de 'max_valor_permitido' el cual sería actualizado una vez cada 24 horas para iniciarlo con el valor 200 y dentro del método 'pagar' se agregaría un condicional que verifique que el pago a realizar sea menor a lo permitido y si se realizara el pago entonces se disminuiría valor de la transacción a 'max_valor_permitido' en otro caso enviar un mensaje de error que el valor excede a lo permitido en ese día.

## Nuevos casos de prueba a adicionar

Se crearía un test donde el valor a pagar sea mayor al permitido en ese dia. En base a esto se debe devolver un mensaje de error donde figure que el valor de la transaccion es mayor al permitido.

## Riesgo

Leve debido a que la implementación requerida no hace una modificación directa del código ni elimina lógica existente solo agrega nuevos condicionales y atributos al código.

# Instalar dependencias

```
pip install -r requirements.txt
```

# Iniciar el server

```
source venv/bin/activate
bash run.bash
```

# Test 

```
source venv/bin/activate
python3 -m unittest tests.py
```
