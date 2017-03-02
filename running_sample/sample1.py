#importing the library function for the spreadsheet
import xlsxwriter

#creating a workbook and saving it in a specific directory that we want
workbook = xlsxwriter.Workbook('C:\\Users\\Xiaomi\\Documents\\xlsx_writer\\running_sample\\sample1.xlsx')
#creating a worksheet in the workbook
worksheet = workbook.add_worksheet()

#writing data in the worksheet
worksheet.write('A1','mono')
worksheet.write('A2','mona')

#completing the operation by closing the workbook
workbook.close()

print "Opeartion completed succesfully"