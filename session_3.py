#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:03:30 2026

@author: valeriediaz
"""
#defines a function of x, that returns x**3 +8
def f(x):
    
    y = x**3 + 8
    
    return y
   
#defines a function that prints f(9) and if its >27 prints Yay 
def main():
    
    print(f(9))
    if f(9) > 27:
        print("YAY!")
        
if __name__=="__main__":
    main()
    
  