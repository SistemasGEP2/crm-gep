import pyodbc
from conexion import connect

def beneficiarios_consulta(contrato):
    try:
       
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""select Beneficiarios.NombreBeneficiario,Beneficiarios.PrimerApellido + ' ' + Beneficiarios.SegundoApellido AS Apellidos_Benefeciario,
                                Beneficiarios.FechaNacimiento,Beneficiarios.Edad,Parentescos.Parentesco
								from Beneficiarios
								inner join Afiliaciones ON Afiliaciones.IdAfiliacion = Beneficiarios.IdAfiliacion
                                inner join parentescos ON Beneficiarios.IdParentesco = Parentescos.IdParentesco
								where Afiliaciones.Contrato = ?;
                                """,contrato)
                results = cursor.fetchall()
                return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None

