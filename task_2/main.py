first_text = input("Введите строку 1: ") # вводим строку 1
second_text = input("Введите строку 2: ") # вводим строку 2
Newfirst_text = [] 
Newsecond_text = []  #создаем списки 
for char in first_text:  #цикл для добавления элементов в строку 1 
    Newfirst_text += char #добавляем элементы
for char in second_text: #цикл для добавления элементов в строку 2
    Newsecond_text += char #добавляем элементы
Newfirst_text.sort()  #Сортируем списки
Newsecond_text.sort()  #Сортируем списки
if Newfirst_text == Newsecond_text:  #сравниваем списки 
    print("Строки являются анаграммами")   #выводим, что являются 
else: #либо 
    print("Строки не являются анаграммами")    #выводим, что не являются 