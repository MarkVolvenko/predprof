import csv
with open('students.csv',encoding='utf8') as file:
    reader=list(csv.reader(file,delimiter=','))[1:]
    sum_class={}
    count_class={}
    for id, name, titleProject_id, _class, score in reader:
        if 'Хадаров Владимир' in name:
            print('k')