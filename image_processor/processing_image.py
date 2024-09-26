import cv2


def to_grayscale(image_path, save_path=None):
    # Converte uma imagem para escala de cinza.
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("A imagem não pôde ser carregada.")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if save_path:
        cv2.imwrite(save_path, gray_image)

    cv2.imshow('Imagem em escala cinza', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return gray_image


def combine_images(image_path1, image_path2, save_path=None):
    # Combina duas imagens usando uma média.
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        raise ValueError("Uma das imagens não pôde ser carregada.")

    # Redimensiona as imagens para o mesmo tamanho
    image1 = cv2.resize(image1, (640, 480))
    image2 = cv2.resize(image2, (640, 480))

    combined_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

    if save_path:
        cv2.imwrite(save_path, combined_image)

    cv2.imshow('Imagem combinada', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return combined_image
