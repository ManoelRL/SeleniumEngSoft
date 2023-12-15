from behave import given, when, then
from src.test_insert_categoria import TestInsertCategoria
import time

testeCategoria  = None

@given(u'eu tenho {nome} e {descricao}')
def step_impl(context, nome, descricao):
    context.testeCategoria = TestInsertCategoria(nome, descricao)
    context.testeCategoria.abrir_site()
    time.sleep(5)
    
@when(u'eu clicar em {acao}')
def step_impl(context, acao):

    context.testeCategoria.click_create_row_button()
    context.testeCategoria.preencher_formulario()
    time.sleep(8)


@then(u'o resultado será {resultado}')
def step_impl(context):
    context.testeCategoria.conferir_insercao()
    time.sleep(2)
    context.testeCategoria.fechar_navegador()



