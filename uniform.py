from PIL import Image
import os, sys

path ='./data/portrait/'

dirs = os.listdir( path )


for item in dirs:
    try:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            longer_side = max(im.size)

            horizontal_padding = (longer_side - im.size[0]) / 2
            vertical_padding = (longer_side - im.size[1]) / 2
            f, e = os.path.splitext(path+item)
            imResize = im.crop(
            (
                -horizontal_padding,
                -vertical_padding,
                im.size[0] + horizontal_padding,
                im.size[1] + vertical_padding
            )
            )
            RGB = imResize.convert('RGB')
            little = RGB.resize((32,32), Image.ANTIALIAS)

            little.save(f + 'resize.jpg', 'JPEG', quality=30)
            
    except Exception as e:
        print(e)