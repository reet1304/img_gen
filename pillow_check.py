from PIL import Image, ImageDraw, ImageFont
import random
import sys
pictures = ["alexey-savchenko-nGDZqViSOHQ-unsplash.jpg","tina-vanhove-lOP9D8VN7Ew-unsplash.jpg","alexander-sergienko-y-5CJNSwV-E-unsplash.jpg"  ]
img = Image.open(random.choice(pictures))
draw = ImageDraw.Draw(img)
font_size = img.width//10
font = ImageFont.truetype("arial.ttf", size=font_size)


def draw_text(x, y, text, color):
    draw.text((x, y), text, font=font, fill=color, anchor='ms', align="center")


def texting(text: str):
    outlineAmount = 3
    y = img.height // 2
    x = img.width // 2
    shadowColor = "black"
    # for adj in range(outlineAmount):
    adj = font_size / 50
    # move right
    draw_text(x - adj, y, text, shadowColor)  # draw.text((x - adj, y), text, font=font, fill=shadowColor, anchor='ms')
    # move left
    draw_text(x + adj, y, text, shadowColor)  # draw.text((x + adj, y), text, font=font, fill=shadowColor, anchor='ms')
    # move up
    draw_text(x, y + adj, text, shadowColor)  # draw.text((x, y + adj), text, font=font, fill=shadowColor, anchor='ms')
    # move down
    draw_text(x, y - adj, text, shadowColor)  # draw.text((x, y - adj), text, font=font, fill=shadowColor, anchor='ms')
    # diagnal left up
    draw_text(x - adj, y + adj, text,
              shadowColor)  # draw.text((x - adj, y + adj), text, font=font, fill=shadowColor, anchor='ms')
    # diagnal right up
    draw_text(x + adj, y + adj, text,
              shadowColor)  # draw.text((x + adj, y + adj), text, font=font, fill=shadowColor, anchor='ms')
    # diagnal left down
    draw_text(x - adj, y - adj, text,
              shadowColor)  # draw.text((x - adj, y - adj), text, font=font, fill=shadowColor, anchor='ms')
    # diagnal right down
    draw_text(x + adj, y - adj, text,
              shadowColor)  # draw.text((x + adj, y - adj), text, font=font, fill=shadowColor, anchor='ms')
    draw_text(x, y, text, (255, 255, 255))  # draw.text((x, y), text, font=font, fill=(255, 255, 255), anchor='ms')


if __name__ == '__main__':
    texting("Это твоё\n предсказание")
    img.show()
# img = Image.new('RGBA', (300, 300), image)
