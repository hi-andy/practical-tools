from PIL import Image


# 贴合图片
def image_merge():
    main_image = Image.new('RGBA', (400, 400), (128, 128, 128))
    from_imge = Image.open('1.jpg')
    position = (0, int((main_image.height - from_imge.height) / 2))
    main_image.paste(from_imge, position)
    main_image.save('merged.png')


# 宽高比缩放图片
def image_resize(width=400):
    image = Image.open('2.jpg')
    (w, h) = image.size
    width_percent = (width / float(w))
    height = int((float(h) * float(width_percent)))

    resize = image.resize((width, height), Image.ANTIALIAS)
    resize.save('resize.png')


# 宽高比缩放图片，空白处添加背景色
def resize_back_color(width=400):
    # 打开，缩放原图
    image = Image.open('2.jpg')
    (w, h) = image.size
    width_percent = (width / float(w))
    height = int((float(h) * float(width_percent)))
    resize = image.resize((width, height), Image.ANTIALIAS)

    # 创建背景图，并贴合
    main_image = Image.new('RGBA', (400, 400), (128, 128, 128))
    position = (0, int((main_image.height - resize.height) / 2))
    main_image.paste(resize, position)
    main_image.save('resizeColor.png')


resize_back_color()
