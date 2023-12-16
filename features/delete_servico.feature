Feature: Deletar Servico
  Essa feature tem como intenção deletar uma Servico.

  Scenario Outline: Delete Servico
    Given eu tenho o codigo de <id>
    When eu clicar em deletar o id
    Then o resultado sera o servico deletado

    Examples:
      |id|
      |1 |