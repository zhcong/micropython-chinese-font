# 1、convert.py
该脚本运行在pc即可 <br/>
```
python3 convert.py 字形文件.otf 常用汉字集.txt 字体输出大小 是否裁剪
```
其中是否裁剪指由于部分字体会留空，是否需要忽略，示例：
```
python3 convert.py 思源雅黑.otf 常用汉字集.txt 64 true
```
将otf格式的字形文件，按照常用汉字集中出现的字符，转换为二进制的中间文件`font.data`
# 2、to_btree.py
该脚本运行在mcu上，将pc上生成的中间文件`font.data`转换为mcu使用的btree文件`font_db.data`

```
FONT_SIZE一定要修改为字体大小，同 -字体输出大小-
```



# 3、生成文件

`font.data`格式：每个字都会是以下格式[utf8编码长度，1byte] [utf8编码，1 or 3 byte] [字形数据，size*size/8 bytes]<br/>

`font_db.data`键值格式：key：utf-8二进制编码，value：字形的点阵

`font_db.data`位置 `/make_db/bilud`