



# Exception Handling
print("Exception handling")
try:
    a=int(input("First Number: "))
    b=int(input("Second Number: "))
    c=a/b
    print ("Output:", c)
#except Exception:      
except ZeroDivisionError:
    print("Number can't be Divided by 0")
except ValueError:
    print("Enter the appropriate number")    
except Exception:
    print("Error occurred in your program give appropriate input")