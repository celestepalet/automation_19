import os
import csv
import shutil

# read csv y create list
with open('students.csv') as csvfile:
    students_file = csv.reader(csvfile,delimiter=' ')  #separete elements in empty spaces
    list_students_names = []
    list_students_id = []
    for row in students_file:
        student = '_'.join(row).lower().split(',')   #join in one str, separate the elements whit '_'
        list_students_names.append(student[0])       #split separete the elements when ','
        list_students_id.append(student[1])

# eliminate first value from the lists
list_students_names.pop(0)
list_students_id.pop(0)

# create files
for name in list_students_names:
    if os.path.exists(name) == False:
        os.mkdir(name)

# paths
origin = './data'
destination_pdf = './tutorials'
destination_directories = "./games"

# list whit the folder contect
files = os.listdir(origin)

# move files
for file in files:
    if os.path.isdir(os.path.join(origin,file)):    #.isdir(path)
        new_path = shutil.move(f"{origin}/{file}", destination_directories)
    elif os.path.isfile(os.path.join(origin, file)) and file.endswith('.pdf'):
        new_path = shutil.move(f"{origin}/{file}", destination_pdf)
