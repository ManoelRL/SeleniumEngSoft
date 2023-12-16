from behave import given, when, then
from src.test_insert_cidadao import TestInsertCidadao
import time

testeInsertCidadao = None

@given(u'eu tenho {id_pessoa}, {cpf}, {email}')
def step_impl(context, id_pessoa, cpf, email):
    context.testeInsertCidadao = TestInsertCidadao(id_pessoa, cpf, email)
    context.testeInsertCidadao.abrir_site()
    time.sleep(5)

@when(u'eu clicar em cadastrar')
def step_impl(context):
    context.testeInsertCidadao.click_create_row_button()
    context.testeInsertCidadao.preencher_formulario()
    time.sleep(8)

@then(u'o resultado será cadastrado')
def step_impl(context):
    context.testeInsertCidadao.conferir_insercao()
    time.sleep(2)
    context.testeInsertCidadao.fechar_navegador()