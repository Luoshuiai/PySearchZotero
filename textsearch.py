# -*- coding: utf-8 -*-
import sqlite3
from collections import Counter,OrderedDict
import webbrowser

from matplotlib.collections import Collection


from textsplit import *

Sqlite_path=input("Please input the path of your sqlite file:")
mydb = sqlite3.connect(Sqlite_path)
cursor = mydb.cursor()
    
def get_word_id(text, length):
    # 获取"中文单字、英文单词、数字"对应的 word ID 
    word_id=[]
    for i in range( 0 , length ):
        cursor.execute(
            'SELECT wordID FROM fulltextWords WHERE word LIKE ?', 
            str(text[i],))
        data = cursor.fetchall()
        if data != []:
            word_id.append(data[0][0])
    return word_id


def get_item_id(word_id):
    # 获取 Word ID 对应的 Item ID
    item_id_list=[]
    for i in range(0, len(word_id)):
        cursor.execute(
            'SELECT itemID FROM fulltextItemWords WHERE wordID LIKE ?', 
            (word_id[i],))
        data = cursor.fetchall()
        for i in range(0, len(data)):
            item_id_list.append(data[i][0])

    return item_id_list


def get_key_list(item_id):
    # 获取 Item ID 对应的 Key
    keys=[]
    for i in range(0, len(item_id)):
        cursor.execute(
            'SELECT key FROM items WHERE itemID LIKE ?', 
            (item_id[i],))
        data = cursor.fetchall()
        keys.append(data[0][0])
    return keys

def key_to_url(key):
    # 把key 转为 Zotero 的打开链接
    url="zotero://select/library/items/"+key
    return url


def de_duplicate(list_value):
    # 对 key 去重，计数
    key_de_duplicate,key_counter=[],[]
    temp_list,list_value=list_value[0:1],list_value[1:]  
    while temp_list != []:
        if temp_list[0] in list_value:
            t = 1   
            while temp_list[0] in list_value:
                t += 1
                list_value.remove(temp_list[0])
            key_counter.append(t)
            key_de_duplicate.append(temp_list[0])
        else:
            key_de_duplicate.append(temp_list[0])
            key_counter.append(1)        
        temp_list,list_value=list_value[0:1],list_value[1:]    
        
    return key_de_duplicate,key_counter




if __name__ == "__main__":
    text=input("Please input the text you want to search:")
    text,lenght=split_zh_en(text)
    word_id=get_word_id(text, lenght)
    item_id=get_item_id(word_id)
    key_list=get_key_list(item_id)
    keylist,keycounter=de_duplicate(key_list)
    print(keylist,keycounter)

    # webbrowser.open("zotero://select/library/items/"+keys[0])
    mydb.close()

    