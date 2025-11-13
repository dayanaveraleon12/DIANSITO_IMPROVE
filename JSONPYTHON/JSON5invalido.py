
import json

# Generar un JSON inválido con cinco errores (sin Numero, FechaEmision, Moneda, FormaPago, FirmaDigital)
factura_invalida_5 = {
    "Factura": {
        "Emisor": {
            "NIT": "900123456",
            "RazonSocial": "Tech Solutions S.A.S"
        },
        "Receptor": {
            "NIT": "800987654",
            "RazonSocial": "Cliente Ejemplo S.A."
        },
        # Falta Numero
        # Falta FechaEmision
        # Falta Moneda
        # Falta FormaPago
        "ValorTotal": 4500000,
        "Detalle": [
            {
                "Descripcion": "Desarrollo de aplicación móvil",
                "Cantidad": 1,
                "ValorUnitario": 4500000
            }
        ]
        # Falta FirmaDigital
    }
}

# Convertir a JSON (string)
json_invalido_5 = json.dumps(factura_invalida_5, indent=4, ensure_ascii=False)
print(json_invalido_5)




#Salida / JSON

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
        "ValorTotal": 4500000,
        "Detalle": [
            {
                "Descripcion": "Desarrollo de aplicación móvil",
                "Cantidad": 1,
                "ValorUnitario": 4500000
            }
        ]
    }
}

'''