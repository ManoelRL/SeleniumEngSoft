from behave import given, when, then

from src.test_update_servico import TestUpdateServico

import time

testeUpdateServico = None

@given(u'eu clico na {desc}')
def step_impl(context, desc):
    context.testeUpdateServico = TestUpdateServico(desc)
    context.testeUpdateServico.abrir_site()
    time.sleep(5)
    
@when(u'eu altero para {descAtt}')
def step_impl(context, descAtt):
    time.sleep(4)
    context.testeUpdateServico.click_data_row()
    time.sleep(2)
    context.testeUpdateServico.preencher_formulario(descAtt)


@then(u'o resultado sera servico atualizado')
def step_impl(context):
    context.testeUpdateServico.conferir_atualizacao()
    time.sleep(2)
    context.fechar_navegador()