from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestInsertCategoria():
    def __init__(self, nome, descricao):

        self.nome = nome
        self.descricao = descricao


        self.SITE_LINK = {"page_categoria": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/categoria"}

        self.SITE_MAP = {"create_row_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button",
                         "categoria_forms": {
                             "nome_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input",
                             "descricao_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input",
                             "save_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
                         },
                         "data_row": f"//div[text()='{self.nome}']"}
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_categoria"])

    def click_create_row_button(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"]).click()

    def preencher_formulario(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["nome_input"]).send_keys(self.nome)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["descricao_input"]).send_keys(self.descricao)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["save_button"]).click()
        time.sleep(1)

    def conferir_insercao(self):
        assert self.driver.find_element(By.XPATH, f"//div[text()='{self.nome}']").is_displayed() is True

    def fechar_navegador(self):
        self.driver.quit()
