"""
使用Pillow来处理图像：pip3 install Pillow
@Date 2020.04.12
"""

# 图片相关
from io import BytesIO
from PIL import Image
import requests as req
from PIL import Image, ImageFilter
# 系统相关os
import os

img = Image.open('./res/img/1.jpg')
print(img.format, img.size, img.mode)

# 直接可以复制
Image.open('./res/img/1.jpg').save('./res/img/1-1.jpg')

# 用thumbnail()方法为其生成原尺寸1/3大小的缩略图
w, h = img.size
img.thumbnail((w//3, h//3))
img.save('./res/img/缩略.jpg', 'jpeg')

# 使用filter()滤镜，此处使用模糊效果
img = Image.open('./res/img/1.jpg')
img1 = img.filter(ImageFilter.BLUR)
img1.save('./res/img/模糊.jpg', 'jpeg')
# 翻转
img = Image.open('./res/img/1.jpg')
img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
img1.save('./res/img/左右翻转.jpg', 'jpeg')
img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
img1.save('./res/img/上下翻转.jpg', 'jpeg')
img1 = img.transpose(Image.ROTATE_90)
img1.save('./res/img/旋转90度.jpg', 'jpeg')
img1 = img.transpose(Image.ROTATE_180)
img1.save('./res/img/旋转180度.jpg', 'jpeg')

# 学习遍历目录和文件
list = os.listdir('./res/img')
# print(list)
# 此处仅遍历img根目录，遍历其子目录自行学习
# 使用os.path.splitext(file)[0]可获得主文件名
# 使用os.path.splitext(file)[-1] 可获得以 . 开头的文件后缀名
for file in list:
    if os.path.splitext(file)[-1] == '.jpg':
        print(os.path.splitext(file)[0])

# 处理网络图片
resp = req.get(
    'https://niit-student.oss-cn-beijing.aliyuncs.com/markdown/1.jpg')
Image = Image.open(BytesIO(resp.content))
# 在此之前可以做相关处理
Image.save('./res/download/test.png')
