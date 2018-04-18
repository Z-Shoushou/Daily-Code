# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:15:09 2018

@author: 兽兽
"""

Real_pay = float(input('Please input your Amount of real pay: '))
Original_pay = float(input('Pleas input your original pay: '))

Ratio = Real_pay / Original_pay

Personal_input = input('Please input your personal consumptions(Comma separated): ').split(',')

for index in range(len(Personal_input)) :
    per_pay = float(Real_pay) / float(Original_pay) * float(Personal_input[index])
    print ('Your personal real pay is ' + str(per_pay) + '.')
