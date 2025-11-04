#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 15:56:50 2025

@author: danny
"""

def calculate_market_shares(sales_data):
    """
    
    расчитывает рыночную долю для каждого магазина, и общую сумму рыночных 
    долей
    

    Parameters
    ----------
    sales_data : dict
        ключ - назввние магазина (str)
        значение - месячные продажи

    Returns
    -------
    turle - рвночная доля каждого магазина (%)
    общая сумма рыночных долей (%)
    общие продажи на рынке ($)
    

    """
    
    print('Исходные данные о месячных продажах:')
    
    # сбор данных
    for store, sales in sales_data.items():
        print('Магазин {}: {}$ '.format(store, sales))
        
    
    # общая доля на рынке
    total_market_sales = sum(sales_data.values())
    
    # print('Общвя доля на рынке {}$'.format(total_market_sales))
    
    # расчёт доли каждого магазина
    market_shares = {}
    
    for store, sales in sales_data.items():
        share = (sales / total_market_sales) * 100
        market_shares[store] = round(share, 2)
        
        # print('Магазин {} рыночная доля {:.2f}%'
          #    .format(store, market_shares[store]))
        
    # сумма рыночных долей 
    total_market_shares = sum(market_shares.values())
    
    # print('Общая доля на рынке ожидаемо {}%'.format(total_market_shares))
    
    return market_shares, total_market_shares, total_market_sales
        



sales_data = {
    'A': 6500,
    'B': 8000,
    'C': 12000,
    'D': 4900,
    'E': 5600
    }

if __name__ == '__main__':  
    market_shares, total_shares, total_sales = calculate_market_shares(sales_data)
    print('Общая капитализация ($):{}'.format(total_sales))
    print('\nВозвращенные рыночные доли(%): {}'.format(market_shares))
    print('\nВозвращенная общая доля (%)', total_shares)
