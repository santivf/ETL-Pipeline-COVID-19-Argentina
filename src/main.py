from extract import extract_covid_data
from transform import transform_covid_data
from load import load_to_mysql
from report import generate_report

if __name__ == "__main__":
    df_raw = extract_covid_data()
    df_daily, df_province = transform_covid_data(df_raw)
    load_to_mysql(df_daily, df_province)
    generate_report(df_daily, df_province)