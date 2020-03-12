# Calculate 50% of cash to necessities
def budget_50(monthly):
    percent = .50
    total = monthly * percent
    print(total)
    return total
# Calculate 30& of cash to wants
def budget_30(monthly):
    percent = .30
    total = monthly * percent
    print(total)
    return total
# Calculate 20% of cash to savings
def budget_20(monthly):
    percent = .20
    total = monthly * percent
    print(total)
    return total

# Get input from user how much goes to each account for essential
# Calculate total budget for essential
def budget_50_total(start_budget):

    total = start_budget
    house = int(input("How much is your housing for month: "))
    utilities = int(input("How much is your utilities this month 'gas, power, etc': "))
    grocery = int(input("How much is your groceries for month "))
    health = int(input("How much is your health insurance for the month "))
    car = int(input("How much is your car payment"))

    for i in range(1):
        data = house, utilities, grocery,health,car
        totals = sum(data)
        total -= totals

    return total

# Get input from user how much goes to each account for wants
# Calculate total budget for wants
def budget_30_total(start_budget):

    total = start_budget
    shopping = int(input("How much is your saving for shopping': "))
    hobbies = int(input("How much is your hobbies "))
    dining = int(input("How much is your dining "))

    for i in range(1):
        data = shopping, hobbies,dining
        totals = sum(data)
        total -= totals

    return total

# Get input from user how much goes to each account for savings
# Calculate total budget for saving
def budget_20_total(start_budget):
    total = start_budget
    three_month = int(input("How much is your saving for month': "))
    ira = int(input("How much is your ira "))

    for i in range(1):
        data = three_month, ira
        totals = sum(data)
        total -= totals

    return total



