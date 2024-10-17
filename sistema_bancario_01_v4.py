import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self.contas):
            conta = self.contas[self._indice]
            self._indice += 1
            return conta
        raise StopIteration

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._transacoes_dia = 0  # Contador de transações diárias
        self._data_transacao_dia = datetime.now().date()  # Data da última transação

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def resetar_transacoes_dia(self):
        self._transacoes_dia = 0

    def incrementar_transacoes_dia(self):
        self._transacoes_dia += 1

    def verificar_limite_transacoes(self):
        if self._data_transacao_dia != datetime.now().date():
            self.resetar_transacoes_dia()
            self._data_transacao_dia = datetime.now().date()

    def sacar(self, valor):
        self.verificar_limite_transacoes()
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        elif valor > 0:
            if self._transacoes_dia >= 10:  # Limitar a 10 transações diárias
                print("\n@@@ Operação falhou! Número máximo de transações diárias excedido. @@@")
                return False
            
            self._saldo -= valor
            self.incrementar_transacoes_dia()  # Incrementa o contador de transações
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        self.verificar_limite_transacoes()
        
        if valor > 0:
            if self._transacoes_dia >= 10:  # Limitar a 10 transações diárias
                print("\n@@@ Operação falhou! Número máximo de transações diárias excedido. @@@")
                return False
            
            self._saldo += valor
            self.incrementar_transacoes_dia()  # Incrementa o contador de transações
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self):
        for transacao in self.transacoes:
            print(f"{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} em {transacao['data']}")

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            return True
        return False

def log_transacao(func):
    def wrapper(*args, **kwargs):
        print(f"\n=== Iniciando transação: {func.__name__} ===")
        resultado = func(*args, **kwargs)
        print(f"=== Transação {func.__name__} finalizada ===")
        return resultado
    return wrapper

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    return cliente.contas[0]

def gerar_numero_conta(clientes):
    # Gera um número de conta único
    ultimo_numero = 0
    for cliente in clientes:
        for conta in cliente.contas:
            numero_conta = int(conta.numero)
            if numero_conta > ultimo_numero:
                ultimo_numero = numero_conta
    return str(ultimo_numero + 1).zfill(4)  # Preenche com zeros à esquerda

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print(f"\n=== Extrato da conta {conta.numero} ===")
    conta.historico.gerar_relatorio()
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")

@log_transacao
def criar_usuario(clientes):
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe o CPF: ")
    endereco = input("Informe o endereço: ")

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)

    print(f"\n=== Cliente {nome} cadastrado com sucesso! ===")

@log_transacao
def criar_conta(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    numero = gerar_numero_conta(clientes)  # Gera número automático da conta
    conta = ContaCorrente.nova_conta(cliente, numero)
    cliente.adicionar_conta(conta)

    print(f"\n=== Conta {numero} criada com sucesso! ===")

def listar_contas(clientes):
    for cliente in clientes:
        print(f"\n=== Clientes: {cliente.nome} ===")
        for conta in cliente.contas:
            print(conta)

def main():
    clientes = []
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            criar_conta(clientes)
        elif opcao == 'lc':
            listar_contas(clientes)
        elif opcao == 'nu':
            criar_usuario(clientes)
        elif opcao == 'q':
            break
        else:
            print("\n@@@ Opção inválida! @@@")

if __name__ == "__main__":
    main()
