import os
from pprint import pprint

BASE_PATH = os.getcwd()
LOG_CATALOG_NAME = 'text'

LOG_FILE_NAME_1 = '1.txt'
LOG_FILE_NAME_2 = '2.txt'
LOG_FILE_NAME_3 = '3.txt'

full_path_1 = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME_1)
full_path_2 = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME_2)
full_path_3 = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME_3)
full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME)

def create_CATALOG(full_path):
    file_list = os.listdir(full_path)
    combined_list = []
    with open(full_path_1, 'r', encoding='utf-8') as file:
        combined_list.append([full_path_1, 0, []])
        for line in file:
            combined_list[-1][2].append(line.strip())
            combined_list[-1][1] += 1
    with open(full_path_2, 'r', encoding='utf-8') as file:
        combined_list.append([full_path_2, 0, []])
        for line in file:
            combined_list[-1][2].append(line.strip())
            combined_list[-1][1] += 1
    with open(full_path_3, 'r', encoding='utf-8') as file:
        combined_list.append([full_path_3, 0, []])
        for line in file:
            combined_list[-1][2].append(line.strip())
            combined_list[-1][1] += 1
    return sorted(combined_list, key=lambda x: x[2], reverse=True)

def create_FILE(full_path, file_name):
    with open(file_name + '.txt', 'w+') as newfile:
        for file in create_CATALOG(full_path):
            newfile.write(f'Путь к файлу: {file[0]}\n')
            newfile.write(f'Количество строк: {file[1]} строк\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('\n')

create_FILE(full_path, 'Новый файл')

