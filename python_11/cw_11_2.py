# Создать класс для представления информации о времени. Ваш класс должен иметь  возможности установки 
# времени и изменения его отдельных полей (час, минута, секунда) с проверкой допустимости вводимых 
# значений. В случае недопустимых значений полей выбрасываются исключения. Создать методы изменения 
# времени на заданное количество часов, минут и секунд.

from datetime import datetime
from datetime import timedelta

class TimeManager(object):
    def __init__(self, h, m, s):
        try:
            if h in range(24) and m in range(60) and s in range(60):
                self.h = h
                self.m = m
                self.s = s
                self.date = datetime(2019, 1, 21, h, m, s)
            else:
                raise ValueError
        except Exception as e:
            print('ValueError {}'.format(e))

    @property
    def get_current_time(self):
        return self.date
    
    @property
    def hours(self):
        return self.date.hour
    
    @hours.setter
    def hours(self, new_hour):
        self.date += timedelta(hours=new_hour)
    
    @property
    def minutes(self):
        return self.date.minute
    
    @minutes.setter
    def minutes(self, new_minutes):
        self.date += timedelta(minutes=new_minutes)
    
    @property
    def seconds(self):
        return self.date.second
    
    @seconds.setter
    def seconds(self, new_seconds):
        self.date += timedelta(seconds=new_seconds)

timing = TimeManager(23, 4, 13)
print(timing.get_current_time)
timing.hours = 5
print(timing.hours)
timing.seconds = 10
print(timing.seconds)
print(timing.get_current_time)