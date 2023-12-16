from behave import given, when, then

from src.test_delete_cidadao import TestDeleteCidadao
import time

testeDeleteCidadao = None

@given(u'eu tenho o numero de {cpf}')
def step_impl(context, cpf):
    context.testeDeleteCidadao = TestDeleteCidadao(cpf)
    context.testeDeleteCidadao.abrir_site()
    time.sleep(5)


@when(u'eu clicar em deletar o cpf')
def step_impl(context):
    context.testeDeleteCidadao.click_data_row()
    time.sleep(1)
    context.testeDeleteCidadao.click_delete_button()
    time.sleep(1)
    context.testeDeleteCidadao.click_confirm_button()
    time.sleep(2)


@then(u'o resultado será o cidado deletado')
def step_impl(context):
    context.testeDeleteCidadao.conferir_delete()
    time.sleep(2)
    context.testeDeleteCidadao.fechar_navegador()