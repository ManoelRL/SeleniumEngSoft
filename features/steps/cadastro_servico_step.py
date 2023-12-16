from behave import given, when, then
from src.test_insert_servico import TestInsertServico
import time

testeServico = None

@given(u'eu entro com {id}, {nome}, {descricao} e {vaga}')
def step_impl(context,id,nome,descricao,vaga):
    context.testeServico = TestInsertServico(id,nome,descricao,vaga)
    context.testeServico.abrir_site()
    time.sleep(5)


@when(u'eu clicar em incluir servico')
def step_impl(context):
    context.testeServico.click_create_row_button()
    context.testeServico.preencher_formulario()
    time.sleep(8)


@then(u'o resultado sera servico incluido')
def step_impl(context):
    context.testeServico.conferir_insercao()
    time.sleep(2)
    context.testeServico.fechar_navegador()