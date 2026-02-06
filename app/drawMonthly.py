from PIL import Image, ImageDraw, ImageFont
import calendar, os
from drawBaseImg import makeBaseCalender


def draw_calender(year: int, month: int):
    baseFilePath: str = "./img/calender_base.jpg"
    im: Image
    if os.path.isfile(baseFilePath):
        im = Image.open(baseFilePath)
    else:
        makeBaseCalender()
        im = Image.open(baseFilePath)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 12)
    titleFont = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 70)

    draw.text((285, 10), str(month), (0, 0, 0), font=titleFont)

    calendar.setfirstweekday(6)
    dateList: list = calendar.monthcalendar(year, month)
    x_value: int = 20
    y_value: int = 220

    for i in dateList:
        for n in i:
            if n != 0:
                draw.text(
                    (x_value, y_value),
                    "　　　" + str(n),
                    (0, 0, 0),
                    font=font,
                )
            x_value += 100
        x_value: int = 20
        y_value += 100

    im.save("./img/calender" + str(year) + "-" + str(month) + ".jpg", quality=95)
