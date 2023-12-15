Feature: CRUD de Categoria
  Essa feature tem como intenção testar o CRUD de Categoria.

  Scenario Outline: Create Categoria
    Given eu tenho <nome> e <desc>
    When eu clicar em incluir
    Then o resultado será incluido.

    Examples:
      | nome   | desc                                        | acao    | resultado |
      | Procon | Programa de Proteção e Defesa do Consumidor | Incluir | Sucesso.  |
