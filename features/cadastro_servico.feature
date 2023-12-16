Feature: CRUD de Servico
  Essa feature tem como intenção testar o CRUD de Servico.

  Scenario Outline: Create Servico
    Given eu entro com <id>, <nome>, <servico> e <vaga>
    When eu clicar em incluir servico
    Then o resultado sera servico incluido

    Examples:
      |id |nome     |servico   |vaga |
      |1  |Teste    |Descricao |10   |