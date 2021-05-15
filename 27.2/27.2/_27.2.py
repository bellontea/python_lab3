from PIL import Image
 
def negative(pixels, i, j):
    """Эффект негитива"""
    r = pixels[i, j][0]
    g = pixels[i, j][1]
    b = pixels[i, j][2]
    return (255 - r, 255 - g, 255 - b)
