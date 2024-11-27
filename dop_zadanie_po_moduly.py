#Обьявление данных
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

study_list = list(students)
study_list.sort()
study_dict = dict()

for i in range(len(study_list)):
    study_dict[study_list[i]] = sum(grades[i])/len(grades[i])

print(study_dict)

