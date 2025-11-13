
import json

# Generar un JSON con errores en facturación (incumple 8 requisitos DIAN)
factura_invalida = {
    # Falta el número de factura (requisito indispensable)
    # Falta la fecha de emisión (requisito indispensable)
    # Falta la hora de emisión (requisito indispensable)
    "emisor": {
        # Falta el NIT del emisor (requisito indispensable)
        # Falta la razón social del emisor (requisito indispensable)
        "direccion": "Calle 123 #45-67, Bogotá"
        # Falta la resolución DIAN (requisito indispensable)
    },
    "cliente": {
        # Falta el nombre o razón social del cliente (requisito indispensable)
        "documento": "987654321"
        # Falta el tipo de documento del cliente (requisito indispensable)
    },
    "items": [
        {
            "codigo": "B001",
            # Falta la descripción del producto o servicio (requisito indispensable)
            "cantidad": 1,
            "valor_unitario": 200000
            # Falta el IVA discriminado (requisito indispensable)
        }
    ],
    "subtotal": 200000,
    "total": 200000
    # Falta la forma de pago (requisito indispensable)
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)


'''
✅ Este JSON incumple los siguientes 8 requisitos DIAN:

Número de factura.
Fecha de emisión.
Hora de emisión.
NIT del emisor.
Razón social del emisor.
Resolución DIAN.
Nombre o razón social del cliente.
Tipo de documento del cliente.
(Extra) Descripción del producto o servicio.
(Extra) IVA discriminado.
(Extra) Forma de pago.
'''