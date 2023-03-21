#while loop to keep prompting until - 1 is entered

percentage = float(input("Enter the percentage:"))

    
while (percentage != -1):
    print("Please enter -1")
    percentage = float(input(""))
    break

# to allow for rounding, if statements less than .5 of number to allow rounding up
# need to # OUT While Loop to see it working
if percentage < 0 or percentage > 100: 
 print ("Please enter a number between 0 and 100")
elif percentage < 39.5: # use less than 39.5 to allow for rounding
 print ("Fail")
elif percentage < 49.5: # use less than 49.5 to allow for rounding
 print ("Pass")
elif percentage < 59.5: # use less than 59.5 to allow for rounding
 print ("Merit1")
elif percentage < 69.5: # use less than 69.5 to allow for rounding
 print ("Merit2")
else: # the only option left is between 69.5 and 100
 print ("Distinction")
