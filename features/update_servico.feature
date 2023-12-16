Feature: Atualizar Servico
    Essa feature tem como intenção atualizar a Servico

    Scenario Outline: Update Servico
        Given eu clico na <desc>
        When eu altero para <descAtt>
        Then o resultado sera servico atualizado

        Examples:
          |desc |descAtt|
          |Teste|Teste2 |