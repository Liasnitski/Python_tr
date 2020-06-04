from PIL import Image, ImageDraw, ImageFont
from os import listdir
import sys


logo = Image.open("logo.png")
logo = logo.resize((100, 100), Image.ANTIALIAS)
logo.save('logo2.png')

qr = Image.open("qr.png")
qr = qr.resize((100, 100), Image.ANTIALIAS)
qr.save('qr2.png')


 
image = Image.open('test.png')

image = image.transpose(Image.ROTATE_90)

idraw = ImageDraw.Draw(image)
text = "Liasnitski Aliaksandr 04.06.2020"
font = ImageFont.truetype("arial.ttf", 20)
idraw.text((80, 300), text, font=font)

watermark = Image.open('logo2.png')
image.paste(watermark, (290, 10))

qrr = Image.open('qr2.png')
image.paste(qrr, (10, 10))


image.save('test2.png', dpi=(200, 200))

image.show()
