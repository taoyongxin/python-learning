"""
读写二进制文件
@Date 2020.04.11
"""


def main():
    try:
        # 将avatar.jpg以二级制制度方式打开啊，读入data变量
        with open('./res/avatar.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        # 将avatar.jpg二级制写的方式打开，写入avatar_copy.jpg
        with open('./res/avatar_copy.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print("程序执行结束")


if __name__ == "__main__":
    main()
