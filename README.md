# Sistema Bancário em Python

Este projeto é uma atualização de um sistema bancário simples desenvolvido em Python como parte do desafio da DIO (Digital Innovation One). O objetivo deste sistema é gerenciar clientes e suas contas, permitindo realizar transações como depósitos e saques, além de gerar relatórios de atividades financeiras.

## Desafios

O projeto abrange os seguintes desafios:

1. **Modelagem de classes**: Implementar a modelagem de clientes e operações bancárias, utilizando programação orientada a objetos (POO).
2. **Persistência de dados**: Atualizar a implementação do sistema para armazenar os dados de clientes e contas bancárias em objetos, ao invés de dicionários, seguindo um modelo de classes UML.
3. **Gerenciamento de transações**: Adicionar funcionalidades para gerenciar transações de depósito e saque, garantindo que as operações sejam realizadas de forma segura.
4. **Aplicação de decoradores**: Implementar decoradores para adicionar funcionalidades adicionais às funções do sistema, como logging de transações.
5. **Iteradores e geradores**: Utilizar iteradores e geradores para facilitar a navegação e a geração de relatórios das transações.

## Funcionalidades Implementadas

- **Cadastro de Clientes**: Permite cadastrar novos clientes com informações como nome, CPF e endereço.
- **Criação de Contas**: Possibilita a criação de contas bancárias associadas a clientes.
- **Depósitos e Saques**: Realiza depósitos e saques, com validações de saldo e limite de saques.
- **Extrato de Transações**: Gera um extrato com as transações realizadas em cada conta.
- **Log de Transações**: Implementa um sistema de log para registrar todas as transações realizadas.
- **Relatório de Transações**: Gera relatórios detalhados das transações realizadas.

## Melhoria Contínua

- **Interface do Menu**: O menu foi aprimorado para melhorar a experiência do usuário.
- **Validações Aprimoradas**: Foram adicionadas validações adicionais para garantir a integridade das transações.
- **Documentação**: O código foi documentado para facilitar a compreensão e a manutenção.

## Como Executar

Para executar o sistema, certifique-se de ter o Python instalado em sua máquina. Depois, siga os passos abaixo:

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute o script principal:

```bash
python sistema_bancario.py
