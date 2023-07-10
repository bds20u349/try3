def Chislo(line, start, typ):
    number = ''
    flag = True
    while flag:
        simvol = line[start]
        if (simvol == ',') or (simvol == ' '):
            flag = False
        else:
            number += simvol
        start += 1

    mnogitel = 1
    if number[-1] == 'k':
        mnogitel = 1000
        number = number[:-1]
    
    if typ == 'int':
        number = int(number)
    if typ == 'float':
        number = float(number)*mnogitel
    if typ == 'str':
        number = number
    return number

def Output(file_name):
    file = open(file_name, 'r')
    try:
        a = True
        while a:
            line = file.readline()
    
            x = line.find("filename")
            if x != -1:
                name = Chislo(line, x+14, 'str')
            
            x = line.find("IOPS")
            if x != -1:
                iops = Chislo(line, x+5, 'float')
                
            x = line.find(" lat")
            if x != -1:
                avg = Chislo(line, line.find("avg")+4, 'float')
                a = False
            if line == '':
                a = False
                name = 'Errore'
                iops = -1
                avg = -1
        return name, iops, avg
    finally:
       file.close()

def Address_format(catalog_name):
    x = catalog_name.find("\\")
    while x != -1:
        catalog_name[x] = '1'
        x = catalog_name.find("\\")
    return catalog_name
