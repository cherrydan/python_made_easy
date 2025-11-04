#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 23:45:30 2025

@author: danny
"""
VALUE = 111111

res = VALUE // 100000
res += VALUE // 10000 % 10
res += VALUE // 1000 % 10
res += VALUE // 100 % 10
res += VALUE // 10 % 10
res += VALUE % 10

print('Сумма разрядов числа {} равняется {}'.format(VALUE, res))