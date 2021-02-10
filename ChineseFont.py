import btree

CACHE_CHAR_COUNT = 32

class ChineseFont:
    
    def __init__(self, file, font_size, is_cache):
        self.__font_size=font_size
        self.__is_cache=is_cache
        cache_size = 0;
        # open data file
        if(is_cache):
            cache_size = int((font_size * font_size + 3) / 8) * CACHE_CHAR_COUNT
        self.__db_file = open(file, 'rb')
        self.__db = btree.open(self.__db_file, cachesize=cache_size)
    
    def get_font_size(self):
        return self.__font_size
    
    def get_is_cache(self):
        return self.__is_cache

    def is_exist(self, key):
        return key in self.__db
    
    def get_bit_map(self, key):
        return self.__db[key]

    def close(self):
        self.__db.close()
        self.__db_file.close()
    