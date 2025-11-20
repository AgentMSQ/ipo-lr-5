content = open("text.txt", "r", encoding='utf-8') #записываем открытие файла 
text = content.read() # читаем файл
wordslist = text.split() #разбиваем содержимое файла по пробелам и находим кол-во слов
print(f"Список слов {wordslist}")  #выводим список слов
Wordcount = len(wordslist)  #считаем кол-во слов 
print(f"Количество слов {Wordcount}") # Выводим кол-во слов 