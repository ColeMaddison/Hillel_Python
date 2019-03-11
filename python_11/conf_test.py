from pytest import fixture
from cw_11_2 import TimeManager

@fixture
def timemanager_init():
    return TimeManager(23, 4, 13)