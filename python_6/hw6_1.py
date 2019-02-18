# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

from re import findall

def remove(file_name):
    new_file_content = ''
    with open(file_name, "r+") as f:
        for line in f:
            found = findall(r'\b[a-zA-Z]{3,5}\b', line)
            if(len(found)%2 == 1):
                found.pop()
            for word in found:
                line = line.replace(word, '')
            new_file_content += line
        f.seek(0)
        f.truncate()
        f.write(new_file_content)
    

remove("python_6/hw6_1.txt") #had to use that path because used debugger to launch file
