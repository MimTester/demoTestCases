import pytest
from libs.meta import SettingVar
import libs.standart_operation as SO

meta = SettingVar()
driver = meta.initDriver()

def setup_module(module): ## Перед тестовым прогоном
    driver.get(meta.mainPth)

def teardown_module(module): ## После тестового прогона
    driver.quit()

def setup_function(function): ## Перед каждым тестом
    driver.get(meta.mainPth)
    
def teardown_function(function): ## После каждого теста
    driver.refresh()

# Сами тесты

# Положительные тесты
@pytest.mark.parametrize("inputData",
[
("Test"),
("TEST"),
("test"),
("123")
])
def test_DemoPositive(inputData):
    assert SO.inputValue(driver, meta, inputData) is True

# setup_module(1)
# test_DemoPositive("Test")


# Отрицательные тесты
@pytest.mark.parametrize("inputData",
[
(""),
("   "),
(")*$%(")
])
def test_DemoNegative(inputData):
    assert SO.inputValue(driver, meta, inputData) is not True
