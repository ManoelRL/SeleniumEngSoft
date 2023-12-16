Feature: Deletar Categoria
  Essa feature tem como intenção deletar uma Categoria.

  Scenario Outline: Delete Categoria
    Given eu tenho <nome>
    When eu clicar em deletar
    Then o resultado será deletado

    Examples:
      |nome      |
      |Procon    |
      