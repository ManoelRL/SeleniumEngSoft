import time
from test_insert_categoria import TestInsertCategoria


def main():

    testeCategoria = TestInsertCategoria("Testando", "Descricaooo")
        
    testeCategoria.abrir_site()
    time.sleep(5)
    testeCategoria.click_create_row_button()
    testeCategoria.preencher_formulario()
        


if __name__ == "__main__":
    main()