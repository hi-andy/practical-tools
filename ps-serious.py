import os
from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *

from PIL import Image

window = Tk()
window.title('产品图片处理程序')
path = StringVar()

path_ = None
color = None


def select_path():
    global path_
    path_ = askdirectory()
    path.set(path_)


# 选择颜色
def getColor():
    global color
    color = tuple([int(x) for x in askcolor()[0]])


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
def resize_back_color(file_dir, out_path, width=400, bgcolor=None):
    files = os.listdir(file_dir)

    if not file_dir:
        showwarning(title='警告', message='未正确选择图片目录')
    else:
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        if bgcolor is not None and bgcolor != 1:
            bgcolor = bgcolor
        elif bgcolor == 2:
            bgcolor = (255, 255, 255)
        elif bgcolor == 3:
            bgcolor = (0, 0, 0)
        else:
            bgcolor = (128, 128, 128)

        for file in files:
            file_path = file_dir + os.sep + file
            # new_file = out_path + file.split('.')[0] + '.png'
            new_file = out_path + file
            print(new_file)

            # 打开，缩放原图
            image = Image.open(file_path)
            (w, h) = image.size
            width_percent = (width / float(w))
            height = int((float(h) * float(width_percent)))
            resize = image.resize((width, height), Image.ANTIALIAS)

            # 创建背景图，并贴合。 如果为 RGBA 模式，必须保存为 png 格式。 "A" alpha png 透明度通道
            main_image = Image.new('RGB', (400, 400), bgcolor)
            position = (0, int((main_image.height - resize.height) / 2))
            main_image.paste(resize, position)
            main_image.save(new_file)

        showinfo(title='处理结果', message='所有图片处理完成')


def set_color():
    global color
    color = CheckVar1.get()


file_out = '/Users/hua/Downloads/pictures/'
# resize_back_color(path, file_out)

Label(window, text='图片目录:').grid(column=0, row=0)
Entry(window, textvariable=path, width=50).grid(column=1, row=0, columnspan=2)
Button(window, text='选择图片目录', command=select_path).grid(column=3, row=0)

Label(window, text='图片背景色').grid(column=0, row=1)

CheckVar1 = IntVar()
Radiobutton(window, text="灰色", variable=CheckVar1, value=1, command=set_color).grid(column=1, row=1)
Radiobutton(window, text='白色', variable=CheckVar1, value=2, command=set_color).grid(column=2, row=1)
Radiobutton(window, text='黑色', variable=CheckVar1, value=3, command=set_color).grid(column=3, row=1)
Button(window, text='自定义', command=getColor).grid(column=4, row=1)

Button(window, text='开始处理图片', command=lambda: resize_back_color(path_, file_out, bgcolor=color)).grid(column=1, row=2,
                                                                                                      columnspan=2)

Button(window, text='退出', command=window.quit).grid(column=2, row=2, columnspan=2)

window.mainloop()
