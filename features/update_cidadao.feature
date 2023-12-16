Feature: Atualizar Cidadao
    Essa feature tem como intenção atualizar a Cidadao

    Scenario Outline: Update Cidadao
        Given eu seleciono o cidadao de email: <email>
        When eu atualizo o email do cidadao para: <emailAtualizado>
        Then eu tenho a o cadastro do cidadao atualizado

        Examples:
            | email           | emailAtualizado       |
            | teste@teste.com | testando@testando.com |