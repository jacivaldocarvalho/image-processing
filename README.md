# PROCESSADOR DE IMAGENS

Um pacote Python para processamento básico de imagens, incluindo conversão para escala de cinza e combinação de duas imagens.

## Índice

- [PROCESSADOR DE IMAGENS](#processador-de-imagens)
  - [Índice](#índice)
  - [Estrutura do Repositório](#estrutura-do-repositório)
  - [Instalação](#instalação)
  - [Funcionalidades](#funcionalidades)
  - [Uso](#uso)
  - [Testes](#testes)
  - [Contribuições](#contribuições)
  - [Licenciamento](#licenciamento)
  - [Autor](#autor)

## Estrutura do Repositório

````
image_processor/
│
├── image_processor/
│   ├── __init__.py
│   ├── processing_image.py
│
├── tests/
│   ├── __init__.py
│   ├── test_processing.py
│
├── README.md
├── setup.py
└── requirements.txt
````

## Instalação

Para instalar o pacote, use o pip:

```bash
pip install image_processor_jr
```

## Funcionalidades

- to_grayscale(image_path, save_path=None): Converte uma imagem para escala de cinza;
- combine_images(image_path1, image_path2, save_path=None): Combina duas imagens usando uma média.

## Uso

``` python
from image_processor_jr.processing_image import to_grayscale, combine_images

# Caminhos das imagens
caminho_imagem1 = 'imagem1.jpg'
caminho_imagem2 = 'imagem2.jpg'
caminho_gray = 'imagem_gray.jpg'
caminho_combinada = 'imagem_combinada.jpg'

# Converter a primeira imagem para escala de cinza e salvar
print("Convertendo a imagem para escala de cinza...")
to_grayscale(caminho_imagem1, save_path=caminho_gray)

# Combinar as duas imagens e salvar
print("Combinando as duas imagens...")
combine_images(caminho_imagem1, caminho_imagem2, save_path=caminho_combinada)

print("Processamento concluído!")
```

## Testes
Para executar os testes, utilize:

```bash
python -m unittest discover tests/
```

## Contribuições
Sinta-se à vontade para contribuir. Faça um fork do projeto, crie uma branch para suas alterações e envie um pull request.

## Licenciamento

Este projeto é licenciado sob a [MIT License](LICENSE) - veja o arquivo LICENSE para mais detalhes.

## Autor

Jacivaldo Carvalho [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/)


