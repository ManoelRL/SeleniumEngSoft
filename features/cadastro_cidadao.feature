Feature: Cadastro de Cidadao
  Essa feature tem como intenção testar o Cadastro de Cidadao.

  Scenario Outline: Create Cidadao
    Given eu tenho <id_pessoa>, <cpf>, <email>
    When eu clicar em cadastrar
    Then o resultado será cadastrado

    Examples:
      |id_pessoa| cpf         | email           |
      |23       | 12345678998 | teste@teste.com |
