import time
from selenium import webdriver
link ="https://netpeak.ua/"

try:
    browser = webdriver.Chrome(executable_path='C://chromedriver_win32/chromedriver.exe')
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(5)
    link2 = "https://career.netpeak.group/"
    browser.get(link2)
    time.sleep(5)
    browser.execute_script("window.scrollBy (0,3300);")
    time.sleep(3)
    link3 = "https://career.netpeak.group/hiring/"
    browser.get(link3)
    time.sleep(3)
    button_resume = browser.find_element_by_name("uploaded-file")    #кнопка "Загрузить резюме"
    file_path = "C://Downloads/Tatnet.jpg"    #путь до файла с рисунком .jpg
    button_resume.send_keys(file_path)   #!!!
    time.sleep(15)
    text_message = browser.find_element_by_css_selector("#up_file_name>.control-label").text    #сообщение об ошибке assert?
    assert "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."==text_message
    time.sleep(3)    #!!!
    inputN = browser.find_element_by_id("inputName")
    inputN.send_keys("join")
    inputLN = browser.find_element_by_id("inputLastname")
    inputLN.send_keys("yeshya")
    inputY = browser.find_element_by_name("by")
    inputY.send_keys("1985")
    inputM = browser.find_element_by_name("bm")
    inputM.send_keys("января")
    inputD = browser.find_element_by_name("bd")
    inputD.send_keys("8")
    time.sleep(3)
    inputE = browser.find_element_by_id("inputEmail")
    inputE.send_keys("dfghk@mail.ru")
    inputP = browser.find_element_by_id("inputPhone")
    inputP.send_keys("8913456789")
    time.sleep(4)
    browser.execute_script("window.scrollBy (0,500);")
    time.sleep(3)
    button_resume = browser.find_element_by_id("submit")
    button_resume.click()
    text_message2 = browser.find_element_by_class_name("warning-fields.help-block").text
    assert "Все поля являются обязательными для заполнения"==text_message2
    style = ('{'
        'color: ##FF0000'
        '}')
    text_message3 = browser.find_element_by_class_name("warning-fields.help-block").get_attribute('color')
    assert style==text_message3
    browser.get(link2)
    h2 = browser.find_element_by_css_selector('//[contains(text(), "Курсы"').text
    assert h2 == "Курсы"    #!!!

finally:
    browser.quit()