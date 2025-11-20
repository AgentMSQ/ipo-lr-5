text = open('text.txt', 'r', encoding="utf-8").read() #присваиваем текст файла переменной 
print(text)  #выводим его 
lines= text.split('\n')  #разбиваем текст по строкам
reversolines = [line[::-1] for line in lines]  #переворачиваем каждую строоку и создаем список из новых строк 
result = '\n'.join(reversolines)  #объединяем новый список в строки по перехооду на новую строку
open('output.txt', 'w', encoding="utf-8").write(result)  #записываем эту строку с переходами на новую в новом файле 
