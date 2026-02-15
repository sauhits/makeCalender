from PIL import Image, ImageDraw, ImageFont
import calendar, os
from drawBaseImg import makeBaseCalender
from drawDescription import addDescription


# ベースイメージを作成して日付と月を書き込む
async def drawCalender(
    year: int, month: int, task_dict: dict[int, str], description_dict: dict[int, str]
):
    base_file_path: str = "./img/calender_base.jpg"
    save_file_path: str = "./img/calender" + str(year) + "-" + str(month) + ".jpg"
    makeBaseCalender()
    im: Image = Image.open(base_file_path)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 12)
    title_font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 70)

    draw.text((285, 10), str(month), (0, 0, 0), font=title_font)

    calendar.setfirstweekday(6)
    date_list: list[list[int]] = calendar.monthcalendar(year, month)
    x_value: int = 20
    y_value: int = 220

    for i in date_list:
        for n in i:
            if n != 0:
                draw.text(
                    (x_value, y_value),
                    "　　　" + str(n),
                    (0, 0, 0),
                    font=font,
                )
                if n in task_dict:
                    draw.text(
                        (x_value, y_value + 20),
                        str(task_dict.get(n)),
                        (0, 0, 0),
                        font=font,
                    )
            x_value += 100
        x_value = 20
        y_value += 100

    im.save(save_file_path, quality=95)
    addDescription(save_file_path, description_dict)
    return save_file_path
