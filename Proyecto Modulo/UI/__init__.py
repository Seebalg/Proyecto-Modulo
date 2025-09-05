def pedir_parametros():
    nombre_departamento = input("Ingrese todo el nombre del departamento en MAYUSCULAS: ").strip()
    limite_registros = int(input("Ingrese el número de registros a consultar: "))
    return nombre_departamento, limite_registros

def mostrar_resultados(df):
    columnas = ["ciudad_municipio_nom", "departamento_nom", "edad",
                "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]

    df = df.reindex(columns=[c for c in columnas if c in df.columns])

    encabezado = "{:<20} {:<15} {:<5} {:<20} {:<12} {:<20}".format(
        "Ciudad", "Departamento", "Edad", "Tipo", "Estado", "País"
    )
    print("\n" + encabezado)
    print("-" * len(encabezado))

    for _, fila in df.iterrows():
        print("{:<20} {:<15} {:<5} {:<20} {:<12} {:<20}".format(
            fila.get("ciudad_municipio_nom", ""),
            fila.get("departamento_nom", ""),
            fila.get("edad", ""),
            fila.get("fuente_tipo_contagio", ""),
            fila.get("estado", ""),
            fila.get("pais_viajo_1_nom", "") or "N/A"
        ))
