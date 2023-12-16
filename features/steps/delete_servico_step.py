from behave import given, when, then

from src.test_delete_servico import TestDeleteServico
import time

testeDeleteServico = None
    
@given(u'eu tenho o codigo de {id}')
def step_impl(context,id):
    context.testeDeleteServico = TestDeleteServico(id)
    context.testeDeleteServico.abrir_site()
    time.sleep(5)


@when(u'eu clicar em deletar o id')
def step_impl(context):
    context.testeDeleteServico.click_data_row()
    time.sleep(1)
    context.testeDeleteServico.click_delete_button()
    time.sleep(1)
    context.testeDeleteServico.click_confirm_button()
    time.sleep(2)


@then(u'o resultado sera o servico deletado')
def step_impl(context):
    context.testeDeleteServico.conferir_delete()
    time.sleep(2)
    context.testeDeleteServico.fechar_navegador()