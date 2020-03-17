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
def budget_50_total(start_budget, house, utilities, grocery, health, car):

    total = start_budget

    for i in range(1):
        data = house, utilities, grocery,health,car
        totals = sum(data)
        total -= totals

    return total

# Get input from user how much goes to each account for wants
# Calculate total budget for wants
def budget_30_total(start_budget, shopping, hobbies, dining):

    total = start_budget

    for i in range(1):
        data = shopping, hobbies,dining
        totals = sum(data)
        total -= totals

    return total

# Get input from user how much goes to each account for savings
# Calculate total budget for saving
def budget_20_total(start_budget, three_month, ira ):
    total = start_budget

    for i in range(1):
        data = three_month, ira
        totals = sum(data)
        total -= totals

    return total

# Validate if they have a goal or not
# If there is a goal do calculation for how long and amount the goal
# Print goal out with amount and time frame to user
def isGoal():

    goals = input("Do you have a goal to save for 'yes or no'")

    if goals.lower().startswith("yes"):

        amount = int(input("Please enter total amount of goal"))
        time_frame = int(input("When do you want to complete goal 'enter in months number'  "))
        g = goal_calculation(amount, time_frame)
        print(g, amount, time_frame, sep=" for ")

    elif goals.lower().startswith("no"):
        print("No goals for now")

# Calculate the total amount to save per month to complete goal
def goal_calculation(amount, time):
    a = amount
    t = time
    total = a / t
    return total




