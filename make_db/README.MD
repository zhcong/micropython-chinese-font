# 1、convert.py
该脚本运行在pc即可 <br/>
```
python3 convert.py 字形文件.otf 常用汉字集.txt 字符图案大小 字符抬高像素
```
其中字符抬高像素是指有些字体会前几行留空，需要抬高

示例：

```
python3 convert.py 思源雅黑.otf 常用汉字集.txt 64 6
```
将otf格式的字形文件，按照常用汉字集中出现的字符，生成字符文件位于`build`下。
# 2、生成文件格式
文件整体数据分布如下

[字符图案大小，2byte] [字符数量，4byte] [字符数据，每字符占用(字符大小^2/8)byte] [索引]

索引部分结构如下

[utf8编码长度，1byte] [utf8编码，1/3byte] [排序，4byte]

