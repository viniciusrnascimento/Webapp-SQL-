import os
from sqlalchemy import create_engine, text

conn_str = os.getenv("DefaultConnection")

conn_str = conn_str.replace(";", ";;")

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

def get_date_from_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT GETDATE()"))
            row = result.fetchone()
            return row[0]
    except Exception as e:
        return f"Erro ao conectar ao SQL: {str(e)}"
