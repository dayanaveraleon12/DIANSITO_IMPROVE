import json

# Estructura estricta de la factura electrónica DIAN
factura_dian = {
    "FacturaElectronica": {
        "CUFE": "ABCDEF1234567890ABCDEF1234567890ABCDEF12",
        "Ambiente": 2,  # 2 = Producción
        "Emisor": {
            "NIT": "901234567",
            "RazonSocial": "Empresa S.A.S.",
            "Direccion": "Calle 123 #45-67",
            "Municipio": "Bogotá",
            "RegimenFiscal": "48"  # Código régimen común
        },
        "Receptor": {
            "TipoIdentificacion": "31",  # 31 = NIT
            "NumeroIdentificacion": "123456789",
            "RazonSocial": "Cliente S.A.",
            "Email": "cliente@correo.com"
        },
        "Documento": {
            "Tipo": "01",  # Factura de venta nacional
            "Numero": "F001-000000123",
            "Fecha": "2025-11-12",
            "Hora": "15:44:34-05:00",
            "Nota": "Venta de productos"
        },
        "Numeracion": {
            "Prefijo": "F001",
            "Desde": 1,
            "Hasta": 999999,
            "ClaveTecnica": "ABCDEF1234567890",
            "Autorizacion": "900123456789012345678901234567",
            "FechaInicio": "2025-11-01",
            "FechaFinal": "2026-10-31"
        },
        "Software": {
            "Identificacion": "SOFTWARE-001",
            "PIN": "123456"
        },
        "Items": [
            {
                "Codigo": "001",
                "Descripcion": "Producto A",
                "Cantidad": 2,
                "ValorUnitario": 100.0,
                "ValorTotal": 200.0,
                "Impuestos": [
                    {
                        "Tipo": "IVA",
                        "Porcentaje": 19.0,
                        "Valor": 38.0
                    }
                ]
            },
            {
                "Codigo": "002",
                "Descripcion": "Producto B",
                "Cantidad": 1,
                "ValorUnitario": 150.0,
                "ValorTotal": 150.0,
                "Impuestos": [
                    {
                        "Tipo": "IVA",
                        "Porcentaje": 19.0,
                        "Valor": 28.5
                    }
                ]
            }
        ],
        "Totales": {
            "Subtotal": 350.0,
            "Impuestos": 66.5,
            "Total": 416.5
        }
    }
}

# Convertir a JSON y mostrarlo
factura_json = json.dumps(factura_dian, indent=4, ensure_ascii=False)
print(factura_json)

# Guardar en archivo
with open("factura_dian.json", "w", encoding="utf-8") as f:
    f.write(factura_json)


#Salida o formato JSON:

'''
No python factura valida-----------------------------------------------------------------------
{
    "FacturaElectronica": {
        "CUFE": "ABCDEF1234567890ABCDEF1234567890ABCDEF12",
        "Ambiente": 2,
        "Emisor": {
            "NIT": "901234567",
            "RazonSocial": "Empresa S.A.S.",
            "Direccion": "Calle 123 #45-67",
            "Municipio": "Bogotá",
            "RegimenFiscal": "48"
        },
        "Receptor": {
            "TipoIdentificacion": "31",
            "NumeroIdentificacion": "123456789",
            "RazonSocial": "Cliente S.A.",
            "Email": "cliente@correo.com"
        },
        "Documento": {
            "Tipo": "01",
            "Numero": "F001-000000123",
            "Fecha": "2025-11-12",
            "Hora": "15:44:34-05:00",
            "Nota": "Venta de productos"
        },
        "Numeracion": {
            "Prefijo": "F001",
            "Desde": 1,
            "Hasta": 999999,
            "ClaveTecnica": "ABCDEF1234567890",
            "Autorizacion": "900123456789012345678901234567",
            "FechaInicio": "2025-11-01",
            "FechaFinal": "2026-10-31"
        },
        "Software": {
            "Identificacion": "SOFTWARE-001",
            "PIN": "123456"
        },
        "Items": [
            {
                "Codigo": "001",
                "Descripcion": "Producto A",
                "Cantidad": 2,
                "ValorUnitario": 100.0,
                "ValorTotal": 200.0,
                "Impuestos": [
                    {
                        "Tipo": "IVA",
                        "Porcentaje": 19.0,
                        "Valor": 38.0
                    }
                ]
            },
            {
                "Codigo": "002",
                "Descripcion": "Producto B",
                "Cantidad": 1,
                "ValorUnitario": 150.0,
                "ValorTotal": 150.0,
                "Impuestos": [
                    {
                        "Tipo": "IVA",
                        "Porcentaje": 19.0,
                        "Valor": 28.5
                    }
                ]
            }
        ],
        "Totales": {
            "Subtotal": 350.0,
            "Impuestos": 66.5,
            "Total": 416.5
        }
    }
}
'''