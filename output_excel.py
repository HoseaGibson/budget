# imports
import xlwt
from xlwt import Workbook
# Write information to excel file

wb = Workbook()

sheet1 = wb.add_sheet("Sheet 1")

sheet1.write(1,0, "ESSENTIAL")
# Store values in the correct cell