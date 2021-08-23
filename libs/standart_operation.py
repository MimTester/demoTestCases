

def inputValue(driver, meta, value):
    try:
        element = driver.find_element_by_css_selector("input[title='Поиск']")
        element.send_keys(value)
        element.send_keys(meta.Keys.ENTER)
    except:
        return "can not write data"
    
    try:
        element = driver.find_element_by_id("result-stats")
        if element.text.find("Результатов: примерно") != -1:
            return True
        else:
            return "incorrect page"
    except:
        return "can not start search"



