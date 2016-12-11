__author__ = 'NovikovII'

import os
import os.path
import shutil



# #выводит текущую дирресторию
# print(os.getcwd())
# #меняет текущую дирректорию
# #os.chdir('C:\shareFolder\Dropbox\python_training')
# #выводит текущую дирресторию
# #print(os.getcwd())
#
# #выводит текущую дирресторию
# print(os.listdir(os.getcwd()))
# #показывает список файлов в текущей дирректории
# print(os.listdir('.'))
#
# #проверяет, файл ли то, что в скобках
# print(os.path.isfile('test.py'))
# #проверяет, дирректория ли то, что в скобках
# print(os.path.isdir('test.py'))
#
# print(list(filter(lambda f: os.path.isfile(f), os.listdir('.'))))
#
# abc = [12, 14, 15, 16, 17]
# #выведет только те элементы списка abc, для которых выполняетс условие x%2 == 0
# print(list(filter(lambda x: x%2 == 0, abc)))
#
#
# #создает дирректорию 'test' с текущей дирректории
# #os.mkdir('test')
# #создает вложенные дирректории
# #os.makedirs('test1/test2/test3')
# #удaление дирректорий
# #os.rmdir('test')
# #уделение дирректорий с вложенными папкеми
# shutil.rmtree('test1')
#
# #копирование файла
# shutil.copy('C:/shareFolder/Dropbox/python_training/model/contact.py', '.')
# #удаление файла
# os.remove('./contact.py')
#
