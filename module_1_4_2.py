
grades= [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]] #по условиям дан список оценок для каждого ученика
                                                                  # в алфавитном порядке
student = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # По условиям множество (set) students содержит
                                                 # неупорядоченную последовательность имён всех учеников в классе
student= list (student)                    # Перевел set в list, чтобы упорядочить по имени
sorted(student)                            # Сделал сортировку по имени. Вывел, проверил
name1 = (grades[0])                        # вывел из списка первое значение переменной соответствующее упорядоченной
                                            # последовательности имени 'Aaron'
sum(name1) / 5                              # высчитал средний бал студента
Aaron = name1                               # для создания множества приствоил имени значение среднего бала студента
name2 = (grades[1])                         # далее аналогичная name1, последовательность действий для других студентов
sum(name2) / 4
Bilbo = name2
name3 = (grades[2])
sum(name3) / 4
Johny = name3
name4 = (grades[3])
sum(name4) / 3
Khendrik = name4
name5 = (grades[4])
sum(name5) / 5
Steve = name5
student = {}            # создал множество и далее наполнил его вышесозданными именами, присвоив им значения в set
student ['Aaron'] = 4.0
student ['Bilbo'] = 2.25
student ['Johny'] = 4.0
student ['Khendrik'] = 3.6666666666666665
student ['Steve'] = 4.8
print(input('Добрый день! Eсли желаете узнать средний бал студента нажмите клавишу "enter"'))
print(student.get (input('Введите правильно имя студента '))) # далее связал имя с set - student и вывел средний бал
print(input('Желаете узнать успеваемость других студентов? Нажмите "enter"'))
print(student.get (input('Введите правильно имя студента ')))
print(input('Желаете узнать успеваемость других студентов? Нажмите "enter"'))
print(student.get (input('Введите правильно имя студента ')))
print(input('Желаете узнать успеваемость других студентов? Нажмите "enter"'))
print(student.get (input('Введите правильно имя студента ')))
print(input('Желаете узнать успеваемость других студентов? Нажмите "enter"'))
print(student.get (input('Введите правильно имя студента ')))






