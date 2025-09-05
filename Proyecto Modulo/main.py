from API import obtener_datos
from UI import pedir_parametros, mostrar_resultados

def main():
    try:
        nombre_departamento, limite_registros = pedir_parametros()
        df = obtener_datos(nombre_departamento, limite_registros)
        mostrar_resultados(df)
    except Exception as e:
        print("Error al consultar la API: ", e)
        print("Verifique el nombre del departamento e intente nuevamente.")

if __name__ == "__main__":
    main()