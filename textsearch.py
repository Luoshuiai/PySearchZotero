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
    word_id=[]
    for i in range( 0 , length ):
        cursor.execute('SELECT wordID FROM fulltextWords WHERE word LIKE ?', (text[i],))
        data = cursor.fetchall()
        if data != []:
            word_id.append(data[0][0])
    return word_id


def get_item_id(word_id):
    item_id_list=[]
    for i in range(0, len(word_id)):
        cursor.execute('SELECT itemID FROM fulltextItemWords WHERE wordID LIKE ?', (word_id[i],))
        data = cursor.fetchall()
        for i in range(0, len(data)):
            item_id_list.append(data[i][0])

    return item_id_list


def get_key_list(item_id):
    keys=[]
    for i in range(0, len(item_id)):
        cursor.execute('SELECT key FROM items WHERE itemID LIKE ?', (item_id[i],))
        data = cursor.fetchall()
        keys.append(data[0][0])
    return keys

def text_search(text):
    text,length=split_zh_en(text)
    word_id = get_word_id(text, length)
    item_id = get_item_id(word_id)
    key_list = get_key_list(item_id)
    return key_list


def de_duplicate(list_value):
    list_de_duplicate=Counter(list_value)
    return list_de_duplicate




if __name__ == "__main__":
    text=input("Please input the text you want to search:")
    keys=text_search(text)
    print(keys)
    keys=de_duplicate(keys)
    print(keys)
    keys=list(keys.values())
    print(keys)
    # webbrowser.open("zotero://select/library/items/"+keys[0])
    mydb.close()