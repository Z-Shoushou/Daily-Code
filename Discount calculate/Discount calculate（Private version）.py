# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:15:09 2018

@author: 兽兽
"""

Real_pay = float(input('Please input your Amount of real pay: '))
Discount_amount  = float(input('Pleas input your discount amount : ')) #Actual total value of goods (including lunch box fee)
Box_fee = float(input('Please input your meal mox fee : '))
Delivery_cost = float(input('Please input your delivery cost : '))
Personal_input = input('Please input your personal consumptions(Comma separated): ').split(',')

Number_people = float(len(Personal_input))
Original_pay = Real_pay + Discount_amount
Ratio = Real_pay / Original_pay

for index in range(len(Personal_input)) :
    per_delivery = float(Delivery_cost / Number_people)
    Personal_pay = float(Personal_input[index]) + Box_fee + per_delivery
    per_pay = float(Real_pay) / float(Original_pay) * float(Personal_pay)
    print ('Your personal real pay is ' + str(per_pay) + '.')
