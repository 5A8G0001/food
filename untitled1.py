# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 01:14:32 2021

@author: USER
"""
import random



dic = {
    1:"麵的時代",
    2:"我家麵店",
    3:"同心緣",
    4:"吃到寶",
    5:"阿哲",
    6:"丹丹",
    7:"廣島",
    8:"臭臉",
    9:"越南",
    10:"火雞肉飯",
    11:"肉粽",
    12:"飯糰"
}

for i in range(10):
    x = 0
    for j in range(1000):
        x = random.randint(1,9)
    print(dic[x])
