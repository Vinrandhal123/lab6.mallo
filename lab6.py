age = int(input("enter your age"))
member = (input(" enter yes or no if you are in membership"))
if age < 18:
 if member == "yes":
    print("total fee is  is 450.00")
if member == "no":
    print("total fee is 650.00")
elif age >=18 and age <=65:
    if member == "yes":
      print("total fee is 550.00")
    if member == "no":
     print("total fee is 750")
elif age > 65:
     if member == "yes":
       print("total fee is 400")
     if member == "no":
         print("total fee is 600")
    