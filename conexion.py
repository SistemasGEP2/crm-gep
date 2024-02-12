import pyodbc
from ldap3 import Server, Connection, ALL
from flask import Flask, jsonify,redirect, url_for,render_template
import datetime





def connect():
    server = '192.168.1.175'
    database = 'Afiliaciones'
    username = 'GEP'
    password = 'GEP322015'

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    return pyodbc.connect(connection_string)



    

def servicios(numero_afiliacion):
    try:
        # Especificaciones del servidor al que me voy a conectar
        server = '192.168.1.175'
        database = 'Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'

        # Sintaxis para conexión a SQL Server
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establecer la conexión
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute(f' SELECT CasosClientes.IdCaso, Proveedores.Nombre,Estados.Estado,Proveedores.IdProveedor FROM CasosClientes INNER JOIN Proveedores ON CasosClientes.IdProveedor = Proveedores.IdProveedor INNER JOIN  Estados ON CasosClientes.IdEstado = Estados.IdEstado where  CasosClientes.IdCaso = {numero_afiliacion};')

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    
def queryHistorico():
    try:
       
        server = '192.168.1.175'
        database = 'Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'

        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute('SELECT  History_Reasig.IdCaso,History_Reasig.usuario,History_Reasig.query,History_Reasig.feha,ProveedoresAnt.Nombre AS ProfesionalAnt,ProveedoresFin.Nombre AS ProfesionalFin FROM History_Reasig INNER JOIN Proveedores AS ProveedoresAnt ON ProveedoresAnt.IdProveedor = History_Reasig.IdProveedorAnt INNER JOIN Proveedores AS ProveedoresFin ON ProveedoresFin.IdProveedor = History_Reasig.IdProveedor;')
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    

def estadosJuridico():
    try:
        server = '192.168.1.175'
        database = 'Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Estados where IdEspecialidad = 2;')
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except Exception as e:
        print(f'Error en la consulta estados a la base de datos: {str(e)}')
        return None


def nombreProfesional():
    try:
        server='192.168.1.175'
        database ='Afiliaciones'
        username='GEP'
        password = 'GEP322015'
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection =pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute('SELECT Proveedores.IdProveedor, Proveedores.Nombre FROM Proveedores where IdEspecialidad = 2 AND Activo = 1;')
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except Exception as e:
        print(f'Error en la consulta de los profecionales a la base de datos: {str(e)}')
        return None
    

def actualizacionreasignacion(estadoSer,profesional,servicio,nombre,profesionalAnt): 
    try:
        #un actualizar es diferente a una consulta por que no va a mostrar ninguna columna seleccionada
        server='192.168.1.175'
        database='Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        fecha_hora_actual = datetime.datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        cursor.execute('UPDATE CasosClientes SET IdEstado = ?, IdProveedor = ? WHERE IdCaso = ?;',
               (estadoSer, profesional, servicio)) #Se pasan los parametros de la función  en una tupla y en la consulta se llaman por orden de ? y por medio del metodo set, 
        cursor.execute("Insert Into Evoluciones (IdCaso,Evolucion,IdEstado,fecha,IdUsuario) values (?,?,?,?,?);",
                        (servicio,f"SERVICIO REASIGNADO",estadoSer,fecha_hora_formateada,"246"))      
           # Consulta para insertar en la tabla History_Reasig
        cursor.execute("INSERT INTO History_Reasig (query,usuario, feha, IdCaso, IdProveedorAnt, IdProveedor) VALUES (?,?, ?,?,?,?);",
                       ("REASIGNADO",nombre,fecha_hora_formateada,servicio,profesionalAnt,profesional))

        connection.commit()
        cursor.close()
        connection.close()
        return "Actualizacion exitoza de la base de datos"
    except Exception as e:
        print(F"Error en la consulta de la actualizacion en la base de datos: {str(e)}")
        return None


def ldapConnect(username, password):
    try:
        print(username,password)
        # Configuración para la conexión a Active Directory
        ldap_server = '192.168.1.50' 
        ldap_user = f'gepdc\\{username}'  
        ldap_password = password  

        # Establecer la conexión con Active Directory
        server = Server(ldap_server, get_info=ALL)
        conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

        # Verificar si la conexión fue exitosa
        if conn.bound:
            print('Conexión exitosa a Active Directory')
            return 'Conexión exitosa a Active Directory'
        else:
            print('Falló la conexión a Active Directory')
            return 'Falló la conexión a Active Directory'

    except Exception as e:
        return f'Error en la conexión Active Directory: {str(e)}'
    
def afiliacion(dato1,fechacont):
    try:
        # Especificaciones del servidor al que me voy a conectar
        server = '192.168.1.175'
        database = 'Afiliaciones'
        username = 'GEP'
        password = 'GEP322015'

        # Sintaxis para conexión a SQL Server
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establecer la conexión
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        if fechacont == None or not fechacont:
            complemento = ""
        else:
            complemento = f"or Afiliaciones.FechaAfiliacion = '{fechacont}'"
        cursor.execute(f"Select Clientes.PrimerNombre,Clientes.PrimerApellido,Clientes.Identificacion,Afiliaciones.Contrato,Clientes.Email from Clientes inner join Afiliaciones On Clientes.IdCliente = Afiliaciones.IdCliente where Clientes.Identificacion ='{dato1}' or Afiliaciones.Contrato ='{dato1}' or Clientes.PrimerNombre like '%{dato1}%'  or Clientes.PrimerApellido = '{dato1}' {complemento}  ")

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None

