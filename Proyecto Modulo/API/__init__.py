import pandas as pd
from sodapy import Socrata

def obtener_datos(nombre_departamento: str, limite_registros: int = 1000) -> pd.DataFrame:

    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr",
                         limit = limite_registros,
                         departamento_nom = nombre_departamento)
    return pd.DataFrame.from_records(results)