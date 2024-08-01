def  custom_write(file_name, strings):
    file = open(file_name,'w',encoding='utf-8')
    strings_positions = {}

    for q ,v in  enumerate(strings):
        strings_positions[(q+1,file.tell())] = v
        file.write(f'{v}\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!' ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



