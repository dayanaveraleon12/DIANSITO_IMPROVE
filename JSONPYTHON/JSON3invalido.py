
import json

# Generar un JSON inválido (sin Numero, sin Moneda, sin FirmaDigital)
factura_invalida_3 = {
    "Factura": {
        # Falta Numero (requisito obligatorio)
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 3500000,
        # Falta Moneda (requisito obligatorio)
        "FormaPago": "Tarjeta de crédito",
        "Detalle": [
            {
                "Descripcion": "Implementación de sistema ERP",
                "Cantidad": 1,
                "ValorUnitario": 3500000
            }
        ],
        "FechaEmision": "2025-11-12"
        # Falta FirmaDigital (requisito obligatorio)
    }
}

# Convertir a JSON (string)
json_invalido_3 = json.dumps(factura_invalida_3, indent=4, ensure_ascii=False)
print(json_invalido_3)




#SALIDA ESPERDA / JSON

'''

{
    "Factura": {
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 3500000,
        "FormaPago": "Tarjeta de crédito",
        "Detalle": [
            {
                "Descripcion": "Implementación de sistema ERP",
                "Cantidad": 1,
                "ValorUnitario": 3500000
            }
        ],
        "FechaEmision": "2025-11-12"
    }
}

'''

