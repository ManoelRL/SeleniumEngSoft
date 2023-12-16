from behave import given, when, then
from src.test_update_cidadao import TestUpdateCidadao

import time

testeUpdateCidadao = None

@given(u'eu seleciono o cidadao de email: {email}')
def step_impl(context, email):
    context.testeUpdateCidadao = TestUpdateCidadao(email)
    context.testeUpdateCidadao.abrir_site()
    time.sleep(5)


@when(u'eu atualizo o email do cidadao para: {emailAtualizado}')
def step_impl(context, emailAtualizado):
    context.testeUpdateCidadao.click_data_row()
    time.sleep(1)
    context.testeUpdateCidadao.preencher_formulario(emailAtualizado)
    time.sleep(2)
    


@then(u'eu tenho a o cadastro do cidadao atualizado')
def step_impl(context):
    context.testeUpdateCidadao.conferir_atualizacao()
    time.sleep(2)
    context.testeUpdateCidadao.fechar_navegador()