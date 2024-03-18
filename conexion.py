import pyodbc

def connect():
    try:
        server = '192.168.1.175'
        database = 'Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'

        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        return pyodbc.connect(connection_string)
        
    except Exception as e:
        return f"Hay un error en la conexion {e}"