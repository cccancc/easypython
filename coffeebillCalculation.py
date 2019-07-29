# -*- coding: utf-8 -*-
# # Project: Cost determination of sending out coffee
# Name: 
# Date: 2019/7/28
# Description: This program will allow the cafe and customerrs to
#              calculate the cost of sending out coffee.


def main():
     # initialize output float variables
     subTotal=0.00
     shiphandleCost=0.00
     deliverCost=0.00
     tax=0.00
     total=0.00

     # initialize output array
     arrCoffeeType=["Jonestown Brew","Plymouth Jolt"]
     arrCityState=["Washingto,California,Texas","Oregon,Florida","other region"]
     arrDeliverType=["Overnight","2-Day","Standard"]
     arrPaymentMethod=["Paypal","Credit Card","Check"]

     # initialize user input variables and ask for number input
     intCoffee=int(input("What kinds of coffee you want to order, 1:Jonestown Brew; 2:Plymouth Jolt Enter you choice:"))
     intPound=int(input("How many would you like to order?:"))
     intCityState=int(input("Please enter you location abbreviated, 1:WA,CA,TE; 2:OR,FL 3:etc.):"))
     intDeliverType=int(input("Please choose your delivery type (1. Overnight; 2. 2-Day; 3.Standard):"))
     intPayMethod=int(input("Please choose your payment method (1.Paypal; 2. Credit Card; 3. Check):"))

     # call Sub-Total function
     subTotal=subtotal(intCoffee,intPound)

     # call shiphandling determine function
     shiphandleCost=shiphandleDetermine(intPound)

     # call tax determine function
     tax=taxDetermine(intCityState,subTotal)

     # call delivery cost determine function
     deliverCost=deliveryCostDetermine(intDeliverType)

     # calculate payment cost
     if intPayMethod==1:
          paymentCost=subTotal*0.03
     elif intPayMethod==2:
          paymentCost=subTotal*0.05
     else:
          paymentCost=-subTotal*0.02
     
     # summary total
     total=subTotal+shiphandleCost+deliverCost+paymentCost+tax

     # display intCoffee, intPound,subTotal,shiphandleCost,deliverCost,CityState,DeliverType,PayMethod,tax amd Total
     print ('********************************************')
     print("Your Order List:")
     print ("Ordered coffee type is: "+ arrCoffeeType[intCoffee-1])
     print ("Number of pounds ordered is: "+ str(intPound))
     print ("Sub-Total (price * quantity) is: "+"$"+ str(subTotal))
     print ("Shipping & Handling cost is: "+"$"+ str(shiphandleCost))
     print ("Delivery cost is: " +"$"+str(deliverCost))
     print ("Sending to: "+arrCityState[intCityState-1])
     print ("Delivery type is: "+arrDeliverType[intDeliverType-1])
     print ("Payment method is: "+arrPaymentMethod[intPayMethod-1])
     print ("Tax is: "+"$"+str(tax))
     print ("*******************************************")
     print ("=>          Total is: "+"$"+str(total))


# calculate sub-total cost if varCoffee= 1 or 2
def subtotal(intCoffee,intPound):
     subTotal=0.00
     # if intCoffee =1
     if intCoffee == 1:   
          subTotal=intPound*10.5
          return subTotal
     # if intCoffee =2
     elif intCoffee== 2:
          subTotal=intPound*16.95
          return subTotal 
                
     else:
          print("Error input!")

# calculate shipping and handle costs 
def shiphandleDetermine(intPound):
     shiphandleCost=0.00
     shiphandleCost=intPound*0.93+2.5
     return shiphandleCost

# calculate tax costs
def taxDetermine(intCityState,subTotal):
     tax=0.00
     # if strCityState= "WA"or "CA" or "TE"
     if intCityState==1:
          tax=subTotal*0.09
     # if strCityState= "OR" or "FL"
     elif intCityState==2:
          tax=0.00
     else:
          tax=subTotal*0.07
     return tax

# calculate delivery cost
def deliveryCostDetermine(intDeliverType):
     deliverCost=0.00
     if intDeliverType==1:
          deliverCost=20.00
     elif intDeliverType==2:
          deliverCost=13.00
     else: 
          return deliverCost
     return deliverCost       
          
main()
