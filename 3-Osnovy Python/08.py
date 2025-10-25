#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:58:18 2025

@author: danny
"""

# должно быть строковое содержимое списка, иначе мы получаем ошибку Und name

words = ['cat','window', 'defenestrate']

for word in words:
    print('Слово: {} Букв: {}'.format(word, len(word)))
