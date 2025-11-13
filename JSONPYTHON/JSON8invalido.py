
import json

# Generar un JSON con errores en facturación (incumple 8 requisitos DIAN distintos)
factura_invalida = {
    # Falta el número de factura
    "fecha_emision": "",  # Fecha vacía (incorrecto)
    # Falta la hora de emisión
    "emisor": {
        "nit": "",  # NIT vacío (incorrecto)
        "razon_social": "",  # Razón social vacía (incorrecto)
        # Falta la dirección del emisor
        # Falta la resolución DIAN
    },
    "cliente": {
        # Falta el nombre del cliente
        "documento": "",  # Documento vacío (incorrecto)
        # Falta el tipo de documento
        # Falta la dirección del cliente
    },
    "items": [
        {
            # Falta el código del producto
            # Falta la descripción del producto
            "cantidad": 0,  # Cantidad inválida
            "valor_unitario": 0  # Valor unitario inválido
            # Falta el IVA discriminado
        }
    ],
    # Falta el subtotal
    # Falta el total
    # Falta la forma de pago
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)


'''
Incumple:

Número de factura.
Fecha de emisión (vacía).
Hora de emisión.
NIT del emisor (vacío).
Razón social del emisor (vacía).
Dirección del emisor.
Resolución DIAN.
Nombre del cliente.
Documento del cliente (vacío).
Tipo de documento del cliente.
Dirección del cliente.
Código del producto.
Descripción del producto.
IVA discriminado.
Subtotal.
Total.
Forma de pago.

'''