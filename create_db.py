import pandas as pd
import getpass
from sqlalchemy import create_engine, text

def save_dataframes_to_db(participating_client_df, clean_demo_df, session_deduplicated_web_data_df):
    password = getpass.getpass()
    db_name = "vanguard"

    # Connect to MySQL server (no DB)
    engine_root = create_engine(f'mysql+pymysql://root:{password}@localhost')

    # Create DB if needed
    with engine_root.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name};"))

    # Connect to the new DB
    engine = create_engine(f'mysql+pymysql://root:{password}@localhost/{db_name}')

    # Upload tables
    participating_client_df.to_sql("experiment", con = engine, if_exists="replace", index=False)
    clean_demo_df.to_sql("demo", con = engine, if_exists="replace", index=False)
    session_deduplicated_web_data_df.to_sql("session", con = engine, if_exists="replace", index=False)
