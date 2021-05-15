from PIL import Image, ImageDraw
 
 
def board(num, s):
    pic = Image.new("RGB", (num * s, num * s), (256, 256, 256))
    draw = ImageDraw.Draw(pic)
    b = (0, 0, 0)
    for i in range(num):
        for j in range(num):
            if (i % 2 == 0) and (j % 2 == 0) or (i % 2 == 1) and (j % 2 == 1):
                draw.rectangle([j * s, i * s, j * s + s - 1, i * s + s - 1], b)
    pic.save('res.png', 'PNG')
