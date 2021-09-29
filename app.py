from PIL import Image, ImageDraw, ImageFont
import sys

"""
이름 만들기
"""
frameNameImg = Image.open('frame_name.png')
nameText = sys.argv[1]  # 매개변수로 넘겨주는 이름

font = ImageFont.truetype('./CJ ONLYONE NEW title Medium.ttf', size=200, encoding='UTF-8')

draw = ImageDraw.Draw(frameNameImg)
draw.text((370, 120), nameText, font=font, fill=(250, 209, 101))

frameNameImg = frameNameImg.resize((192, 64))

frameNameImg.save('result_name_{}.png'.format(nameText), 'PNG')


"""
초상화 만들기
"""
framePortraitImg = Image.open('frame_portrait.png')
try:
    portraitImg = Image.open('portrait.png')
except FileNotFoundError:
    portraitImg = Image.open('portrait.jpg')

portraitImg = portraitImg.resize((975, 785))

mergedPortraitImg = Image.new('RGB', (framePortraitImg.size[0], framePortraitImg.size[1]), (255, 255, 255))

mergedPortraitImg.paste(framePortraitImg, (0, 0))
mergedPortraitImg.paste(portraitImg, (162, 155))

mergedPortraitImg = mergedPortraitImg.resize((192, 192))

mergedPortraitImg.save('result_portrait_{}.png'.format(nameText), 'PNG')


