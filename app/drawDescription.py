from PIL import Image, ImageDraw, ImageFont
import os


def addDescription(path: str, descriptionDict: dict):
    numOfDescription: int = len(descriptionDict)
    if numOfDescription == 0:
        return
    addSpace: int = 30 * numOfDescription + 10
    width: int = 720
    height: int = 820
    im = Image.new("RGB", (width, height + addSpace), (255, 255, 255))
    if not (os.path.isfile(path)):
        return
    im2 = Image.open(path)
    im2.paste(im)
    draw = ImageDraw.Draw(im)
    im2.save(path, quality=95)
