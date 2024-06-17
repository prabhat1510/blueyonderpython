# Exception Handling with try-except and finally Block
try:
    x = int(input("Your number: "))
    res = 15 / x
    print("Result  - ", res)

except ValueError:
    print("You should have given either an character or a float")

except ZeroDivisionError:
    print("Infinity")
    
finally:
    print("There may or may not have been an exception.")
