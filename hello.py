# -*- coding: utf-8 -*-
# # Project: Cost determination of sending out coffee
# Name: 
# Date: 2019/7/28
# Description: This program will allow the cafe and customerrs to
#              calculate the cost of sending out coffee.

# initialize output variables
subTotal=0.0
shiphandleCost=0.0
deliverCost=0.0
tax=0.0
# initialize user input variables and ask for input
strCoffee=str(input("What kinds of coffee you want to order, A:Jonestown Brew; B:Plymouth Jolt; C:Both? Enter you choice:"))
intPound=int(input("How many would you like to order?:"))
strCityState= str(input("Please enter you location abbreviated (WA,CA,TE,OR,FL,etc.):"))
strDeliverType=str(input("Please choose your delivery type (1. Overnight; 2. 2-Day; 3.Standard):"))
strPayMethod=str(input("Please choose your payment method (1.Paypal; 2. Credit Card; 3. Check):"))
# coffeeType=[Jonestown Brew, Plymouth Jolt]

def main():
 
# calculate sub-total cost if varCoffee= A or B
    if (strCoffee == "A" | "B" | "C"):   
        elif strCoffee =="A":
             intPound=int(input("How many would you like to order?:"))
             subTotal=intPound*10.5
        elif strCoffee=="B":
             intPound=int(input("How many would you like to order?:"))
             subTotal=intPound*16.95 
        elif strCoffee=="C":
             intPound1=int(input("How many of Jonestown Brew would you like to order?:"))
             intPound2=int(input("How many of Plymouth Jolt would you like to order?:")) 
             subTotal=intPound1*10.5+intPound2*16.95  
        else:
             print("Error input!")
             strCoffee=str(input("What kinds of coffee you want to order, A:Jonestown Brew; B:Plymouth Jolt; C:Both? Enter you choice:"))
             print(strCoffee+subTotal)
main()

print('hello world')
#Washington, California and Texas Oregon or Florida