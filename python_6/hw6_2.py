# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def phone_numbers(file_in, file_out):
    with open(file_in) as f_in, open(file_out, 'w') as f_out:
        lines = f_in.readlines()
        for line in lines: 
            if line[0] == 'K' or line[0] == 'C':
                f_out.write(line)


phone_numbers('python_6/hw6_2(in).txt', 'python_6/hw6_2(out).txt')