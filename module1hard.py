# 1st way
grade = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Jhonny","Bilbo","Steve","Khendrik","Aaron"}
# вычисляем среднее для каждого из студентов
Aaron = sum(grade[0])/len(grade[0])
Bilbo = sum(grade[1])/len(grade[1])
Jhonny = sum(grade[2])/len(grade[2])
Khendrik = sum(grade[3])/len(grade[3])
Steve = sum(grade[4])/len(grade[4])
# создаем dictinoary с ключом по студенту и значением по средней оценке
class_book = {"Aaron":Aaron,"Bilbo":Bilbo,"Jhonny":Jhonny,"Khendrik":Khendrik,"Steve":Steve}
print(class_book)

# 2nd way
grade = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Jhonny","Bilbo","Steve","Khendrik","Aaron"}
student_list = sorted(list(students)) # преобразование множества в список и сортировка по алфавиту
avg_grade1 = sum(grade[0])/len(grade[0])
avg_grade2 = sum(grade[1])/len(grade[1])
avg_grade3 = sum(grade[2])/len(grade[2])
avg_grade4 = sum(grade[3])/len(grade[3])
avg_grade5 = sum(grade[4])/len(grade[4])
grade_book = {student_list[0]:avg_grade1,student_list[1]:avg_grade2, student_list[2]:avg_grade3,\
              student_list[3]:avg_grade4,student_list[4]:avg_grade5}
print(grade_book)