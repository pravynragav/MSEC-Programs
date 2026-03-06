temp=input("Enter temperature status:")
Humidity=input("Enter Humidity Status:")
if(temp=="warm") and (Humidity=="dry"):
   print("you can play basketball")
elif(temp=="warm") and (Humidity=="humid"):
   print("you can play tennis")
elif(temp=="cold") and (Humidity=="dry"):
   print("you can play cricket")
elif(temp=="cold") and (Humidity=="humid"):
   print("you can do swimming")
else:
   print("Enter Valid status")
