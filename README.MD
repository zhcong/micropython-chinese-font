## 1、字库文件生成
全部生成代码位于`make_db`，具体生成步骤见[README文件](make_db/README.MD)
已生成文件`font_db.data`，该文件是btree数据库文件，使用键值对存储，可以存储在任意存储上(片上存储、外置SD卡等)，不占用RAM空间