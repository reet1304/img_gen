from PIL import Image, ImageDraw, ImageFont
import random
import sys
import csv

pictures = ["alexey-savchenko-nGDZqViSOHQ-unsplash.jpg", "tina-vanhove-lOP9D8VN7Ew-unsplash.jpg",
            "alexander-sergienko-y-5CJNSwV-E-unsplash.jpg"]
img = Image.open(random.choice(pictures))
draw = ImageDraw.Draw(img)
font_size = img.width // 13
font = ImageFont.truetype("arial.ttf", size=font_size)

predictions =[]
# predictions = ["Счастье уже \n стоит за дверью.", "Будьте внимательны \n к своему здоровью.",
#      "Прислушайтесь к \n советам интуиции.", "Люди, что \n сейчас рядом,\n будут помогать\n весь год.",
#      "Нужная встреча\n произойдет\n совсем скоро.", "Любовь улыбается\n и ждет своего часа.",
#      "Везение в \nденежных вопросах.", "Удача в \nлюбом начинании.",
#       "Счастье где-то рядом,\n обернитесь вокруг.", "Год слёз,\n но только от радости.",
#       "Вас ожидает поездка\n в новую страну.", "Этот год кардинально\n изменит Вашу жизнь.",
#       "Возможно пополнение\n в семье в\n этом году.", "Карьерный рост будет\n стремителен и успешен.",
#       "Мир и покой\n в семье весь год.", "Романтическое свидание\n поможет найти\n взаимные чувства.",
#       "Любое дело \nобречено на успех.",
#      "Путешествие для души \nподарит необходимый отдых\n и новые впечатления.",
#       "Откройте сердце любви\n в этом году.", "Семья подарит \nнастоящую поддержку.",
#       "В этом году ожидается \nмножество новых знакомств.", "Пора отдохнуть \nи заняться хобби.",
#     "В этом году\n Вас ждет море счастья.", "Фортуна ответит\n <да> на любой вопрос.",
#     "Рискуйте\n и обязательно выиграете.", "Этот год принесет\n повышение на работе.",
#    "Желаемое осуществится\n в середине года.", "Этот год принесет\n только счастье и успех.",
#   "В этом году\n к Вам придет любовь,\n не упустите ее.",
#  "Очень удачный год\n для начала \nсобственного бизнеса."]


def draw_text(x, y, text, color):
    draw.text((x, y), text, font=font, fill=color, anchor='ms', align="center")


def texting(text: str):
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


def csv_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.reader(file_obj, delimiter=';')
    for line in reader:
        predictions.append(line[0])



if __name__ == '__main__':
    csv_path = "2021.csv"
    with open(csv_path, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)
    letter = random.choice(predictions)
    texting(letter)
    size = font.getsize(letter)
    print(size)
    img.show()
# img = Image.new('RGBA', (300, 300), image)
#
