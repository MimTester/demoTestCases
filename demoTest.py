import pytest
from libs.meta import SettingVar

meta = SettingVar()

def setup_module(module): ## Перед тестовым прогоном
    pass

def teardown_module(module): ## После тестового прогона
    pass

def setup_function(function): ## Перед каждым тестом
    pass
    
def teardown_function(function): ## После каждого теста
    pass

def test_Demo():
    pass