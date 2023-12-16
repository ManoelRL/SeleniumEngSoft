from behave import given, when, then

from src.test_update_categoria import TestUpdateCategoria

import time

testeUpdateCategoria = None

@given(u'eu clico no {nome}')
def step_impl(context, nome):
    context.testeUpdateCategoria = TestUpdateCategoria(nome)
    context.testeUpdateCategoria.abrir_site()
    time.sleep(5)
    
@when(u'eu atualizo para {nomeAtualizado}')
def step_impl(context, nomeAtualizado):
    context.testeUpdateCategoria.click_data_row()
    time.sleep(1)
    context.testeUpdateCategoria.preencher_formulario(nomeAtualizado)
    time.sleep(2)


@then(u'eu tenho a categoria atualizada')
def step_impl(context):
    context.testeUpdateCategoria.conferir_atualizacao()
    time.sleep(2)
    context.testeUpdateCategoria.fechar_navegador()