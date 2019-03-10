# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#   

import asyncio
import traceback

loop = asyncio.get_event_loop()

async def grep(line, pattern):
    print('Looking for {}'.format(pattern))
    if pattern in line:
        printer(pattern, line)
    

def printer(line, pattern):
    print('Pattern {} found in line: {}'.format(line, pattern))


async def dispenser(line, patterns):
    for pattern in patterns:
        await grep(line, pattern)


def follow(file, patterns):
    file.seek(0, 2)
    try:
        while True: 
            line = file.readline()
            if line.strip():
                loop.run_until_complete(dispenser(line, patterns))

    except Exception as e:
        print(traceback.format_exc())
        print(e)

f_open = open('./python_10/hw_10_1.txt')
follow(f_open, ['python', 'is', 'great'])
f_open.close()