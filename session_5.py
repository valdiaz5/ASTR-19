#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:53:42 2026

@author: valeriediaz
"""

import numpy as np
from astropy.table import Table

#function creates a list of values for sinx
def sin_data(x1,x2, entries):
    '''
        inputs: x1- starting x value 
                x2- ending x value 
                entries- the number of entries we want of sinx
                
        output: sinx data in a list 
    
    '''
    x = np.linspace(x1, x2, entries)
    y = np.sin(x)
    return x, y

#this fucntion tabulates the data from the first function 
def main():
    x, y = sin_data(0, 2*np.pi, 1000)
    table = Table([x, y], names=('x', 'sin(x)'))
    print(table)

if __name__ == "__main__":
    main()