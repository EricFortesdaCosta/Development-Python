import qrcode
imagem = qrcode.make("https://docs.google.com/document/d/1ZRFb_wAqgzrgqY1eUdrgsoYQO1rts9FqFR-Jh2IxWVY/edit")

imagem.save("QRcodegerado.png") 