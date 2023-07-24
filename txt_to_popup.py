from PIL import Image, ImageDraw, ImageFont


def txt_to_popup(txt: str):
    txt = txt.upper()
    txt = f"[{txt}]"
    txts = txt.split("\n")
    # load an image
    image = Image.open("popup.png")
    draw = ImageDraw.Draw(image)
    W, H = image.size
    font = ImageFont.truetype("font.ttf", 40)
    num_lines = len(txts)
    h_shift = 50
    # initial_h = (H - (num_lines * h_shift)) // 2
    initial_h = 0
    current_h = initial_h
    for txt_ in txts:
        _, _, w, h = draw.textbbox((0, 0), txt_, font=font)
        draw.text((W-w)/2, 0, txt_, font=font)
        # current_h += h_shift

    image.show()


txt_to_popup("TEXT ALIGN TOP LINE\nNEW LINE MIDDLE\nBOTTOM LINE")
