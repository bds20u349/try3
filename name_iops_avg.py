def Reading_the_necessary_information(line, start, typ): #функция, считывающая из строки line подстроку, начинающююся с индекса start и заканчивающуюся пропуском или запятой
    number = ''
    flag = True
    while flag: #пока не " " или "," считываем строку
        simvol = line[start]
        if (simvol == ',') or (simvol == ' '):
            flag = False
        else:
            number += simvol
        start += 1

    mnogitel = 1 #если это число, оканчивающееся на k или m, то домножим его на 1000 и 1000000 соостветственно
    if (number[-1] == 'k') and (typ != 'str'):
        mnogitel = 1000
        number = number[:-1] #вырежим последний символ, т.к. он не является числом
    elif (number[-1] == 'm') and (typ != 'str'):
        mnogitel = 1000000
        number = number[:-1]

    #перевод результата в нужный формат
    if typ == 'int':
        number = int(number)
    if typ == 'float':
        number = float(number)*mnogitel
    if typ == 'str':
        number = number
    return number

def Checking_the_file_name(file_name): #проверка на соответствие имени файла шалону вида "fio-*-*.log"
    x = file_name[4:].find('-')+4 #Ищем индекс второго знака "-" между подстроками "fio-" и ".log"
    if (x != -1) and (file_name[:4] == 'fio-') and (file_name[-4:] == '.log') and (file_name[4:x].isdigit()) and (file_name[x+1:-4].isdigit()): #проверяем, чтобы имя файла начиналось на "fio-", заканчивалось на ".log", присутствовал второй знак "-" и между этими тремя подстроками находились числа
        return True
    else:
        return False

def Output(file_name):
    file = open(file_name, 'r')
    a = True
    try:
        while a:
            line = file.readline()
    
            x = line.find("filename")
            if x != -1:
                name = Reading_the_necessary_information(line, x+14, 'str')
            
            x = line.find("IOPS")
            if x != -1:
                iops = Reading_the_necessary_information(line, x+5, 'float')
                
            x = line.find(" lat")
            if x != -1:
                if line.find("usec") != -1:
                    mnogitel = 1000
                else:
                    mnogitel = 1
                avg = Reading_the_necessary_information(line, line.find('avg')+4, 'float')/mnogitel
                a = False
        return name, iops, avg
    finally:
       file.close()

