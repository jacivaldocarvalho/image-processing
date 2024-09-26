# Image Processor

Um pacote Python para processamento básico de imagens, incluindo conversão para escala de cinza e combinação de duas imagens.

## Instalação

Para instalar o pacote, use o pip:

```bash
pip install image-processor

```

## Funcionalidades

- to_grayscale(image_path): Converte uma imagem para escala de cinza;
- combine_images(image_path1, image_path2): Combina duas imagens usando uma média.

## Uso

``` python
from image_processor.processing import to_grayscale, combine_images

# Converter imagem para escala de cinza
gray_image = to_grayscale('path/to/image.jpg')

# Combinar duas imagens
combined_image = combine_images('path/to/image1.jpg', 'path/to/image2.jpg')
```
## Testes
Para executar os testes, utilize:

```bash
python -m unittest discover tests/
```
## Contribuições
Sinta-se à vontade para contribuir. Faça um fork do projeto, crie uma branch para suas alterações e envie um pull request.


