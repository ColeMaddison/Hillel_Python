from conf_test import timemanager_init

def test_timemanager_set_hours_correct(timemanager_init):
    timemanager_init.hours = 5
    assert timemanager_init.hours == 4


def test_timemanager_set_minutes_seconds_correct(timemanager_init):
    timemanager_init.minutes = 5
    timemanager_init.seconds = 3
    assert timemanager_init.minutes == 9
    assert timemanager_init.seconds == 16