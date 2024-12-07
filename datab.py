import pyodbc as odbc

con_str = (
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-QB8L5VP\SQLEXPRESS;'
    'DATABASE=Test;'
)

conn = odbc.connect(con_str)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Test.dbo.SP")
for row in cursor:
    print(row)


