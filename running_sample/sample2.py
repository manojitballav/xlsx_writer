#importing the library function for the spreadsheet
import xlsxwriter

#creating a workbook and saving it in a specific directory that we want
workbook = xlsxwriter.Workbook('C:\\Users\\Xiaomi\\Documents\\xlsx_writer\\running_sample\\sample2.xlsx')
#creating a worksheet in the workbook
worksheet = workbook.add_worksheet()

#Data what we want to write in the excel sheet
expenses = (['Rent',5500],['Food',3000],['Bills',4000])

#initialising the rows and coloumns to zero since they start with zero in spreadsheet
row = 0
col = 0


#writing data in the worksheet by iterating over the Data that need to be written in the spreadsheet
for item,cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost)
    row=row+1

#Calculating the total using a formula
worksheet.write(row,0,'Total')
worksheet.write(row,1,'=SUM(B1:B3)')

#completing the operation by closing the workbook
workbook.close()

print "Operation completed succesfully"