from selenium import webdriver

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestInsertCategoria:
    def __init__(self, nome, descricao):

        self.nome = nome
        self.descricao = descricao


        self.SITE_LINK = {"page_categoria": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/categoria"}

        self.SITE_MAP = {"create_row_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button",
                         "categoria_forms": {
                             "nome_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input",
                             "descricao_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input",
                             "save_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
                         }}
        
        self.driver = webdriver.Chrome()

    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_categoria"])
        # time.sleep(20)


    def click_create_row_button(self):
        #  button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"])))
        #  button.click()
        self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"]).click()

    def preencher_formulario(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["nome_input"]).send_keys(self.nome)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["descricao_input"]).send_keys(self.descricao)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["categoria_forms"]["save_button"]).click()
        time.sleep(1)

    def conferir_insercao(self):
        if self.driver.find_element(By.XPATH, f"//div[text()='{self.nome}']"):
            print("Sucesso!")
        else:
            print("Falhou!")

    def fechar_navegador(self):
        self.driver.quit()


# teste = TestInsertCategoria("Testando", "Descricaoo")

# teste.abrir()