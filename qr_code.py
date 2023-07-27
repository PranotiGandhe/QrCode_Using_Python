import qrcode as qr
img = qr.make("https://github.com/PranotiGandhe")
img.save("Github_Qrcode.png")