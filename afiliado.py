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
                
        return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    
def consulta_caratula(contrato):
    try:
        #contrato = '5A20293'
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT Afiliaciones.Contrato,Afiliaciones.FechaAfiliacion,Afiliaciones.ValorAfiliacion,Afiliaciones.ValorLetras,Afiliaciones.Cuotas, Instituciones.NombreInstitucion,
                                Clientes.PrimerApellido + ' ' + Clientes.SegundoApellido AS Apellidos,Clientes.PrimerNombre + ' ' + Clientes.SegundNombre AS Nombres,EstadosCiviles.NombreEstadoCivil,TiposdeIdentificacion.NombreTipoIdentificacion,
                                Clientes.Identificacion,Clientes.Fechadenacimiento, Departamentos.NombreDepartamento,Clientes.DireccionResidencia,Clientes.TelefonoResidencia,Clientes.Celular,
                                Clientes.Barrio,Municipios.NombreMunicipio, Departamentos.NombreDepartamento,Clientes.Profesion,Clientes.Email,Clientes.RH,Agentes.NombreAgente as Conferencista
                                from afiliaciones 
                                inner join Clientes ON Afiliaciones.IdCliente = Clientes.IdCliente
                                inner join Instituciones ON Afiliaciones.IdInstitucion = Instituciones.IdInstitucion 
                                inner join EstadosCiviles ON Clientes.IdEstadoCivil = EstadosCiviles.IdEstadoCivil
                                inner join TiposdeIdentificacion ON Clientes.IdTipoIdentificacion = TiposdeIdentificacion.IdTipoIdentificacion
                                inner join Departamentos ON Clientes.IdDepartamentoNac = Departamentos.IdDepartamento
                                inner join Municipios ON Clientes.IdMunicipio = Municipios.IdMunicipio
                                inner join Agentes ON Afiliaciones.IdAgente = Agentes.IdAgente
                                where Afiliaciones.Contrato = ?
                                """,contrato)
                results = cursor.fetchall()

                for i in results: 
                    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23= i
                    print(f"ESTOS SON LOS DATOS DEL DOCUMENTO : " + b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23)
                

                         

                     

        return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
consulta_caratula()
    
