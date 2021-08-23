from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SettingVar:
    mainPth = "https://www.google.ru/"
    IM_PWAIT = 3
    Keys = Keys
    
    def initDriver(self):
        """
        Инициализация вебдрайвера
        """
        driver = webdriver.Chrome()
        
        driver.implicitly_wait(self.IM_PWAIT)
        driver.get(self.mainPth)
        driver.set_window_size(1024, 768)
        return driver