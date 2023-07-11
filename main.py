from name_iops_avg import Output
from name_iops_avg import Checking_the_file_name
from export_excel import ExportExcel
import os

file = open('Config.txt', 'r') #открываем файл, в торый записаны пути к каталогу с тестами и к котологу с excel файлом
catalog_name = file.readline()[13:-1] #первые 13 символов - это "folder name: ", а последний знак переноса "\n"
file.close() #закрываем файл
catalog_name = catalog_name.replace('\\', '/') #заменяем системные знаки \ на /
folder = input('введите имя папки: ') #rw6d4-16kstrip1800slong
catalog_name = catalog_name + '/' + folder #Получаем общий путь внутрь каталога
catalog = os.listdir(catalog_name) #получаем список названий всех файлов внутри каталога

for file_name in catalog:
    if Checking_the_file_name(file_name): #проверка на соответствие имени файла шалону вида "fio-*-*.log"
        name, iops, avg = Output(catalog_name + '/' + file_name) #Получение из файла с результатом теста имени тестируемого диска, отправленных iops и результата evg
        ExportExcel(name, iops, avg) #записываем данные в excel
