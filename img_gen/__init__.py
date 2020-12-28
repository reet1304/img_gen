from PIL import Image, ImageDraw, ImageFont

class StrokeCenterDrawer:
    def __init__(self, img: Image, font: str):
        self._draw = ImageDraw.Draw(img)

        font_size = img.width // 13
        self._font = ImageFont.truetype(font, size=font_size)

        self._generate_draw_positions(img)

    def _generate_draw_positions(self, img: Image):
        x_center, y_center = img.width // 2, img.height // 2
        self._center_position = (x_center, y_center)
        shift = (img.width // 13) / 50
        self._stroke_positions = [
            (x_center - shift, y_center),
            (x_center - shift, y_center + shift),
            (x_center, y_center + shift),
            (x_center + shift, y_center + shift),
            (x_center + shift, y_center),
            (x_center + shift, y_center - shift),
            (x_center, y_center - shift),
            (x_center - shift, y_center - shift),
        ]

    def _draw_pos(self, pos, text: str, color):
        self._draw.text(pos, text, font=self._font, fill=color, anchor='ms', align="center")

    def draw(self, text: str, main_color = (255, 255, 255), stroke_color = (0, 0, 0)):
        for pos in self._stroke_positions:
            self._draw_pos(pos, text, color=stroke_color)
        self._draw_pos(self._center_position, text, color=main_color)


# def _texting(img, text: str):
#     y = img.height // 2
#     x = img.width // 2
#     shadowColor = "black"
#     # for adj in range(outlineAmount):
#     adj = font_size / 50
#     _draw_text(x - adj, y, text,
#                shadowColor)
#     _draw_text(x + adj, y, text,
#                shadowColor)
#     _draw_text(x, y + adj, text, shadowColor)
#     # move down
#     _draw_text(x, y - adj, text,
#                shadowColor)
#     _draw_text(x - adj, y + adj, text, shadowColor)
#     _draw_text(x + adj, y + adj, text,
#                shadowColor)
#     _draw_text(x - adj, y - adj, text,
#                shadowColor)
#     _draw_text(x + adj, y - adj, text,
#                shadowColor)
#     _draw_text(x, y, text, (255, 255, 255))

def insert_text_center(img_path: str, font: str, prediction: str) -> Image:
    img = Image.open(img_path)
    StrokeCenterDrawer(img, font).draw(prediction)
    return img
