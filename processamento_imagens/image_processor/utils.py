# utils.py
def convert_to_grayscale(image):
    """Converte a imagem para escala de cinza."""
    return image.convert('L')

def rotate_image(image, degrees):
    """Roda a imagem por um número específico de graus."""
    return image.rotate(degrees)
