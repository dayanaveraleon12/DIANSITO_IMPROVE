
import json

# Generar un JSON con errores en facturación (incumple 6 requisitos DIAN diferentes)
factura_invalida = {
    # Falta el número de factura (requisito indispensable)
    # Falta la fecha de emisión (requisito indispensable)
    "emisor": {
        "nit": "900123456-7",
        "razon_social": "Comercial XYZ",
        # Falta la dirección del emisor (requisito indispensable)
        # Falta la resolución DIAN (requisito indispensable)
    },
    "cliente": {
        # Falta el nombre o razón social del cliente (requisito indispensable)
        "documento": "987654321",
        "tipo_documento": "CC"
    },
    "items": [
        {
            "codigo": "P001",
            "descripcion": "Producto genérico",
            "cantidad": 3,
            "valor_unitario": 50000
            # Falta el IVA discriminado por ítem (requisito indispensable)
        }
    ],
    "subtotal": 150000,
    "total": 150000
    # Falta la forma de pago (requisito indispensable)
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)



'''
✅ Este JSON incumple los siguientes 6 requisitos DIAN:

Número de factura.
Fecha de emisión.
Dirección del emisor.
Resolución DIAN.
Nombre o razón social del cliente.
IVA discriminado por ítem.
(Extra) Forma de pago.
'''