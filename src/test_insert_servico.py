from selenium import webdriver

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

class TestInsertServico:
    def __init__(self, id, nome, descricao, vaga):
        
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.vaga = vaga


        self.SITE_LINK = {"page_servico": "https://schedulingengsoftware.budibase.app/app/schedulingsystem#/servico"}

        self.SITE_MAP = {"create_row_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button",
                         "servico_forms": {
                             "id_servico_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input",
                             "nome_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input",
                             "descricao_input": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input",
                             "vaga_input":"/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[5]/div/div/div/input",
                             "save_button": "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
                         }}
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)


    def abrir_site(self):
        self.driver.get(self.SITE_LINK["page_servico"])
        # time.sleep(20)


    def click_create_row_button(self):
        #  button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"])))
        #  button.click()
        self.driver.find_element(By.XPATH, self.SITE_MAP["create_row_button"]).click()

    def preencher_formulario(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.SITE_MAP["servico_forms"]["id_servico_input"]).send_keys(self.id)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["servico_forms"]["nome_input"]).send_keys(self.nome)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["servico_forms"]["descricao_input"]).send_keys(self.descricao)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["servico_forms"]["vaga_input"]).send_keys(self.vaga)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["servico_forms"]["save_button"]).click()
        time.sleep(1)

    def conferir_insercao(self):
        if self.driver.find_element(By.XPATH, f"//*[text()='{self.id}']"):
            print("Sucesso!")
        else:
            print("Falhou!")

    def fechar_navegador(self):
        self.driver.quit()


# teste = TestInsertservico("Testando", "Descricaoo")

# teste.abrir()