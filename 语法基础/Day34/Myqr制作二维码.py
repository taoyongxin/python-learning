"""
Myqr制作二维码
    """
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont


def img_code():
    myqr.run(words='https://niit-student.oss-cn-beijing.aliyuncs.com/markdown/ZNJ3(_A`3A)M~5G7`MCP3YD.png',
             version=1,
             level='H',
             picture='./res/img/lvye.png',
             colorized=True,
             contrast=1.0,
             brightness=1.0,
             save_name='code2.png',
             save_dir=os.getcwd() + '/res/img/')


def draw():
    img = Image.open('./res/img/code2.png')
    w, h = img.size
    txt = 'Tao'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/font/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/img/code3.png')


if __name__ == '__main__':
    img_code()
    draw()
