#twig w
#10/20/23
#returns larer number and tests some exaples
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

#tests
print(max(7, 12))  #first number bigger
print(max(3, -5))  #second number bigger
print(max(-2, -8))  #one number negative
print(max(-4, -4))  #both numbers negative
print(max(9, 9))  #both numbers the same


