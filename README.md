# ETL-Pipeline-COVID-19-Argentina

ETL pipeline for historical COVID-19 cases in Argentina (2020-2022).

## Features
- **Extract**: Automatic download + unzip from official Ministry of Health ZIP
- **Transform**: Clean dates, daily cases/deaths, mortality rate, province stats with pandas
- **Load**: MySQL tables (daily stats + province stats)
- **Report**: Key metrics + evolution plot (matplotlib)

## Dataset
- Source: Official Argentina Ministry of Health (automatic download from https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.zip)
- Fields: id_evento_caso, sexo, edad, residencia_provincia_nombre, fecha_diagnostico, fallecido, etc.

## Tools
- Python
- Pandas
- Requests (download ZIP)
- SQLAlchemy + PyMySQL
- Matplotlib
- Docker

## Setup MySQL local
- Install MySQL Community
- Create DB `covid_argentina`
- Config .env credentials

## How to Run
1. Clone repo

2. pip install -r requirements.txt

3. Config .env

4. python src/main.py

Docker:

docker build -t etl-covid-argentina

docker run --env-file .env etl-covid-argentina
