import requests
import zipfile
import io
import pandas as pd
import os

def extract_covid_data():
    # Official Argentina Ministry of Health ZIP URL
    url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.zip"
    
    print("Downloading ZIP from official source...")
    response = requests.get(url)
    response.raise_for_status()
    
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_name = [f for f in z.namelist() if f.endswith('.csv')][0]
        with z.open(csv_name) as csv_file:
            df = pd.read_csv(csv_file, low_memory=False, parse_dates=[
                'fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico'
            ])
    
    print("Extraction from official ZIP completed")
    return df