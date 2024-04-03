from src.conection.conexion import connect
class historial:
    def __init__(self,nombre):
        self.nombre = nombre



    def insertarHistoricoReasignacion(self):
        try:
            with connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT  History_Reasig.IdCaso,History_Reasig.usuario,History_Reasig.query,History_Reasig.feha,ProveedoresAnt.Nombre AS ProfesionalAnt,ProveedoresFin.Nombre AS ProfesionalFin FROM History_Reasig INNER JOIN Proveedores AS ProveedoresAnt ON ProveedoresAnt.IdProveedor = History_Reasig.IdProveedorAnt INNER JOIN Proveedores AS ProveedoresFin ON ProveedoresFin.IdProveedor = History_Reasig.IdProveedor WHERE idtipo=1;')
                    results = cursor.fetchall()
                    return results
        except Exception as e:
            print(f'Error en la consulta a la base de datos: {str(e)}')
            return None