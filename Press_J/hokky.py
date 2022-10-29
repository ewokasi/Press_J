from random import randint
import re

import requests
data_base = open(r"hokky.txt", "r", encoding="UTF-8")
all_hokky = data_base.read().split('\n')
data_base.close()

def gen():
    res = ""
    for i in range(2):
        res = res + all_hokky[randint(0, len(all_hokky)-1)]+'\n'
    res = res + all_hokky[randint(0, len(all_hokky) - 1)]
    if res[len(res)-1] not in ".!?":
        res =res + "."
    res =res+"\n"
    res = res+'\n'+'\t'+f"@От Меть Ся, {randint(1,2000)} до н.э"
    return res


def pic_gen(message):
    req = requests.get("https://yandex.ru/images/search?text=" + message)
    ph_links = list(filter(lambda x: '.jpg' in x, re.findall('''(?<=["'])[^"']+''', req.text)))
    ph_list = []
    for i in range(len(ph_links)):
        if (ph_links[i][0] == "h"):
            ph_list.append(ph_links[i])
    del ph_links
    return ph_list[randint(0, len(ph_list)-1)]

