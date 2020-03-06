# Calculate 50% of cash to necessities
def budget_50(monthly):
    percent = .50
    total = monthly * percent
    result = monthly - total
    return result
# Calculate 30& of cash to wants
def budget_30(monthly):
    percent = .30
    total = monthly * percent
    result = monthly - total
    return result
# Calculate 20% of cash to savings
def budget_20(monthly):
    percent = .20
    total = monthly * percent
    result = monthly - total
    return result