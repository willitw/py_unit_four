def calculate_bonus(years_worked, annual_salary):
    if years_worked > 5:
        bonus = annual_salary * 0.05
        total_salary = annual_salary + bonus
        return total_salary

def main():
    salary = int(input("What is your current salary? "))
    years_worked = int(input("How many years have you worked here? "))

    total_salary = calculate_bonus(years_worked, salary)

    print("Your total salary is ${:.2f}".format(total_salary))

if __name__ == "__main__":
    main()
