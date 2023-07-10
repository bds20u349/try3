from name_iops_avg import Output
from name_iops_avg import Address_format
from export_excel import ExportExcel
import os

#catalog_name = input('введите путь к файлу: ')
catalog_name = "C:/Users/kkdan/Desktop/git/project1/rw6d4-16kstrip1800slong"
catalog_name = catalog_name.replace('\\', '/')
catalog = os.listdir(catalog_name)

for file_name in catalog:
    name, iops, avg = Output(catalog_name + '/' + file_name)
    if name != 'Error':
        ExportExcel(name, iops, avg)
