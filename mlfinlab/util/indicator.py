# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:41:46 2020

@author: Wei_X
"""

import pandas as pd

def bband(data: pd.DataFrame, span0: int = 50, width: int = 1):
    '''
    Basic bollinger band
    
    params: DataFrame => entire dataframe which close price resides
    params: int => span0 is how many to roll
    params: int => width to set 
    '''
    
    data['ma'] = data['close'].rolling(span0).mean()
    std = data['close'].rolling(span0).std() * width
    
    data['upper'] = data['ma'] + std
    data['lower'] = data['ma'] + std
    
    return data