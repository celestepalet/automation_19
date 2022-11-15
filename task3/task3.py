import os
import csv
import shutil


#leer el csv y poner en listas su contenido
with open('students.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    list_students_names=[]
    list_students_id=[]
    for row in spamreader:
        student=' '.join(row).split(',')
        list_students_names.append(student[0])
        list_students_id.append(student[1])

#eliminar primer valor
list_students_names.pop(0)
list_students_id.pop(0)

#crear carpetas
for name in list_students_names:
    if os.path.exists(name)==False:
        os.mkdir(name)

#datos de rutas
origin = './data'
destination_pdf = './Tutorials'
destination_directories = "./Games"

#lista con lo que contiene la carpeta
files = os.listdir(origin)

#mover archivos
for file in files:
    if os.path.isdir(os.path.join(origin,file)):
        new_path= shutil.move(f"{origin}/{file}", destination_directories)
        print(f'The directory {file} is now in {destination_directories}')
    elif os.path.isfile(os.path.join(origin, file)) and file.endswith('.pdf'):
        new_path= shutil.move(f"{origin}/{file}", destination_pdf)
        print(f'The file {file} is now in {destination_pdf}')
        