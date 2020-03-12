# Import
import budget_calc
from output_excel import create_workbook

# Get total monthly cash from check
while True:
    try:
        monthly = int(input("How much is your monthly cash flow " ))
        if monthly == 0:
            print("Please enter a non-zero number")
        elif monthly < 0:
            print("Please enter a positive number")
        break
    except ValueError:
        print("Please enter a valid number")

# Calculate budget for essentials

essential = budget_calc.budget_50(monthly) # Calculates essential percentage

print(budget_calc.budget_50_total(essential))# Calculates total bills returns left over

saving = budget_calc.budget_20(monthly)  # Calculates saving percentage

print(budget_calc.budget_20_total(saving)) # Calculates total savings returns left over

want = (budget_calc.budget_30(monthly)) # Calculates wants percentage

print(budget_calc.budget_30_total(want)) # Calculates total wants and returns left overs

print(essential, saving, want)
# Save to a pdf file for all information
#create_workbook()
