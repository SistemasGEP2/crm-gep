from src.conection.conexion import connect
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
                                    Afiliaciones.Contrato = ? or Clientes.Identificacion = ? or Clientes.PrimerNombre like ?;
                                """,contrato,contrato,contrato)
                results = cursor.fetchall()

                # Imprimir los resultados en la consola
                
        return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
    
def consulta_caratula(contrato):
    try:
        
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
        return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None

class afiliado:
    def __init__(self,pri_nom,seg_nom,pri_ape,seg_ape,contrato,fechacont):
            self.pri_nom = pri_nom
            self.seg_nom = seg_nom
            self.pri_ape = pri_ape
            self.seg_ape = seg_ape
            self.contrato = contrato
            self.fechacont = fechacont
    

    #metodo para listar el afiliado
    def listarafiliado(self,contrato,fechacont):
        #conexion a la base de datos
        try:
            with connect() as connection:
                with connection.cursor() as cursor:
                    if fechacont == None or not fechacont:
                        complemento = ""
                    else:
                        complemento = f"or Afiliaciones.FechaAfiliacion = '{fechacont}'"
                    cursor.execute(f"Select Clientes.PrimerNombre,Clientes.PrimerApellido,Clientes.Identificacion,Afiliaciones.Contrato,Clientes.Email from Clientes inner join Afiliaciones On Clientes.IdCliente = Afiliaciones.IdCliente where Clientes.Identificacion ='{contrato}' or Afiliaciones.Contrato ='{contrato}' or Clientes.PrimerNombre like '%{contrato}%'  or Clientes.PrimerApellido = '{contrato}' {complemento}  ")
                    results = cursor.fetchall()
                    return results

        except Exception as e:
            print(f'Error en la consulta a la base de datos: {str(e)}')
            return None


    
