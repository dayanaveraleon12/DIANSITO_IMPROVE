
import json

# Generar un JSON con errores en facturación (incumple Dirección del emisor. Nombre o razón social del cliente. IVA discriminado por ítem. Forma de pago.)

factura_invalida = {
    "numero_factura": "F002",  # OK
    "fecha_emision": "2025-11-12",  # OK
    "emisor": {
        "nit": "900123456",  # OK
        # Falta la dirección del emisor (requisito indispensable)
        "razon_social": "Comercial ABC"
    },
    "cliente": {
        # Falta el nombre o razón social del cliente (requisito indispensable)
        "documento": "987654321"
    },
    "items": [
        {
            "codigo": "B001",
            "descripcion": "Servicio de mantenimiento",
            "cantidad": 1,
            "valor_unitario": 200000
            # Falta el IVA discriminado por ítem (requisito indispensable)
        }
    ],
    "total": 200000,
    # Falta la forma de pago (requisito indispensable)
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)
