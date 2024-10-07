# process_image.py

from image_processor import load_image, resize_image, convert_to_grayscale

# Carregar uma imagem
img = load_image("caminho/para/imagem.jpg")

# Redimensionar a imagem
resized_img = resize_image(img, (200, 200))

# Converter para escala de cinza
gray_img = convert_to_grayscale(resized_img)

# Salvar a imagem
gray_img.save("imagem_processada.jpg")
