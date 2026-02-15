from PIL import Image, ImageDraw, ImageFont


def makeBaseCalender():
    im = Image.new("RGB", (720, 820), (255, 255, 255))  # 画像サイズ,背景色
    draw = ImageDraw.Draw(im)

    draw.line(
        ((10, 10), (710, 10), (710, 810), (10, 810), (10, 10)), fill=(0, 0, 0)
    )  # 外枠

    # ここから横線
    draw.line(((10, 130), (710, 130)), fill=(0, 0, 0))
    draw.line(((10, 210), (710, 210)), fill=(0, 0, 0))
    draw.line(((10, 310), (710, 310)), fill=(0, 0, 0))
    draw.line(((10, 410), (710, 410)), fill=(0, 0, 0))
    draw.line(((10, 510), (710, 510)), fill=(0, 0, 0))
    draw.line(((10, 610), (710, 610)), fill=(0, 0, 0))
    draw.line(((10, 710), (710, 710)), fill=(0, 0, 0))

    # ここから縦線
    draw.line(((110, 130), (110, 810)), fill=(0, 0, 0))
    draw.line(((210, 130), (210, 810)), fill=(0, 0, 0))
    draw.line(((310, 130), (310, 810)), fill=(0, 0, 0))
    draw.line(((410, 130), (410, 810)), fill=(0, 0, 0))
    draw.line(((510, 130), (510, 810)), fill=(0, 0, 0))
    draw.line(((610, 130), (610, 810)), fill=(0, 0, 0))

    # # 日曜日
    # draw.polygon(
    #     ((10, 130), (110, 130), (110, 210), (10, 210)),
    #     fill=(255, 60, 60),
    #     outline=(0, 0, 0),
    # )

    # # 土曜日
    # draw.polygon(
    #     ((610, 130), (710, 130), (710, 210), (610, 210)),
    #     fill=(60, 60, 255),
    #     outline=(0, 0, 0),
    # )

    title_font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 50)

    draw.text((35, 130), "日", (0, 0, 0), font=title_font)
    draw.text((135, 130), "月", (0, 0, 0), font=title_font)
    draw.text((235, 130), "火", (0, 0, 0), font=title_font)
    draw.text((335, 130), "水", (0, 0, 0), font=title_font)
    draw.text((435, 130), "木", (0, 0, 0), font=title_font)
    draw.text((535, 130), "金", (0, 0, 0), font=title_font)
    draw.text((635, 130), "土", (0, 0, 0), font=title_font)

    title_font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 70)
    draw.text((385, 10), "月", (0, 0, 0), font=title_font)

    # draw.text((285, 10), "01", (0, 0, 0), font=title_font)

    title_font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 12)
    # draw.text((20, 220), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度
    # draw.text((20, 240), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度,1行20px
    # draw.text((120, 320), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度
    # draw.text((220, 420), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度
    # draw.text((320, 520), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度
    # draw.text((420, 620), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度
    # draw.text((520, 720), "あいうえおかき", (0, 0, 0), font=title_font)  # 7文字程度

    im.save("./img/calender_base.jpg", quality=95)


makeBaseCalender()
