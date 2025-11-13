
# JSON de facturación inválido (sin FechaEmision y sin desglose de impuestos)
import json

factura_invalida = {
    "Factura": {
        "Numero": "FV-2025-001",
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 1500000,
        "Moneda": "COP",
        "FormaPago": "Transferencia",
        "Detalle": [
            {
                "Descripcion": "Servicio de desarrollo de software",
                "Cantidad": 1,
                "ValorUnitario": 1500000
            }
        ],
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

# Convertir a JSON (string)
json_invalido = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_invalido)



#Salida esperada:

'''

{
    "Factura": {
        "Numero": "FV-2025-001",
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        "ValorTotal": 1500000,
        "Moneda": "COP",
        "FormaPago": "Transferencia",
        "Detalle": [
            {
                "Descripcion": "Servicio de desarrollo de software",
                "Cantidad": 1,
                "ValorUnitario": 1500000
            }
        ],
        "FirmaDigital": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn..."
    }
}

'''