from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestUpdateCidadao:
    def __init__(self, email):

        self.email = email


        self.SITE_LINK = {"page_cidadao": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/cidadao"}

        self.SITE_MAP = {"click_data": f"//div[text()='{self.email}']",
                         "update_forms": {
                             "email_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input",
                             "descricao_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input",
                         },
                         "save_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"}
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_cidadao"])


    def click_data_row(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["click_data"]).click()

    def preencher_formulario(self, emailAtualizado):
        self.driver.find_element(By.XPATH, self.SITE_MAP["update_forms"]["email_input"]).clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["update_forms"]["email_input"]).send_keys(emailAtualizado)
        time.sleep(1)
        self.email = emailAtualizado
        self.driver.find_element(By.XPATH, self.SITE_MAP["save_button"]).click()
        time.sleep(1)

    def conferir_atualizacao(self):
        assert self.driver.find_element(By.XPATH, f"//div[text()='{self.email}']").is_displayed() is True

    def fechar_navegador(self):
        self.driver.quit()