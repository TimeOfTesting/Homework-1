# Выполение задания №3
# Модифицируйте программу из задания 2 таким образом, чтобы данные не выводились на экран, а сохранялись в словарь. Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи.
the_date1 = input("Введите дату: ")
task1 = input ("Введите задачу: ")
the_date2 = input("Введите дату: ")
task2 = input ("Введите задачу: ")
the_date3 = input("Введите дату: ")
task3 = input ("Введите задачу: ")
dictionary = {
  the_date1: task1,
  the_date2: task2,
  the_date3:task3 
}
print(dictionary)
