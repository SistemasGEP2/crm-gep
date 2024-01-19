from conexion import connect
import pyodbc

def afiliacion_bienvenida(contrato):
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT 
                                    Afiliaciones.Contrato,ISNULL(Clientes.PrimerNombre, '') + ' ' + ISNULL(Clientes.SegundNombre, '') + ' ' + ISNULL(Clientes.PrimerApellido, '') + ' ' + ISNULL(Clientes.SegundoApellido, '') AS NombreCompleto, Municipios.NombreMunicipio, Departamentos.NombreDepartamento FROM Afiliaciones 
                                INNER JOIN 
                                    Clientes ON Afiliaciones.IdCliente = Clientes.IdCliente
                                INNER JOIN 
                                    Departamentos ON Clientes.IdDepartamentoNac = Departamentos.IdDepartamento
                                INNER JOIN 
                                    Municipios ON Clientes.IdMunicipio = Municipios.IdMunicipio
                                WHERE 
                                    Afiliaciones.Contrato = ?;
                                """,contrato)
                results = cursor.fetchall()

                # Imprimir los resultados en la consola
                for row in results:
                    print(row)

        return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None


        
