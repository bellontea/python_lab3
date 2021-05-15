from PIL import Image, ImageDraw
 
def gradient(color):
    new_color = (0, 0, 0)
    res = Image.new("RGB", (512, 200), new_color)
    draw = ImageDraw.Draw(res)
    if color.lower() == 'r':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(i // 2, 0, 0), width=1)
    if color.lower() == 'g':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(0, i // 2, 0), width=1)
    if color.lower() == 'b':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(0, 0, i // 2), width=1)
    res.save("res.png", "PNG")