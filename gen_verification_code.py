from PIL import Image, ImageDraw, ImageFont
import random


def verifycode():
    """生成验证图片"""
    # 定义变量,用于画面的背景色,宽,高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    heigh = 50
    # 创建画面对象
    im = Image.new('RGB', (width, heigh), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()方法绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigh))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    # 随机生成四个值作为验证码
    ran_str = ""
    for i in range(0, 4):
        ran_str += str[random.randrange(0, len(str))]
    print(ran_str)
    
    # 构造字体对象 可以不定义字体就要用到load_default()函数
    font = ImageFont.load_default()
    # font = ImageFont().truetype(r'c:\windows\Fonts\AdobeArabic-Bold.otf', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), ran_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), ran_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), ran_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), ran_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    im.save('idencode.png')


if __name__ == '__main__':
    verifycode()
   
   
    """
    # 存入session, 用于做进一步的验证(用于html请求时,且还要传入request)
    # request.session['verifycode'] = ran_str

    # 内存文件操作
    import io

    buf = io.BinaryIO
    # 将图片保存在内存中,文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端,MIME类型为图片png
    # buf.getvalue()从内存中取出
    return HttpResponse(buf.getvalue(), 'image/png')
    """