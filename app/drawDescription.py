from PIL import Image, ImageDraw, ImageFont
import os
from typing import Final


def addDescription(path: str, description_dict: dict[int, str]):
    font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 12)
    num_of_description: Final[int] = len(description_dict)
    if num_of_description == 0:
        return
    add_space: int = 30 * num_of_description + 10
    width: Final[int] = 720
    height: Final[int] = 820

    im: Image = Image.new("RGB", (width, height + add_space), (255, 255, 255))  # 新規
    draw = ImageDraw.Draw(im)
    for i in range(num_of_description):
        y_value: int = height + 30 * (i + 1)
        draw.line(((10, y_value), (710, y_value)), fill=(0, 0, 0))

    y_value = height + 10
    for i in range(0, 31):
        if i in description_dict:
            draw.text(
                (10, y_value), f"{i}日: {description_dict.pop(i)}", (0, 0, 0), font=font
            )
            y_value += 30

    if not (os.path.isfile(path)):
        return
    im2: Image = Image.open(path)  # 既存
    im.paste(im2, (0, 0))

    im.save(path, quality=95)
