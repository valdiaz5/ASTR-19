#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:12:26 2026

@author: valeriediaz
"""

#declare a class to describe the characteristics of an animal
class Animal:
    
    #initialization function with all paramaters of characteristics 
    def __init__(self, length_arms, length_legs, number_eyes, tail, furry):
        ''' 
            inputs:
                length_arms: float, tells the length of the arms of an animal 
                length_legs: float, tells the elgnth of the legs 
                number_eyes: int, tells the number of eyes the animal has 
                tail:boolean, has a tail? yes/true, no/false
                furry: boolean, has a tail? yes/true, no/false
        '''
        
        self.length_arms = length_arms
        self.length_legs = length_legs
        self.number_eyes = number_eyes
        self.tail = tail
        self.furry  = furry

    def print(self):
        # this function prints out the characteritics of the animal 
        
        print(f'Arm length: {self.length_arms} in')
        print(f'Leg length: {self.length_legs} in')
        print(f'Number of eyes: {self.number_eyes}')
        print(f'Does it have a tail? {self.tail}')
        print(f'Is it furry? {self.furry}')

#this instance prints out the characteristics of my favorite animal a sea otter 
sea_otter = Animal(10.2, 10.2, 2, True, True)
sea_otter.print()
        

