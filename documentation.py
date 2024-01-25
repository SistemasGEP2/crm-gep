from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import white, black
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import locale
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from afiliado import afiliacion_bienvenida, consulta_caratula
from io import BytesIO
from beneficiario import beneficiarios_consulta

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


def caratula_afiliado(contrato):
    pdf_file = "Caratula_Afiliacion.pdf"
    pdf_buffer = BytesIO()
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)

    caratula_paths = [
        'static/img/Caratula_1.jpg',
        'static/img/Caratula_2.jpg',
        'static/img/Caratula_3.jpg',
    ]

    carat = consulta_caratula(contrato)
    consulta_bene = beneficiarios_consulta(contrato)

    for i, caratula_path in enumerate(caratula_paths, start=1):
        
        if i > 1:
            pdf_canvas.showPage()

        # Cargar la imagen y obtener sus dimensiones
        caratula = ImageReader(caratula_path)
        caratula_width, caratula_height = caratula.getSize()
        row = []
        # Dibujar la imagen en la página
        pdf_canvas.drawImage(caratula_path, 0, 0, width=letter[0], height=letter[1])
        if i <= min(len(carat), len(consulta_bene)) and carat and consulta_bene:
            #row_beneficiario = consulta_bene[0]
            
            
            
            b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23 = carat[i-1]
        pdf_canvas.setFont("Helvetica", 11)
        pdf_canvas.setFillColor(colors.black) 
        if i == 1:
            
            texto_personalizado_contrato = b1
            pdf_canvas.drawString(525, 561, texto_personalizado_contrato)
            texto_personalizado_nombres = b8
            pdf_canvas.drawString(99,480, texto_personalizado_nombres)
            texto_personalizado_apellidos = b7
            pdf_canvas.drawString(215,480, texto_personalizado_apellidos)
            texto_personalizado_estadocivil = b9
            pdf_canvas.drawString(352,480,texto_personalizado_estadocivil)
            texto_personalizado_identificacion = b11
            pdf_canvas.drawString(456,480,texto_personalizado_identificacion) 
            texto_personalizado_direccionresi = b14
            pdf_canvas.drawString(20,362,texto_personalizado_direccionresi)
            texto_personalizado_municipio = b18
            pdf_canvas.drawString(20,440,texto_personalizado_municipio)
            texto_personalizado_departamento = b13
            pdf_canvas.drawString(215,440, texto_personalizado_departamento)
            texto_personalizado_barrio = b17
            pdf_canvas.drawString(350,440,texto_personalizado_barrio)
            texto_personalizado_celular = b16
            pdf_canvas.drawString(456,440,texto_personalizado_celular)
            texto_personalizado_email = b21
            pdf_canvas.drawString(20,400,texto_personalizado_email)
            texto_personalizado_rh = b22
            pdf_canvas.drawString(215,400,texto_personalizado_rh)
            texto_personalizado_profesion = b20
            pdf_canvas.drawString(350,400,texto_personalizado_profesion)
            texto_personalizado_fechanaci = b12
            pdf_canvas.drawString(456,400,texto_personalizado_fechanaci)
            texto_personalizado_institucion = b6
            pdf_canvas.drawString(350,362,texto_personalizado_institucion)
            texto_personalizado_valor = b3
            valor_convertido = str(b3)
            pdf_canvas.drawString(277,313,valor_convertido)
            texto_personalizado_cuotas = b5
            cuota_convertido = str(b5)
            pdf_canvas.drawString(216,313,cuota_convertido)
            texto_personalizado_fechaafilia = b2
            pdf_canvas.drawString(108,313,texto_personalizado_fechaafilia)
            texto_personalizado_valorletras = b4
            pdf_canvas.drawString(400,313, texto_personalizado_valorletras)
            beneficiarios_data = consulta_bene
            y_coordinate = 160
            for row in beneficiarios_data:
             pdf_canvas.drawString(25, y_coordinate, row[0])
             pdf_canvas.drawString(132, y_coordinate, row[1])
             pdf_canvas.drawString(290, y_coordinate, str(row[2]))
             pdf_canvas.drawString(422, y_coordinate, str(row[3]))
             pdf_canvas.drawString(516, y_coordinate, row[4])
             y_coordinate -= 20 

            
            
                
        elif i == 3:
                texto_personalizado = f"Texto personalizado para hoja {i}: {b21}"
    # Guardar el PDF con todas las páginas
    pdf_canvas.save()
    pdf_buffer.seek(0)

    with open(pdf_file, 'wb') as f:
        f.write(pdf_buffer.read())







