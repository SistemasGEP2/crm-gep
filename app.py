from flask import send_from_directory
from flask import Flask, render_template, request, redirect, url_for, session, send_file,Response
from conexion import servicios,queryHistorico,estadosJuridico,nombreProfesional,actualizacionreasignacion,ldapConnect,afiliacion
from  documentation import contrat, caratula_afiliado
from afiliado import consulta_caratula, afiliacion_bienvenida
import os
from io import BytesIO
from zipfile import ZipFile



from datetime import datetime, time
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import glob

import zipfile


from beneficiario import beneficiarios_consulta

app = Flask(__name__)
app.secret_key = 'supersecretkey_322015#$!asdjfl322015'
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Captura las credenciales del formulario
        username = request.form['username']
        password = request.form['password']
         
        
        # Validar las credenciales contra Active Directory usando ldapConnect
        try:
            estado_conexion = ldapConnect(username, password)
            print(f"esta es la variable{estado_conexion}")

            # Verificar si la conexión fue exitosa
            if estado_conexion == 'Conexión exitosa a Active Directory':
                session['logged_in'] = True
                session['username'] = username
                
                return redirect(url_for('index'))  # Redirige a la página de dashboard si las credenciales son correctas
            else:
                print('Credenciales incorrectas. Por favor, inténtalo nuevamente')
                error = 'Credenciales incorrectas. Por favor, inténtalo nuevamente.'
                return render_template('prueba.html', error=error)

        except Exception as e:
            error = f'Error en la autenticación: {str(e)}'
            return render_template('prueba.html', error=error)

    return render_template('prueba.html')

@app.route('/index')
def index():
    

    try:

        profesional = nombreProfesional()
            
        data = queryHistorico()
        boton = '<a href="/logout" type="button" id="btn-seccion" class="#"><strong>Cerrar Sesión</strong></a>' 
        botondos = '<a href="/psicologia" type="button" id="btn-seccion-false" class="#"><strong>psicologia</strong></a>'
        botontres = '<a href="/" type="button" id="btn-seccion-false" class="#"><strong>Asesor</strong></a>'    

        if 'username' in session:
            nombre = session['username']
            nombre_usuario = nombre.split('.')[0]
            return render_template('index.html', data=data, botondos = botondos, botontres = botontres
                                   ,boton=boton,nombre=nombre_usuario,profesional=profesional)
        else:
            return redirect(url_for('login'))
        # Renderizar la plantilla con los datos
        
    
    except Exception as e:
            print(f'Error: {str(e)}')
            return "Hubo un error  verifique la informción o consulte con un profesional"
    



datos ={}

@app.route('/procesar_busqueda', methods=['POST'])
def procesar_busqueda():
    try:
        if 'username' in session:
            global datos
            numero_afiliacion = request.form['numeroDato']
            print(f'Número de afiliación obtenido: {numero_afiliacion}')
            datosServicios = servicios(numero_afiliacion)
            data = queryHistorico()
            global dato0 
            global dato1 
            global dato2
            global dato3 
            for row in datosServicios: 
                dato0 =datos['dato0'] =row[0]
                dato1 =datos['dato1'] =row[1]
                dato2 =datos['dato2'] =row[2]
                dato3 =datos['dato3'] =row[3]
                update_btn = '<button type="button" id="actualizar-btn"  class="btn btn-success" onclick="actualizarServ();">Actualizar</button>'
            boton = '<a href="/logout" type="button" id="btn-seccion" class="#"><strong>Cerrar Sesión</strong></a>'    
            nombre = session['username']
            nombre_usuario = nombre.split('.')[0]

        else:
            return redirect(url_for('login'))             
        profesional = nombreProfesional()     
        

        return render_template('index.html',data=data,dato0=dato0,dato1=dato1,dato2=dato2,dato3=dato3,update_btn=update_btn,profesional=profesional,nombre=nombre_usuario,boton=boton)

    except Exception as e:
        return "Hubo un error al procesar la búsqueda: " + str(e)


@app.route('/update')
def diccionarios():
    try:
        global datos
        global dato0
        global dato1 
        global dato2
        global dato3
       
        estado = estadosJuridico()
        nombre = nombreProfesional()

        

        return render_template('update.html',estado=estado,nombre=nombre,dato0=dato0,dato1=dato1,dato2=dato2,dato3 = dato3) 
    except Exception as e:
         return "Hubo un error al procesar los diccionarios" + str(e)
    

@app.route('/updateServicios', methods=['POST'])
def actualiserv():
    try:
        estadoSer = request.form.get('estado')
        profesional = request.form.get('proveedor')
        servicio = request.form.get('servicio')
        profesionalAnt = request.form.get('proveedorAnt')
        nombre = session['username']
        

        if estadoSer is None or profesional is None or servicio is None:
            return "Faltan datos necesarios para la actualización", 400
        else:
            datosServicios = actualizacionreasignacion(estadoSer, profesional, servicio,nombre,profesionalAnt)
            if datosServicios:
                return render_template('update.html', datosServicios=datosServicios)
            else:
                return "Error en la actualización de datos", 500

    except Exception as e:
        return "Error al procesar la consulta de actualizar datos: " + str(e), 500


@app.route('/logout')
def logout():
    # esto elimina la sesion que se creo en @app.route(/login)
    session.pop('logged_in',None)
    session.pop('username', None)
    return redirect(url_for('login'))   


