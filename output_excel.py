# imports
import xlwt
from xlwt import Workbook

# Write information to excel file
# define a function to create an excel sheet
def create_workbook(house, utilities, grocery, health, car, three_month, emer, shop, food,hobby):

    wb = Workbook()

    # Styles for lettering  and heading and subcat.
    style = xlwt.easyxf("font: bold 1, color red, height 300;")
    style2 = xlwt.easyxf("font: bold 1, color blue, height 200;")

    sheet1 = wb.add_sheet("Sheet 1")

    # Store values in the correct cell
    # Create cells for essential and categories listed
    sheet1.write(0,0, "ESSENTIAL", style)
    sheet1.write(1, 0, "HOUSING", style2)
    sheet1.write(2, 0, "UTILITIES", style2)
    sheet1.write(3, 0, "GROCERIES", style2)
    sheet1.write(4, 0, "HEALTH INSURANCE", style2)
    sheet1.write(5, 0, "CAR PAYMENT", style2)
    sheet1.write(1, 3, house)
    sheet1.write(2, 3, utilities)
    sheet1.write(3, 3, grocery)
    sheet1.write(4, 3, health)
    sheet1.write(5, 3, car)

    # Create cells for save and categories listed
    sheet1.write(7,0, "SAVE", style)
    sheet1.write(8, 0, "401K/IRA", style2)
    sheet1.write(9, 0, "EMERGENCY", style2)
    sheet1.write(8, 3, three_month)
    sheet1.write(9, 3, emer)

    # Create cells for wants and categories listed
    sheet1.write(11,0, "WANTS", style)
    sheet1.write(12, 0, "SHOPPING", style2)
    sheet1.write(13, 0, "DINING OUT", style2)
    sheet1.write(14, 0, "HOBBIES", style2)
    sheet1.write(12, 3, shop)
    sheet1.write(13, 3, food)
    sheet1.write(14, 3, hobby)

    # Create cells for goals and categories listed
    sheet1.write(1, 8, "GOALS", style)
    sheet1.write(2, 8, "GOAL SAVING", style2)

    # Save file
    wb.save("xlwt example.xls")


