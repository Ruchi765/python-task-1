print("~~~~~~~~~~~~~minicalculator~~~~~~~~~~~~~~~~~~")
num1=int(input("inter a number here:"))
num2=int(input("input a another number here:"))
print(""""
      press 1 for addition
      press 2 for substraction
      press 3 for multiplication
      press 4 for division
      press 5 for modulo""")
choice = int(input("enter a choice between 1-5:")) 
if choice == 1:
    print ("the addition of given two numbers is" , num1+num2)
elif choice == 2:
    print ("the substraction of given two number is", num1-num2)
elif choice == 3:
    print  ("the multiplication of given two number is" , num1*num2)
elif choice == 4:
    print  ("the division of given two number is" , num1/num2)
elif choice == 5:
    print ("the modulo of given two number is",num1%num2)
else:
    print ("invailid choice")


    