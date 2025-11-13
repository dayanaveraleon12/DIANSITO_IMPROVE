
import json

# Generar un JSON inválido (sin NIT del receptor y sin FormaPago)
factura_invalida_2 = {
    "Factura": {
        "Numero": "FV-2025-002",
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            # Falta el NIT (requisito obligatorio)
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 2500000,
        "Moneda": "COP",
        # Falta FormaPago (requisito obligatorio)
        "Detalle": [
            {
                "Descripcion": "Consultoría en arquitectura de software",
                "Cantidad": 1,
                "ValorUnitario": 2500000
            }
        ],
        "FechaEmision": "2025-11-12",
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

# Convertir a JSON (string)
json_invalido_2 = json.dumps(factura_invalida_2, indent=4, ensure_ascii=False)
print(json_invalido_2)



#Salida esperada / JSON

'''

{
    "Factura": {
        "Numero": "FV-2025-002",
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 2500000,
        "Moneda": "COP",
        "Detalle": [
            {
                "Descripcion": "Consultoría en arquitectura de software",
                "Cantidad": 1,
                "ValorUnitario": 2500000
            }
        ],
        "FechaEmision": "2025-11-12",
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

'''