#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:49:23 2025

@author: danny
"""

try:
    name = input('Введите своё имя ')
    age = int(input('Введите свой возраст '))

    print('Меня зовут {}, а мой возраст {}'.format(name, age))
    
except ValueError:
    print('В возраст нельзя вводить буквы!')

finally:
    print('Всего доброго, {}'.format(name))
    