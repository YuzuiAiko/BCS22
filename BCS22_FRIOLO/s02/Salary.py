class bonusCalculator:
    def __init__(self, years_of_service,salary):
        self.years_of_service = years_of_service
        self.salary = salary

    def calculate_bonus(years_of_service, salary):
        bonus_percentage = 0

        if years_of_service >= 5:
            if years_of_service >= 20:
                bonus_percentage = 200
            elif years_of_service >= 15:
                bonus_percentage = 150
            elif years_of_service >= 10:
                bonus_percentage = 100
            else:
                bonus_percentage = 5

        bonus_amount = (bonus_percentage / 100) * salary
        return bonus_amount

    name_User = input("Enter Name: ")
    years_of_service = int(input("Enter years of service: "))
    salary = float(input("Enter salary: ₱"))
    bonus = calculate_bonus(years_of_service, salary)
    print("Name: ",name_User)
    print(f"Longevity Bonus: ₱{bonus:.2f} ")
    print("Final Salary: ₱", bonus + salary)
    print("Running Time: 0(1)")