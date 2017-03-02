#importing the library function for the spreadsheet
import xlsxwriter

workbook = xlsxwriter.Workbook('C:\\Users\\Xiaomi\\Documents\\xlsx_writer\\running_sample\\test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1','mono')
worksheet.write('A2','mona')

workbook.close()