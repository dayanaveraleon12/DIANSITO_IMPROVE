
import json

# Generar un JSON inválido (sin FechaEmision, sin ValorTotal, sin NIT del emisor)
factura_invalida_4 = {
    "Factura": {
        "Numero": "FV-2025-004",
        "Emisor": {
            # Falta NIT (requisito obligatorio)
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        # Falta ValorTotal (requisito obligatorio)
        "Moneda": "COP",
        "FormaPago": "Transferencia",
        "Detalle": [
            {
                "Descripcion": "Servicio de mantenimiento de software",
                "Cantidad": 1,
                "ValorUnitario": 500000
            }
        ],
        # Falta FechaEmision (requisito obligatorio)
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

# Convertir a JSON (string)
json_invalido_4 = json.dumps(factura_invalida_4, indent=4, ensure_ascii=False)
print(json_invalido_4)



#Salida / JSON

'''

{
    "Factura": {
        "Numero": "FV-2025-004",
        "Emisor": {
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "Moneda": "COP",
        "FormaPago": "Transferencia",
        "Detalle": [
            {
                "Descripcion": "Servicio de mantenimiento de software",
                "Cantidad": 1,
                "ValorUnitario": 500000
            }
        ],
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

'''