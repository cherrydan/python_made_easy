#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 17:02:46 2025

@author: danny
"""

# выводит первые 8 чисел ряда Фибоначчи. Ошибка в отсутствии отступов в теле
# цикла while

a, b = 0, 1
while a < 15:
    print(a, end=', ')
    a, b = b, a + b