from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import white, black
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import locale
from afiliado import afiliacion_bienvenida, consulta_caratula

def contrat(nombre_documento, nombre_afiliado, numero_contrato, departamento, ciudad):
 

    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
    current_date_and_time = datetime.datetime.now()
    date = current_date_and_time.strftime('%w de %B de %Y')
    print(date)
    c = canvas.Canvas(nombre_documento,pagesize=(612, 792))

    nombre_afiliado = nombre_afiliado
    # Comentar la línea de la imagen para probar sin ella
    imagen = ImageReader('./static/img/fondo.png')
    c.setFont("Helvetica-Bold", 12)

    # Comentar la línea de la imagen para probar sin ella
    c.drawImage(imagen, 0, 0, width=612, height=792)
    c.drawString(100, 750, "Hola esto es un pdf de prueba :D")
    x, y = 432, 598
    ancho, alto = 30, 92
    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(0, 0, 0)
    c.rect(x, y, alto, ancho, stroke=True, fill=True)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(440, 609, f"AFL. {numero_contrato}")
    c.drawString(91, 535, "Señor(a)")
    c.drawString(91, 520, nombre_afiliado)
    c.drawString(91, 503, f"{departamento} - {ciudad}")
    c.setFont("Helvetica", 12)
    c.drawString(91, 587, f"Bogotá D.C., {date}")
    c.drawString(91, 455, "Es  de   gran importancia   para   nuestra  organizacón  darle  la   mas  calurosa")
    c.drawString(91, 440, "bienvenida como  afiliado(a) al servicio de  previsión que usted ha adquirido con")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(91, 424, "GRUPO EMPRESARIAL PROTECCIÓN S.A.S.")
    c.setFont("Helvetica", 12)
    c.drawString(91, 393, "Adjunto a esta encuentra:")
    c.drawString(105, 360, "•    Contrato de prestación de servicios,  el cual  sugerimos  mantener  en  un")
    c.drawString(105, 345, "     lugar donde facilite su ubicación y evite su deterioro.")
    c.drawString(105, 318, "•    Tarjeta  con los datos de la  empresa para  cualquier  emergencia, la cual")
    c.drawString(105, 303, "     debe  portar como un  documento mas.")
    c.drawString(105, 276, "•    Guía de Servicios")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(91, 250, "Para prestarle  un mejor  servicio agradecemos mantener actualizados sus")
    c.drawString(91, 235, "datos personales,  en caso que estos  presenten alguna modificación.")
    c.setFont("Helvetica", 12)
    c.drawString(95, 195, "Atentamente,")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(95, 80, "AREA DE SISTEMAS")

    c.save()


def caratula_afiliado(contrato_caratula,fechaafiliacion_caratula,valorafiliacion_caratula,valorletras_caratula,cuotas_caratula,institucion_caratula,apellidos_caratula,nombres_caratula,estadocivil_caratula,tipoidentificacion_caratula,identificacion_caratula,fechanacimiento_caratula,departamento_caratula,direccionresidencia_caratula,telefono_residencia,celular_caratula,barrio_caratula,municipio_caratula,profesion_caratula,correo_caratula,rh_caratula,apellidosbeneficiario_caratula,nombrebeneficiario_caratula,edadbeneficiario_caratula,fechanacimientobeneficiario_caratula,parentescobeneficiario_caratula,conferencista_caratula):
    pdf_file = "Caratula Afiliacion.pdf"
    pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)
    
    carat = consulta_caratula()
    for i in carat:
        contrato_caratula,fechaafiliacion_caratula,valorafiliacion_caratula,valorletras_caratula,cuotas_caratula,institucion_caratula,apellidos_caratula,nombres_caratula,estadocivil_caratula,tipoidentificacion_caratula,identificacion_caratula,fechanacimiento_caratula,departamento_caratula,direccionresidencia_caratula,telefono_residencia,celular_caratula,barrio_caratula,municipio_caratula,profesion_caratula,correo_caratula,rh_caratula,apellidosbeneficiario_caratula,nombrebeneficiario_caratula,edadbeneficiario_caratula,fechanacimientobeneficiario_caratula,parentescobeneficiario_caratula,conferencista_caratula = i
        print(i)
    # Rutas de las imágenes
    caratula_paths = [
        'static/img/Caratula_1.jpg',
        'static/img/Caratula_2.jpg',
        'static/img/Caratula_3.jpg',
    ]
    pdf_canvas.drawString(95,270,f"{nombres_caratula}")
    pdf_canvas.drawString(91,235, f"{contrato_caratula}")
    # Iterar sobre las imágenes y agregar cada una a una página diferente
    for i, caratula_path in enumerate(caratula_paths, start=1):
        # Saltar a una nueva página para cada imagen después de la primera
        if i > 1:
            pdf_canvas.showPage()

        # Cargar la imagen y obtener sus dimensiones
        caratula = ImageReader(caratula_path)
        caratula_width, caratula_height = caratula.getSize()

        # Dibujar la imagen en la página
        pdf_canvas.drawImage(caratula_path, 0, 0, width=letter[0], height=letter[1])

    # Guardar el PDF con todas las páginas
    pdf_canvas.save()



