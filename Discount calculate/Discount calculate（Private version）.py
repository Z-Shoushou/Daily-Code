# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:15:09 2018

@author: 兽兽
"""

Real_pay = float(input('Please input your Amount of real pay: '))
Commodity_price = float(input('Pleas input your commodity price: '))
Meals_fee = float(input('Please input your meal fee : '))
Delivery_cost = float(input('Please input your delivery cost : '))
Personal_input = input('Please input your personal consumptions(Comma separated): ').split(',')

Number_people = float(len(Personal_input))
Original_pay = Meals_fee * Number_people + Delivery_cost + Commodity_price
Ratio = Real_pay / Original_pay


for index in range(len(Personal_input)) :
    per_delivery = float(Delivery_cost / Number_people)
    Personal_pay = float(Personal_input[index]) + Meals_fee + per_delivery
    per_pay = float(Real_pay) / float(Original_pay) * float(Personal_pay)
    print ('Your personal real pay is ' + str(per_pay) + '.')