@app.route('/welcomeaf', methods=['POST', 'GET'])
def welcomeaf():
    try:
        contrato = None
        consultaraf = ''
        dato1, dato2, dato3, dato4 = None, None, None, None

        btndown = ''

        if request.method == 'POST':
            contrato = request.form.get('contrato')
            fechacont = request.form.get('fechacont')
            print(f"ESTA ES LA FECHA QUE SE ESTA ESCRIBIENDO:: {fechacont}")
            
            
            if contrato is None or not contrato :
                contrato = 0
                consultaraf = afiliacion(contrato,fechacont)
                for row in consultaraf:
                    dato1, dato2, dato3, dato4 = row

                btndown = '<button type="submit" class="btn btn-success donlawn">Descargar</button>'
            elif contrato:
                consultaraf = afiliacion(contrato,fechacont)
                for row in consultaraf:
                    dato1, dato2, dato3, dato4 = row

                btndown = '<button type="submit" class="btn btn-success donlawn">Descargar</button>'

            else:
                print('Error: Vuelva y verifique los datos que está escribiendo')

            

        return render_template('Welcome/Welcome.html',btndown= btndown,contrato=contrato, consultaraf=consultaraf, dato1=dato1, dato2=dato2, dato3=dato3, dato4=dato4)
    except Exception as e:
        return "<p style='color:red;font-size:35px;font-weight: 600; font-family:arial;'> Error: Vuelva y verifique la información. Si el error persiste, contacte con un desarrollador D:</p>" + str(e)




@app.route("/downpdf", methods=['POST', 'GET'])
def downpdf():
    try:


        contratopdf = request.form.get('contratopdf') # on and None
        clausulapdf = request.form.get('clausulapdf')
        tarjetapdf = request.form.get('tarjetapdf')
        brochurepdf = request.form.get('brochurepdf')
        
        contratopordebajo = request.form.get('contratopordebajo')


        


        pdfs = []
 

        consultarpdf2 = afiliacion_bienvenida(contratopordebajo)
        consultarpdf3 = consulta_caratula(contratopordebajo)

        if consultarpdf2 is not None:
            for i in consultarpdf3:
                b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23 = i
                pdf_name = f"Contrato_{b1}.pdf"
                pdf = caratula_afiliado(pdf_name, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, contratopordebajo)
            for i in consultarpdf2:
                a1, a2, a3, a4 = i 
                print(i)               
                pdf_name = f"Contrato_{contratopordebajo}.pdf"
                #pdf = contrat(pdf_name, a2, a1, a3, a4)
                #pdfs.append(pdf_name) esta es la carta de bienvenida por si la piden luego
        if contratopdf == 'on':
            pdfs.append(f"Contrato_{contratopordebajo}.pdf")
        if clausulapdf == 'on':
            pdfs.append("static\\pdf\\Clausulas.pdf")
        if tarjetapdf == 'on':
            pdfs.append("static\\pdf\\Tarjeta_Titular.pdf")
        if brochurepdf == 'on':
            pdfs.append("static\\pdf\\BrochureGEP.pdf")

        else:
            print('listo :D')

        contrato = request.form.get('contrato')
        pdfs = [] 
        consultarpdf2 = afiliacion_bienvenida(contrato)
        if consultarpdf2 is not None:
            for i in consultarpdf2:
                a1, a2, a3, a4 = i
                pdf_name = f"Carta Bienvenida_{a2}.pdf"
                pdf = contrat(pdf_name, a2, a1, a3, a4)
                pdfs.append(pdf_name)
                pdfs.append("static\\pdf\\Tarjeta_Titular.pdf")
                pdfs.append("static\\pdf\\BrochureGEP.pdf")
                pdfs.append(f"Caratula_{contrato}.pdf")

                
          
        if not pdfs:
            return "Error: No se generaron archivos PDF."


        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, 'a') as zip_file:
            for pdf in pdfs:
                # Agrega solo el nombre del archivo al archivo zip
                zip_file.write(pdf, os.path.basename(pdf))

        zip_buffer.seek(0)
        return Response(
            zip_buffer,
            mimetype='application/zip',
            headers={'Content-Disposition': f'attachment;filename={contratopordebajo}.zip'}
        )

    except Exception as e:
        return str(e)


def delete_pdf():
    try:
        # Especifica las horas permitidas para la eliminación (12:01 AM y 12:01 PM)
        allowed_hours = [time(11, 10), time(14,50),time(17,12)]

        # Obtén la hora actual
        current_time = datetime.now().time()
        print(f"Hora actual: {current_time}")
        print(f"Horas permitidas: {allowed_hours}")

        # Verifica si la hora actual está en las horas permitidas
        if any(current_time.hour == allowed_time.hour and current_time.minute == allowed_time.minute for allowed_time in allowed_hours):
            directorio_actual = os.getcwd() #con esta linea de codigo es donde estamos en el directorio actual
            archivos_txt = glob.glob(os.path.join(directorio_actual,'*.pdf')) #por nmedio de glob es que nos ayuda a encontrar la extencion .txt
            for archivo in archivos_txt:
                try:
                    f = open("log.txt","a")
                    print(f.write("\n" + f" >> Archivo eliminado {archivo}"))
                    os.remove(archivo) #recorro todos las rutas que hay con la extencion y las elimino 

                except Exception as eror:
                    return "No se pudo eliminar" + str(eror)

    except Exception as e:
        print(f"Error al eliminar archivos PDF: {str(e)}")

# Configurar un planificador para ejecutar la función cada día a las 12:01 AM y 12:01 PM
scheduler = BackgroundScheduler()
scheduler.add_job(delete_pdf, 'cron', hour='11,14,17', minute=12)
scheduler.start()

# Detener el planificador al cerrar la aplicación Flask
atexit.register(lambda: scheduler.shutdown())

# Ejecutar la función directamente al inicio para probar
delete_pdf()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)