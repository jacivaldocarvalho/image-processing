import unittest
from image_processor.processing_image import to_grayscale, combine_images


class TestImageProcessing(unittest.TestCase):
    def test_to_grayscale(self):
        gray_image = to_grayscale('path/to/sample.jpg')
        # Verifica se é uma imagem em escala de cinza
        self.assertEqual(gray_image.ndim, 2)

    def test_combine_images(self):
        combined_image = combine_images('path/to/sample1.jpg',
                                        'path/to/sample2.jpg')
        # Verifica se a imagem combinada é colorida
        self.assertEqual(combined_image.shape[2], 3)


if __name__ == '__main__':
    unittest.main()
