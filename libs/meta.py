from selenium import webdriver

class SettingVar:
    mainPth = ""
    IM_PWAIT = 3

    def initDriver(self):
        """
        Инициализация вебдрайвера
        """
        driver = webdriver.Chrome()
        
        driver.implicitly_wait(self.IM_PWAIT)
        driver.get(self.mainPth)
        driver.set_window_size(1024, 768)
        return driver