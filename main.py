##
 #  @filename   :   main.cpp
 #  @brief      :   4.2inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 28 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import epd4in2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import qrcode

EPD_WIDTH = 400
EPD_HEIGHT = 300

def main():
    epd = epd4in2.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame

    # 画像
    nahuda = Image.open('image/tekimen_nahuda_monoclo.bmp')
    nahuda = nahuda.rotate(90, expand=True)
    
    image.paste(nahuda, (0, 0))

    # もじ
    moji = Image.new('1', (EPD_HEIGHT, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(moji)
    fontsize = 40
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', fontsize)

    small = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', 24)
    symbola = ImageFont.truetype("/usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf", 24)
    display_1st_line = 'てきめん'
    center_1st_line = EPD_HEIGHT / 2 - (len(display_1st_line) * fontsize) / 2
    display_2nd_line = '@youkidearitai'
    # TODO: 1.9してるのは半角のサイズを取る方法がわからなかった
    center_2nd_line = EPD_HEIGHT / 2 - (len(display_2nd_line) / 1.9 * fontsize) / 2

    draw.text((center_1st_line, 0), display_1st_line, font=font, fill=0)
    draw.text((center_2nd_line, fontsize + 5), display_2nd_line, font=font, fill=0)
    draw.text((0, 240), '💩', font=symbola, fill=0) # うんち(pile of poo)

    draw.text((320-24, 240), "💩", font=symbola, fill=0)

    moji = moji.rotate(90, expand=True)

    image.paste(moji, (135, 0))

    # qrコード
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=2
    )

    qr.add_data('https://twitter.com/youkidearitai')
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    #qr_image = qr_image.rotate(90, expand=True)
    w, h = qr_image.size
    qr_center = (EPD_WIDTH / 2 - w / 2, EPD_HEIGHT / 2 - h / 2)
    qr_paste_position = (int(qr_center[0]) + 80, int(qr_center[1]))

    image.paste(qr_image, qr_paste_position)

    epd.display_frame(epd.get_frame_buffer(image))

if __name__ == '__main__':
    main()
