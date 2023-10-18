# even_odd.py
# Twig Williams
# 10/18/23

def even_or_odd(number):
    if number % 2 == 0:
        return str(number) + " is an even number"
    if number % 2 == 1:
        return str(number) + " is an odd number"

def main():
    user_input = input("Please enter a number: ")
    number = int(user_input)
    result = even_or_odd(number)
    print(result)

if __name__ == "__main__":
    main()




#shabingus