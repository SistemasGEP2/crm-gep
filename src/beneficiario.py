import pyodbc
from src.conection.conexion import connect

def beneficiarios_consulta(contrato):
    try:
       
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""select Beneficiarios.NombreBeneficiario,Beneficiarios.PrimerApellido + ' ' + Beneficiarios.SegundoApellido AS Apellidos_Benefeciario,
                                Beneficiarios.Edad,Parentescos.Parentesco
								from Beneficiarios
								inner join Afiliaciones ON Afiliaciones.IdAfiliacion = Beneficiarios.IdAfiliacion
                                inner join parentescos ON Beneficiarios.IdParentesco = Parentescos.IdParentesco
                                inner join Clientes ON Clientes.IdCliente = Beneficiarios.IdCliente
								where Afiliaciones.Contrato = ? or Clientes.Identificacion = ? or Clientes.PrimerNombre like '%' + ? + '%';
                                """,contrato,contrato,contrato)
                results = cursor.fetchall()

                return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None

