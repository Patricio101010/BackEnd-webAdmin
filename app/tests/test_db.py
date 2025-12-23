import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PMORALES1;"
    "DATABASE=FinanzasPersonalesDB;"
    "UID=sa;"
    "PWD=*sa"
)
print("Conexión exitosa")
conn.close()

