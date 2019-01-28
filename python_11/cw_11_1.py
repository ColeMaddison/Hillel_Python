# Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер группы, успеваемость 
# (массив из пяти элементов).

from statistics import mean

class Student(object):
    def __init__(self, name, initials, group_no, progress):
        self.name = name
        self.initials = initials
        self.group_no = group_no
        self.progress = progress

    def avg_mark(self):
        return mean(self.progress)

nikolay = Student('Niko', 'NK', 13, [10, 10, 9, 10, 5])

print(nikolay.avg_mark())