principal=float(input("enter the principal amount:"))
years=int(input("enter the number of years"))

#the rate
rate=16/100
#calculate the compound interest
Amount=principal*(1+rate)**years

print("the total amount is ",Amount)
   
