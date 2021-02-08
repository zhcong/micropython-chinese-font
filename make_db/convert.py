#! /bin/bash
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from bitarray import bitarray

def print_import(text):
    print(text)
    print('-------------------------')

def auto_cut_func(img, draw, chart, font, size):
    draw.text((0,0), chart,font = font, fill='black')
    img_np = np.array(img)
    index = np.where(img_np > 0)
    draw.rectangle((0, 0, size, size), fill=(0, 0, 0, 0))
    return (0 if len(index[0]) == 0 else index[0][0])

def load_chinese(file_name):
    with open(file_name) as fp:
        charts = fp.readline()
        return charts

def binarization(img, size):
    img_np = np.array(img)
    img_result_list = bitarray()
    for pix_line in img_np:
        for pix in pix_line:
            if(pix[3] >= 255/2):
                img_result_list.append(True)
            else:
                img_result_list.append(False)
    return img_result_list.tobytes()

def convert_chart(chart, font, size, auto_cut):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if(auto_cut):
        cut_line = auto_cut_func(img, draw, chart, font, size)
        draw.text((0,-cut_line), chart,font = font, fill='black')
    else:
        draw.text((0,0), chart,font = font, fill='black')
    img_np = binarization(img, size)
    return img_np

if __name__=='__main__':
    if(len(sys.argv)<4):
        print_import('参数缺失，python3 convert.py xxx.otf xxx.txt size auto_cut')
        exit(-1)
    print_import('字形文件%s，筛选字符集文件%s' %(sys.argv[1], sys.argv[2]))

    size = int(sys.argv[3])
    auto_cut = sys.argv[4] == "true"

    charts = load_chinese(sys.argv[2])
    print_import('读取筛选字符集文件\nover')

    font = ImageFont.truetype(sys.argv[1], size)
    print_import('读取字形文件\nover')

    # [utf8编码长度，1byte][utf8编码，1 or 3 byte][字形数据，size*size/8 bytes]
    with open('font.data', 'wb') as fp:
        for chart in charts:
            char_bin_data = convert_chart(chart, font, size, auto_cut)
            chart_key = bytes(chart,encoding='utf-8')
            if(len(chart_key) == 1): 
                fp.write(b'\x01')
            else:
                fp.write(b'\x03')
            fp.write(chart_key)
            fp.write(char_bin_data)
    print_import('写入中间文件\nover')
