from name_iops_avg import Output
from name_iops_avg import Checking_the_file_name
from name_iops_avg import File_name_sorting_function
from export_excel import ExportExcel
from openpyxl import load_workbook
import os

#-------------------Открываем файл и считываем оттуда пути к папкам с тестами и папке с excel----------------------------------------------------
config_file = open('Config.txt', 'r') #открываем файл, в торый записаны пути к каталогу с тестами и к котологу с excel файлом
name_of_the_folder_with_tests = config_file.readline()[13:-1] #первые 13 символов - это "folder name: ", а последний знак переноса "\n" файлом
name_of_the_folder_with_excel = config_file.readline()[11:-1] #первые 11 символов - это "file name: ", а последний знак переноса "\n"
config_file.close() #закрываем файл
#-----------------------------------------------------------------------------------------------------------------------------------------------



#---------Считываем имя интересуещей нас папки с тестами и имя интресуещего на excel файла. Сотавляем общий путь к excel файлу и файлам с тестами--------------
name_of_the_folder_with_tests = name_of_the_folder_with_tests.replace('\\', '/') #заменяем системные знаки \ на / в пути к папке с тестами
name_of_the_folder_with_excel = name_of_the_folder_with_excel.replace('\\', '/') #заменяем системные знаки \ на / в пути к папке с excel
folder_name = input('введите имя папки с тестами: ') #rw6d4-16kstrip1800slong
excel_name = input('введите имя файла excel: ') #test.xlsx
name_of_the_folder_with_tests = name_of_the_folder_with_tests + '/' + folder_name #Получаем общий путь внутрь каталога с тестами
name_of_the_folder_with_excel = name_of_the_folder_with_excel + '/' + excel_name #Получаем общий путь к файлу excel
catalog_with_tests = os.listdir(name_of_the_folder_with_tests) #получаем список названий всех файлов внутри каталога
catalog_with_tests.sort(key=File_name_sorting_function)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------



wb = load_workbook(name_of_the_folder_with_excel)#получаем доступ к excel файлу
if folder_name in wb.sheetnames: #если лист с таки именем уже существует, то удаляем его и создаём снова, тем самым отчищаем его от прошлых значений
    wb.remove(wb[folder_name])
ws = wb.create_sheet(folder_name) #создаём новый лист

for file_name in catalog_with_tests: #берём по очереди все файлы с тестами
    if Checking_the_file_name(file_name): #проверка на соответствие имени файла шаблону вида "fio-*-*.log"
        name, iops, avg = Output(name_of_the_folder_with_tests + '/' + file_name) #Получение из файла с результатом теста имени тестируемого диска, отправленных iops и результата evg
        ExportExcel(ws, name, iops, avg) #записываем данные в excel
wb.save(name_of_the_folder_with_excel) #сохраняем изменения в лист excel
wb.close() #закрываем лист excel
