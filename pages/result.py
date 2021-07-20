from selenium.webdriver.common.by import By

class ResultPage:
    
    RESULT_LINKS = (By.XPATH, '//cite')

    def __init__(self,browser):
        self.browser=browser

    def result_link_title(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles