try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np


class ChineseOCR:
    @staticmethod
    def ocr(path) -> str:
        image = cv2.imread(path)
        image = ChineseOCR.netflix_manipulations(image)
        # cv2.imwrite("ocr_result.png", image)
        return pytesseract.image_to_string(image, lang='chi_sim')

    @staticmethod
    def netflix_manipulations(image):
        kernel = np.ones((2, 2), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return image