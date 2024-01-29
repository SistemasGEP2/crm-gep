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
    date = current_date_and_time.strftime('%d de %B de %Y')
    print(date)
    c = canvas.Canvas(nombre_documento,pagesize=(612, 792))

    nombre_afiliado = nombre_afiliado
    # Comentar la línea de la imagen para probar sin ella
    imagen = ImageReader('./static/img/fondo.png')
    imagen2 = ImageReader('./static/img/firma.png')
    c.setFont("Helvetica-Bold", 12)

    # Comentar la línea de la imagen para probar sin ella
    c.drawImage(imagen, 0, 0, width=612, height=792)
    # c.drawString(100, 750, "Hola esto es un pdf de prueba :D")
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
    c.drawString(95, 80, "AREA CORRESPONDENCIA")
    c.drawImage(imagen2, 92, 98, width=120, height=65)

    c.save()
def hex_to_rgb(hex_color):
    # Convertir el código hexadecimal a componentes RGB
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def caratula_afiliado(pdf_file, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, contrato):
    pdf_buffer = BytesIO()
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
    consulta_bene = beneficiarios_consulta(contrato)  
    img = ImageReader('static/img/Caratula_1.jpg')
    pdf_canvas.drawImage(img, 0, 0, width=letter[0], height=letter[1])
    pdf_canvas.setFont("Helvetica-Bold",12)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(512,569, b1)
    pdf_canvas.setFont("Helvetica-Bold",8)
    pdf_canvas.drawString(99,503, b8)
    pdf_canvas.drawString(215,503, b7)
    pdf_canvas.drawString(458,503,b9)
    pdf_canvas.drawString(354,503,b11) 
    pdf_canvas.drawString(22,468,b18)
    pdf_canvas.drawString(215,468, b13)
    pdf_canvas.drawString(354,468,b17)
    pdf_canvas.drawString(457,468,b16)
    pdf_canvas.drawString(22,432,b21.upper())
    pdf_canvas.drawString(355,432,b22.upper())
    pdf_canvas.drawString(215,432,b20)
    pdf_canvas.drawString(456,432,b12)
    pdf_canvas.drawString(22,395,b14)
    pdf_canvas.drawString(353,395,b6.upper())
    texto_personalizado_valor = b3
    valor_convertido = str(b3)
    pdf_canvas.drawString(262,342.5,valor_convertido)
    cuota_convertido = str(b5)
    pdf_canvas.drawString(362,342.5,cuota_convertido)
    pdf_canvas.drawString(175,342.5,b2)
    pdf_canvas.drawString(450,342.5,b4)
    beneficiarios_data = consulta_bene
    y_coordinate_datos = 211.5
    y_coordinate = 221.9

    for row in beneficiarios_data:
        # Convertir el código hexadecimal a RGB
        rgb_color = hex_to_rgb("F28A31")
        pdf_canvas.setFont("Helvetica-Bold",7)
        # Dibujar línea vertical con color RGB
        pdf_canvas.setStrokeColorRGB(*[x/255.0 for x in rgb_color])  # Convertir a rango de 0 a 1
        pdf_canvas.setLineWidth(0.5)
        pdf_canvas.line(16, y_coordinate - 17, 596, y_coordinate - 17)  # Línea horizontal superior
        pdf_canvas.line(16, y_coordinate, 16, y_coordinate - 17)         # Línea vertical izquierda
        pdf_canvas.line(596, y_coordinate, 596, y_coordinate - 17)     # Línea vertical derecha

        pdf_canvas.drawString(52, y_coordinate_datos, row[0]) 
        pdf_canvas.drawString(208, y_coordinate_datos, row[1])
        pdf_canvas.drawString(390, y_coordinate_datos, str(row[2]))
        pdf_canvas.drawString(523, y_coordinate_datos, str(row[3]))
        y_coordinate_datos -= 17
        y_coordinate -= 17 
     
    # Guardar el PDF con todas las páginas
    pdf_canvas.save()
    pdf_buffer.seek(0)

    with open(pdf_file, 'wb') as f:
        f.write(pdf_buffer.read())