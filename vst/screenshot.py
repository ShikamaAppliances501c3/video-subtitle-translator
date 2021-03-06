import mss
import mss.tools


class Screenshot:
    @staticmethod
    def capture(path, left, top, width, height):
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {"top": top, "left": left, "width": width, "height": height}
            # Grab the data
            sct_img = sct.grab(monitor)
            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=path)
