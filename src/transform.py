import pandas as pd
import os

def transform_covid_data(df_raw):
    df = df_raw.copy()
    
    df['fallecido'] = df['fallecido'].map({'SI': 1, 'NO': 0, '': 0}).fillna(0)
    df['asistencia_respiratoria_mecanica'] = df['asistencia_respiratoria_mecanica'].map({'SI': 1, 'NO': 0, '': 0}).fillna(0)
    
    df['fecha_diagnostico'] = pd.to_datetime(df['fecha_diagnostico'], errors='coerce')
    daily_cases = df.groupby('fecha_diagnostico').size().reset_index(name='daily_cases')
    daily_deaths = df[df['fallecido'] == 1].groupby('fecha_diagnostico').size().reset_index(name='daily_deaths')
    province_stats = df.groupby('residencia_provincia_nombre').agg({
        'id_evento_caso': 'count',
        'fallecido': 'sum',
        'asistencia_respiratoria_mecanica': 'sum'
    }).rename(columns={'id_evento_caso': 'total_cases'}).reset_index()
    
    df_transformed = daily_cases.merge(daily_deaths, on='fecha_diagnostico', how='left').fillna(0)
    df_transformed['mortality_rate'] = (df_transformed['daily_deaths'] / df_transformed['daily_cases'] * 100).round(2)
    
    output_path = os.path.join('data', 'processed', 'covid_transformed.csv')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_transformed.to_csv(output_path, index=False)
    
    province_path = os.path.join('data', 'processed', 'province_stats.csv')
    province_stats.to_csv(province_path, index=False)
    
    print("Transformation completed")
    return df_transformed, province_stats