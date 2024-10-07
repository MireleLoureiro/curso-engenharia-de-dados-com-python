# core.py
from PIL import Image, ImageFilter

def load_image(path):
    """Carrega uma imagem a partir de um caminho."""
    try:
        image = Image.open(path)
        return image
    except IOError as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None

def resize_image(image, size):
    """Redimensiona a imagem para um determinado tamanho."""
    return image.resize(size)

def apply_filter(image, filter_type):
    """Aplica um filtro à imagem."""
    filters = {
        'BLUR': ImageFilter.BLUR,
        'CONTOUR': ImageFilter.CONTOUR,
        'DETAIL': ImageFilter.DETAIL,
    }
    if filter_type in filters:
        return image.filter(filters[filter_type])
    else:
        print(f"Filtro '{filter_type}' não reconhecido.")
        return image
