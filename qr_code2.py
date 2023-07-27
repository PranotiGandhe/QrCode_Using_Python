import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )

qr.add_data("https://github.com/PranotiGandhe")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow", back_color="turquoise")
img.save("Github_Qrcode_color.png")

