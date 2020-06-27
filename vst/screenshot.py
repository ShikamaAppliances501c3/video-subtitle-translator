import mss
import mss.tools

class Screenshot:
    @staticmethod
    def capture(left, top, width, height):
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {"top": top, "left": left, "width": width, "height": height}
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
