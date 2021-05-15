from PIL import Image
 
def makeanagliph(filename, delta):
    pic = Image.open(filename)
    pixels = pic.load()
    x, y = pic.size
    res = Image.new('RGB', (x, y), (255, 255, 255))
    pixels2 = res.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            if (i - delta >= 0):
                r1, g1, b1 = pixels[i - delta, j]
                pixels2[i, j] = r1, g, b
            else:
                g, b = pixels[i, j][1:]
                pixels2[i, j] = 0, g, b
    res.save('res.jpg')