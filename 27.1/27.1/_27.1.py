from PIL import Image 
 
def make_preview(size, n_colors):
    pic = Image.open("image.jpg")
    res = pic.resize(size)
    res = res.quantize(n_colors)
    res.save('res.bmp')
