# setup.py
from setuptools import setup, find_packages

setup(
    name="image_processor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",  # Dependência necessária para manipulação de imagens
    ],
    author="Seu Nome",
    author_email="seuemail@example.com",
    description="Um pacote de processamento de imagens simples",
    url="https://github.com/seuusuario/image_processor",  # Repositório GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
