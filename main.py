# Программа исправляет несоблюдение следующих правил русского языка:
# 1. сочетания ЧА-ЩА пишутся с буквой "А"
# 2. ЧУ-ЩУ с  буквой "У"
import string
counter = 0
text = input('Введите текст:')
wanted_letter_pos_1 = 0
if text[counter] == 'ч' or text[counter] == 'щ':
    if text[counter + 1] == 'я':
        correct_text_1 = text[:text.find('я', wanted_letter_pos_1)] + 'а' + text[text.find('я', wanted_letter_pos_1) + 1:]
# нахожу позицию буквы в которой допущена ошибка, вставляю правильную и окуржаю ее срезами исходной строки
for counter in range(len(text)):
    if text[counter] == 'ч' or text[counter] == 'щ':
        if text[counter+1] == 'я':
            wanted_letter_pos_1 += text.find('я', wanted_letter_pos_1)
            correct_text_1 = correct_text_1[:text.find('я', wanted_letter_pos_1)] + 'а' + text[text.find('я',wanted_letter_pos_1) + 1:]
# таким же образом изменяю строку, сдвигаясь на следующую букву с ошибкой поиск следующей буквы
        else:
            correct_text_1=text     # обьявляем переменную если на случай когда ошибка первого типа не найдена

wanted_letter_pos_1 = 0
counter = 0
if text[counter] == 'ч' or text[counter] == 'щ':
    if text[counter + 1] == 'ю':
        correct_text_1 = correct_text_1[:text.find('ю', wanted_letter_pos_1)] + 'у' + correct_text_1[text.find('ю', wanted_letter_pos_1) + 1:]
for counter in range(len(text)):
    if text[counter] == 'ч' or text[counter] == 'щ':
        if text[counter + 1] == 'ю':
            wanted_letter_pos_1 += text.find('ю', wanted_letter_pos_1)
            correct_text_1 = correct_text_1[:text.find('ю', wanted_letter_pos_1)] + 'у' + correct_text_1[text.find('ю',wanted_letter_pos_1) + 1:]
# алгорнитм повторяется для других букв
print(correct_text_1)