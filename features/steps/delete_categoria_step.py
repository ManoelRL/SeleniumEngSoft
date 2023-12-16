from behave import given, when, then

from src.test_delete_categoria import TestDeleteCategoria
import time

testeDeleteCategoria = None

@given(u'eu tenho {nome: s}')
def step_impl(context, nome):
    context.testeDeleteCategoria = TestDeleteCategoria(nome)
    context.testeDeleteCategoria.abrir_site()
    time.sleep(5)


@when(u'eu clicar em deletar')
def step_impl(context):
    context.testeDeleteCategoria.click_data_row()
    time.sleep(1)
    context.testeDeleteCategoria.click_delete_button()
    time.sleep(1)
    context.testeDeleteCategoria.click_confirm_button()
    time.sleep(2)


@then(u'o resultado será deletado')
def step_impl(context):
    context.testeDeleteCategoria.conferir_delete()
    time.sleep(2)
    context.testeDeleteCategoria.fechar_navegador()