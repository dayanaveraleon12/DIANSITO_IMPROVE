
import json

# Generar un JSON con errores en facturación (incumple 6 requisitos DIAN)
factura_invalida = {
    # Falta el número de factura (requisito indispensable)
    "fecha_emision": "2025-11-12",
    # Falta la hora de emisión (requisito indispensable)
    "emisor": {
        "nit": "900123456-7",
        # Falta la razón social del emisor (requisito indispensable)
        "direccion": "Calle 123 #45-67, Bogotá"
        # Falta la resolución DIAN (requisito indispensable)
    },
    "cliente": {
        "nombre": "Juan Pérez",
        # Falta el tipo de documento del cliente (requisito indispensable)
        "documento": "987654321"
    },
    "items": [
        {
            "codigo": "B001",
            "descripcion": "Servicio de mantenimiento",
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
✅ Este JSON incumple los siguientes 6 requisitos DIAN:

Número de factura.
Hora de emisión.
Razón social del emisor.
Resolución DIAN.
Tipo de documento del cliente.
IVA discriminado por ítem.
(Extra) Forma de pago.
'''