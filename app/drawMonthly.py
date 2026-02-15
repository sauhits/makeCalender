from PIL import Image, ImageDraw, ImageFont
import calendar, os
from drawBaseImg import makeBaseCalender
from drawDescription import addDescription


# ベースイメージを作成して日付と月を書き込む
def drawCalender(year: int, month: int, taskDict: dict, descriptionDict: dict):
    baseFilePath: str = "./img/calender_base.jpg"
    saveFilePath: str = "./img/calender" + str(year) + "-" + str(month) + ".jpg"
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
                if n in taskDict:
                    draw.text(
                        (x_value, y_value + 20),
                        str(taskDict.get(n)),
                        (0, 0, 0),
                        font=font,
                    )
            x_value += 100
        x_value: int = 20
        y_value += 100

    im.save(saveFilePath, quality=95)
    addDescription(saveFilePath, descriptionDict)


di = {5: "ごみ捨て", 12: "ごみ捨て", 19: "ごみ捨て", 26: "ごみ捨て"}
di2 = {5: "プラゴミ", 12: "資源ごみ", 26: "燃えるゴミ"}
drawCalender(2026, 2, di, di2)
