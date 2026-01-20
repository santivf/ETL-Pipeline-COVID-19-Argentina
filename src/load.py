from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def load_to_mysql(df_daily, df_province):
    engine = create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
    
    df_daily.to_sql('covid_daily_stats', engine, if_exists='replace', index=False)
    df_province.to_sql('covid_province_stats', engine, if_exists='replace', index=False)
    
    print("Load to MySQL completed")