# Sistema Bancário em Python

## Descrição

Este projeto é uma atualização do sistema bancário desenvolvido como parte do desafio da DIO (Digital Innovation One). O objetivo é implementar um sistema bancário que permita a criação de clientes, contas, e a realização de transações como depósitos, saques e geração de extratos, utilizando conceitos de Programação Orientada a Objetos (POO).

## Funcionalidades

- **Cadastro de Clientes e Contas Bancárias:** Permite cadastrar clientes e suas respectivas contas com número de conta gerado automaticamente.
- **Realização de Depósitos e Saques:** O sistema suporta operações de depósitos e saques, com verificação de saldo e limites.
- **Exibição de Extrato Bancário:** Gera o extrato com o histórico de todas as transações realizadas na conta.
- **Registro de Transações com Histórico:** Mantém o histórico de transações como saques e depósitos para referência futura.
- **Relatórios Detalhados de Transações:** Possui gerador de relatórios de transações realizadas nas contas.

## Melhorias Implementadas

- **Uso de Programação Orientada a Objetos (POO):** O sistema foi modelado utilizando classes para representar Clientes, Contas e Transações.
- **Criação Automática de Contas:** O número da conta é gerado automaticamente para evitar duplicatas.
- **Limite de Transações Diárias:** O sistema restringe o número de transações (depósitos e saques) a um máximo de 10 operações diárias por conta.
- **Limite de Saques:** Cada conta corrente tem um limite máximo de 3 saques diários, com o valor de até R$ 500,00 por saque.
- **Decoradores:** Implementação de um decorador para registrar log de todas as transações realizadas, como forma de acompanhamento.
- **Iteradores:** Foi adicionado um iterador personalizado para percorrer contas bancárias, permitindo uma navegação fácil entre elas.
- **Geradores:** Implementação de um gerador para criar relatórios de transações de forma eficiente, sem precisar carregar tudo na memória de uma só vez.
- **Tratamento de Erros:** Implementação de mensagens de erro amigáveis para melhorar a experiência do usuário e prevenir operações inválidas.

## Como Executar

### Pré-requisitos

- **Python 3.x**
- Bibliotecas padrão do Python (nenhuma biblioteca externa necessária)

### Clonando o Repositório

Para clonar este repositório, utilize o seguinte comando no terminal:

```bash
git clone https://github.com/dann17dev/sistema_bancario_01_v4.git

Para clonar este repositório, utilize o seguinte comando:

```bash
git clone https://github.com/dann17dev/sistema_bancario_01_v4.git
