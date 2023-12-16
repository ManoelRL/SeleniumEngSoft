Feature: Deletar Cidadao
  Essa feature tem como intenção deletar uma Cidadao.

  Scenario Outline: Delete Cidadao
    Given eu tenho o numero de <cpf>
    When eu clicar em deletar o cpf
    Then o resultado será o cidado deletado

    Examples:
      |cpf            |
      |12345678998    |