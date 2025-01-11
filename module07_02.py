from idlelib.iomenu import encoding
strings_positions = {} # создаем пустой список

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8') # Открываем файл для чтения с кодировкой utf-8
    for i in strings:
        index = strings.index(i)     # Показывает номер элемента списка
        tupl = (index + 1, file.tell()) # Добавляем номер элемента списка и байт начала строки
        strings_positions[tupl] = i # Добавляем в слоаврь кортеж в виде ключа и саму строку в виде значения
        file.write(f'{i}\n') # Пишем каждую строку из списка string в файл
    file.close()
    return print(strings_positions)

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]

result = custom_write('test.txt',     info)

for elem in strings_positions.items():
    print(elem)