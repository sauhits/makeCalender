from PIL import Image, ImageDraw, ImageFont


def addDescription(wrap_im: Image, description_dict: dict[int, str], tmp_byte):
    font = ImageFont.truetype("./font/NotoSansJP-Regular.ttf", 12)
    num_of_description: int = len(description_dict)
    im2: Image = wrap_im  # 既存
    if num_of_description == 0:
        im2.save(tmp_byte, format="JPEG", quality=95)
        return
    add_space: int = 30 * num_of_description + 10
    width: int = 720
    height: int = 820

    im: Image = Image.new("RGB", (width, height + add_space), (255, 255, 255))  # 新規
    draw = ImageDraw.Draw(im)
    for i in range(num_of_description):
        y_value: int = height + 30 * (i + 1)
        draw.line(((10, y_value), (710, y_value)), fill=(0, 0, 0))

    y_value = height + 10
    for i in range(0, 32):
        if i in description_dict:
            draw.text(
                (10, y_value), f"{i}日: {description_dict.pop(i)}", (0, 0, 0), font=font
            )
            y_value += 30

    im.paste(im2, (0, 0))

    im.save(tmp_byte, format="JPEG", quality=95)
