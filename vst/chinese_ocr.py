try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2


class ChineseOCR:
    @staticmethod
    def ocr(path) -> str:
        image = cv2.imread(path)
        return pytesseract.image_to_string(image, lang='chi_sim')