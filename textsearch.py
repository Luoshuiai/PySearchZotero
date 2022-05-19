# -*- coding: utf-8 -*-
import sqlite3
from textsplit import *

mydb = sqlite3.connect('zotero.sqlite')
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

    print(item_id_list)  
    return item_id_list

