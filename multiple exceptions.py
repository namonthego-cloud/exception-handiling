try:
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter seconed number:"))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print ("Divison by zero is error!")

except ValueError:
    print ("please enter a valid whole numbers")

except:
    print("wrong input ")

else:
    print("no exceptions")
finally:
    print("this will excute no matter what")