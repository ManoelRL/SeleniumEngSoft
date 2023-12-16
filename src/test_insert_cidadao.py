from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestInsertCidadao:
    def __init__(self, id_pessoa, cpf, email):

        self.id_pessoa = id_pessoa
        self.cpf = cpf
        self.email = email


        self.SITE_LINK = {"page_cidadao": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/cidadao"}

        self.SITE_MAP = {"create_row_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button",
                         "cidadao_forms": {
                             "cpf_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input",
                             "email_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input",
                             "id_pessoa_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div/input",
                             "save_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
                         }}
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_cidadao"])

    def click_create_row_button(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"]).click()

    def preencher_formulario(self): 
        self.driver.find_element(By.XPATH, self.SITE_MAP["cidadao_forms"]["cpf_input"]).send_keys(self.cpf)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["cidadao_forms"]["email_input"]).send_keys(self.email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["cidadao_forms"]["id_pessoa_input"]).send_keys(self.id_pessoa)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["cidadao_forms"]["save_button"]).click()
        time.sleep(1)

    def conferir_insercao(self):
        assert self.driver.find_element(By.XPATH, f"//div[text()='{self.cpf}']").is_displayed() is True

    def fechar_navegador(self):
        self.driver.quit()
