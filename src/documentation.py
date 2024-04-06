from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import white, black
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import locale
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from src.afiliado import afiliacion_bienvenida, consulta_caratula
from io import BytesIO
from src.beneficiario import beneficiarios_consulta
from reportlab.pdfbase.pdfdoc import PDFString

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
    locale.setlocale(locale.LC_TIME, 'es_ES.utf-8')
    consulta_bene = beneficiarios_consulta(contrato)
    img = ImageReader('static/img/Caratula_1.jpg')
    pdf_canvas.drawImage(img, 0, 0, width=letter[0], height=letter[1])
    pdf_canvas.setFont("Helvetica-Bold",14)
    pdf_canvas.setFillColor(colors.red)
    contrato_medir = len(b1)
    if contrato_medir <= 5:
        pdf_canvas.drawString(505,652, b1)
    else:
        pdf_canvas.drawString(495,652, b1)
    pdf_canvas.setFont("Helvetica-Bold",6.5)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(37,552, b8)
    pdf_canvas.drawString(266,552, b7)
    pdf_canvas.drawString(180,512,b9)
    pdf_canvas.drawString(497,552,b11) 
    pdf_canvas.drawString(37,471,b18)#MUNICIPIO
    pdf_canvas.drawString(202,471, b13)#DEPARTAMENTO
    pdf_canvas.drawString(367,471,b17)#BARRIO
    pdf_canvas.drawString(320,512,b16)#CELULAR
    pdf_canvas.drawString(462,512,b21)#CORREO
    pdf_canvas.drawString(532,471,b22.upper())#RH
    pdf_canvas.drawString(37,512,b20)
    # pdf_canvas.drawString(456,466,b12)
    pdf_canvas.drawString(37,430,b14)#DIRECCION
    pdf_canvas.drawString(321,430,b6.upper())#INSTITUCION
    pdf_canvas.setFont("Helvetica-Bold",9)
    texto_personalizado_valor = b3
    valor_convertido = str(b3)
    pdf_canvas.drawString(142,336.5,valor_convertido)#VALOR
    cuota_convertido = str(b5)
    pdf_canvas.drawString(498,336.5,cuota_convertido)
    pdf_canvas.drawString(37,336.5,b2)
    pdf_canvas.drawString(249,336.5,b4) #VALOR LETRAS
    beneficiarios_data = consulta_bene
    y_coordinate_datos = 232
    y_coordinate = 245
    url_boton = "https://www.grupoempresarialproteccion.com"
    pdf_canvas.linkURL(url_boton,(580,290,470,320), thickness = 1,  borderColor=colors.blue, textColor=colors.black)
    for row in beneficiarios_data:
        # Convertir el código hexadecimal a RGB
        rgb_color = hex_to_rgb("E6C78C")
        pdf_canvas.setFont("Helvetica-Bold",5.5)
        # Dibujar línea vertical con color RGB
        pdf_canvas.setStrokeColorRGB(*[x/255.0 for x in rgb_color])  # Convertir a rango de 0 a 1
        pdf_canvas.setLineWidth(0.5)
        pdf_canvas.line(27, y_coordinate - 17, 584, y_coordinate - 17)  # Línea horizontal superior
        pdf_canvas.line(27, y_coordinate, 27, y_coordinate - 17)         # Línea vertical izquierda
        pdf_canvas.line(585, y_coordinate, 585, y_coordinate - 17)     # Línea vertical derecha
        pdf_canvas.drawString(50, y_coordinate_datos, row[0] if row[0] else "")
        pdf_canvas.drawString(177, y_coordinate_datos, row[1] if row[1] else "")
        pdf_canvas.drawString(372, y_coordinate_datos, str(row[2]) if row[2] else "")
        pdf_canvas.drawString(515, y_coordinate_datos, str(row[3]) if row[3] else "")
        y_coordinate_datos -= 17
        y_coordinate -= 17

    pdf_canvas.showPage()
    # firma = ImageReader('static/img/Firma_Caratula.jpg')
    # pdf_canvas.drawImage(firma,0,600,250,150)
    # Guardar el PDF con todas las páginas
    caratula_firma = ImageReader('static/img/Caratula_firma.jpg')
    pdf_canvas.drawImage(caratula_firma, 0, 0, width=letter[0], height=letter[1])
    pdf_canvas.save()
    pdf_buffer.seek(0)

    with open(pdf_file, 'wb') as f:
        f.write(pdf_buffer.read())