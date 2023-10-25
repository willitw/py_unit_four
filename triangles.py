#twig willaims
# randomly picks three numbers from 1-10 and sees if they can make a triangle

import random

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def main():
    a = random.randint(1, 10)  
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    print(f"{a} {b} {c}")

    if is_triangle(a, b, c):
        print("This can make a triangle!!!!")
    else:
        print("These lengths cannot form a triangle")

if __name__ == "__main__":
    main()
