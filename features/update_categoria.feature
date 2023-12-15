Feature: Atualizar Categoria
    Essa feature tem como intenção atualizar a Categoria

    Scenario Outline: Update Categoria
        Given eu clico no <nome>
        When eu atualizo para <nomeAtualizado>
        Then eu tenho a categoria atualizada

        Examples:
            | nome   | nomeAtualizado |
            | Procon | Procon2        |