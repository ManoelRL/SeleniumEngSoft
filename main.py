import time
from test_insert_categoria import TestInsertCategoria
from test_delete_categoria import TestDeleteCategoria


def main():


    def insert():
        testeCategoria = TestInsertCategoria("Testando", "Descricaooo")
            
        testeCategoria.abrir_site()
        time.sleep(5)
        testeCategoria.click_create_row_button()
        testeCategoria.preencher_formulario()
        time.sleep(8)
        testeCategoria.conferir_insercao()

    def delete():
        testeUpdateCategoria = TestUpdateCategoria("Testando")

        testeUpdateCategoria.abrir_site()
        time.sleep(5)
        testeUpdateCategoria.click_data_row()
        time.sleep(3)
        testeUpdateCategoria.click_delete_button()
        time.sleep(1)
        testeUpdateCategoria.click_confirm_button()
        time.sleep(1)
        testeUpdateCategoria.conferir_insercao()



    delete()
        


if __name__ == "__main__":
    main()