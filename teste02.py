from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]

planilha['A1'] = "Nome"
planilha['B2'] = "Quantidade"


wb.save("C:\\Users\\Anaê\\Desktop\\roles.xlsx")