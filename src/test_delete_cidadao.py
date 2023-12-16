from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestDeleteCidadao:
    def __init__(self, cpf):

        self.cpf = cpf

        self.SITE_LINK = {"page_categoria": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/cidadao"}

        self.SITE_MAP = {"click_data": f"//div[text()='{self.cpf}']",
                         "delete_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/button",
                         "confirm_button": "/html/body/div[2]/div/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/span/div/button"}
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_categoria"])


    def click_data_row(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["click_data"]).click()

    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["delete_button"]).click()

    def click_confirm_button(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["confirm_button"]).click()

    def conferir_delete(self):
        try:
            self.driver.find_element(By.XPATH, f"//div[text()='{self.cpf}']")

            assert False, f"A categoria {self.cpf} não foi excluída!"
        except NoSuchElementException:
            pass

    def fechar_navegador(self):
        self.driver.quit()