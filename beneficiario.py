from conexion import connect
import pyodbc



def beneficiarios_consulta():
    try:
        contrato = '5A20293'
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

                matrix = []

                for row in results:
                    print(len(row))
                    for element in row:
                        print(element, end=' ')
                
                    dato1, dato2, dato3, dato4, dato5 = row

                
                for row in matrix:
                    for element in row:
                     print(element, end=' ')
                
                matrix_dato1, matrix_dato2, matrix_dato3, matrix_dato4, matrix_dato5 = row
                

                
                datos_variables = {}

                
                for index, row in enumerate(results, start=1):
                    
                    nombre_variable = f'dato_{index}'

                    
                    datos_variables[nombre_variable] = row

                    
                    print(f'{nombre_variable}: {datos_variables}')

                

                return results
    except pyodbc.Error as e:
        print(f'Error en la consulta a la base de datos: {str(e)}')
        return None
beneficiarios_consulta()