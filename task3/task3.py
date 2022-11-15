import os
import csv
import shutil

# leer el csv y poner en listas su contenido
with open('students.csv') as csvfile:
    students_file = csv.reader(csvfile,delimiter=' ')  # separa el csv en lista, separa los elementos d ela lista cuando hay espacio vacio
    list_students_names = []
    list_students_id = []
    for row in students_file:  # split hace la lista separando cuando hay ,
        student = '_'.join(row).lower().split(',')  # join junta todo en un str, a los elementos de la lista los separa con espacio vacio
        list_students_names.append(student[0])
        list_students_id.append(student[1])

# eliminar primer valor
list_students_names.pop(0)
list_students_id.pop(0)

# crear carpetas
for name in list_students_names:
    if os.path.exists(name) == False:
        os.mkdir(name)

# datos de rutas
origin = './data'
destination_pdf = './tutorials'
destination_directories = "./games"

# lista con lo que contiene la carpeta
files = os.listdir(origin)

# mover archivos
for file in files:  # path.join une dos los argumentos separando por /
    if os.path.isdir(
            os.path.join(origin, file)):  # path.isdir pregunta si el argumento es una carpeta, tengo que darle una ruta
        new_path = shutil.move(f"{origin}/{file}", destination_directories)  # (ruta del archivo , ruta destino)
    elif os.path.isfile(os.path.join(origin, file)) and file.endswith('.pdf'):
        new_path = shutil.move(f"{origin}/{file}", destination_pdf)
