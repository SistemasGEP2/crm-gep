import datetime
from src.conection.conexion import connect

def servicios(numero_afiliacion):
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f' SELECT CasosClientes.IdCaso, Proveedores.Nombre,Estados.Estado,Proveedores.IdProveedor FROM CasosClientes INNER JOIN Proveedores ON CasosClientes.IdProveedor = Proveedores.IdProveedor INNER JOIN  Estados ON CasosClientes.IdEstado = Estados.IdEstado where  CasosClientes.IdCaso = {numero_afiliacion};')
                results = cursor.fetchall()
                return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    
def queryHistorico():
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT  History_Reasig.IdCaso,History_Reasig.usuario,History_Reasig.query,History_Reasig.feha,ProveedoresAnt.Nombre AS ProfesionalAnt,ProveedoresFin.Nombre AS ProfesionalFin FROM History_Reasig INNER JOIN Proveedores AS ProveedoresAnt ON ProveedoresAnt.IdProveedor = History_Reasig.IdProveedorAnt INNER JOIN Proveedores AS ProveedoresFin ON ProveedoresFin.IdProveedor = History_Reasig.IdProveedor WHERE idtipo=1;')
                results = cursor.fetchall()
                return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    

def estadosJuridico():
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM Estados where IdEspecialidad = 2;')
                results = cursor.fetchall()
                return results
    except Exception as e:
        print(f'Error en la consulta estados a la base de datos: {str(e)}')
        return None


def nombreProfesional():
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT Proveedores.IdProveedor, Proveedores.Nombre FROM Proveedores where IdEspecialidad = 2 AND Activo = 1;')
                results = cursor.fetchall()
                return results
    except Exception as e:
        print(f'Error en la consulta de los profecionales a la base de datos: {str(e)}')
        return None
    

def actualizacionreasignacion(estadoSer,profesional,servicio,nombre,profesionalAnt): 
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                fecha_hora_actual = datetime.datetime.now()
                fecha_hora_formateada = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                cursor.execute('UPDATE CasosClientes SET IdEstado = ?, IdProveedor = ? WHERE IdCaso = ?;',
                    (estadoSer, profesional, servicio)) #Se pasan los parametros de la función  en una tupla y en la consulta se llaman por orden de ? y por medio del metodo set, 
                cursor.execute("Insert Into Evoluciones (IdCaso,Evolucion,IdEstado,fecha,IdUsuario) values (?,?,?,?,?);",
                                (servicio,f"SERVICIO REASIGNADO",estadoSer,fecha_hora_formateada,"246"))      
                # Consulta para insertar en la tabla History_Reasig
                cursor.execute("INSERT INTO History_Reasig (query,usuario, feha, IdCaso, IdProveedorAnt, IdProveedor,idtipo) VALUES (?,?, ?,?,?,?,);",
                            ("REASIGNADO",nombre,fecha_hora_formateada,servicio,profesionalAnt,profesional,1))

                connection.commit()
                return "Actualizacion exitoza de la base de datos"
    except Exception as e:
        print(F"Error en la consulta de la actualizacion en la base de datos: {str(e)}")
        return None



    
def afiliacion(dato1,fechacont):
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                if fechacont == None or not fechacont:
                    complemento = ""
                else:
                    complemento = f"or Afiliaciones.FechaAfiliacion = '{fechacont}'"
                cursor.execute(f"Select Clientes.PrimerNombre,Clientes.PrimerApellido,Clientes.Identificacion,Afiliaciones.Contrato,Clientes.Email from Clientes inner join Afiliaciones On Clientes.IdCliente = Afiliaciones.IdCliente where Clientes.Identificacion ='{dato1}' or Afiliaciones.Contrato ='{dato1}' or Clientes.PrimerNombre like '%{dato1}%'  or Clientes.PrimerApellido = '{dato1}' {complemento}  ")
                results = cursor.fetchall()
                return results
    except Exception as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None

