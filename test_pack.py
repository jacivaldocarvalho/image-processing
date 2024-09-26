from image_processor_jr.processing_image import to_grayscale, combine_images

# Converter imagem para escala de cinza
gray_image = to_grayscale('imagem1.jpg', save_path='gray_image.jpg')

# Combinar duas imagens
combined_image = combine_images('imagem1.jpg', 'imagem2',
                                save_path='combine_image.jpg')
