import btree

# 单个字符大小
FONT_SIZE = 32

try:
    f_db = open("font_db.data", "r+b")
except OSError:
    f_db = open("font_db.data", "w+b")

with open('font.data','rb') as f_data:
    db = btree.open(f_db)
    while True:
        key_len = f_data.read(1)
        if key_len == b'':
            break
        key = '\x00\x00\x00'
        if(key_len[0] == 1):
            key = f_data.read(1)
        else:
            key = f_data.read(3)
        data = f_data.read(int(FONT_SIZE*FONT_SIZE/8))
        db[key]=data
        print(key + ' over')
db.close()
f_db.close()
