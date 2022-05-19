# -*- coding: utf-8 -*-

def split_zh_en(text):
    # 分割中英文
    zh_list=[]
    en_list=[]
    number_list=[]
    word=''
    number=''
    for  i in range (0,len(text)):
        if ord(text[i]) >= 0x4e00 and ord(text[i]) <= 0x9fbb:
            zh_list.append(text[i])
            en_list.append(word)
            word=''
            number_list.append(number)
            number=''
        elif ord(text[i])>=0x0041 and ord(text[i])<=0x005a or ord(text[i])>=0x0061 and ord(text[i])<=0x007a:
            word=word+text[i]          
            number_list.append(number)
            number=''
        elif  ord(text[i])>=0x0030 and ord(text[i])<=0x0039:
            number = number+text[i]
            en_list.append(word)
            word=''
        else :
            en_list.append(word)
            word=''
            number_list.append(number)
            number=''
    # zh_list=[x for x in zh_list if x != '']
    # en_list=[x for x in en_list if x != '']
    # number_list=[x for x in number_list if x != '']
    
    text_splited=zh_list+en_list+number_list
    text_splited=[x for x in text_splited if x != '']
    return text_splited,len(text_splited)
