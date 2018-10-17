import os
for currentFolder, subFolder, fileNames in os.walk(input('Введите путь к папкам\n')):
    print('В папке{}:\n\tСодержатся папки:{}\n\tСодержатся файлы:{}'.format(currentFolder,     subFolder, fileNames))
   
