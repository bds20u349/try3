from openpyxl import load_workbook

def ExportExcel(name, iops, avg):
    fn = 'C:/Users/kkdan/Desktop/git/project1/test.xlsx' #переменная для пути
    wb = load_workbook(fn) 
    ws = wb['data'] #название листа

    row = 1
    col = 1
    a = True

    while (a): #перебираем все именя дисков
        cell = ws.cell(row = row, column = col)
        if (cell.value != name) and (cell.value != None):
            col += 2
        else:
            if (cell.value == None): #Если имени диска ещё нет
                ws.cell(row = row, column = col).value = name
                
            cell = ws.cell(row = row+1, column = col)
            cell.value = iops
            
            cell = ws.cell(row = row+1, column = col+1)
            cell.value = avg
            
            a = False

    wb.save(fn)
    wb.close()
