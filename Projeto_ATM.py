import random
import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

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
        self._extrato = Extrato()

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
        def extrato(self):
            return self._extrato
        
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo    

        if excedeu_saldo:
            print("Você não possui saldo o suficiente.")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
            
        else:
            print("Erro: Valor informado é inválido.")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
                
        else:
            print("Erro: Valor informado é inválido.")
            return False

        return True
    
    def cheque_especial(self, salario):
        limite_cheque_especial = 0.20

        if salario >= 2000:
            limite = salario * limite_cheque_especial
            print(f"Você possui um limite de R$ {limite:.2f} disponivel.")

        else:
            print("Você não possui limite de Cheque especial.")
            return False

        return True
        
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
                
    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self.extrato.transacoes if transacao["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saque >= self.limite_saques
        
        if excedeu_limite:
            print("Erro: O valor excede o limite.")
    
        elif excedeu_saques:
            print("Erro: Excedeu o limite de saques.")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"Agência:\t{self._agencia}\nC/C:\t\t{self._numero}\nTitular:\t{self.cliente.nome}"        
              
                  
class Extrato:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__,
                                 "valor": transacao.valor,
                                 "data": datetime.now().strftime
                                 ("%d-%m-%Y %H:%M:%s"),})
     
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
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
            conta.extrato.adicionar_transacao(self)
            
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.extrato.adicionar_transacao(self)

            
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDEPOSITAR
    [2]\tSACAR
    [3]\tEXTRATO
    [4]\tNOVO USUÁRIO
    [5]\tNOVA CONTA
    [6]\tLISTAR CONTAS
    [0]\tSAIR
    
    ==>"""
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta.")
        return
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not clientes:
        print()
        print("Cliente não encontrado.\n\nCaso seja seu primeiro acesso, será necessário criar seu >USUÁRIO e sua CONTA.\n\nVamos te redirecionar para o MENU principal.")
        return
    
    valor = float(input("Informe o valor a ser depositado: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
def sacar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor a ser sacado: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n============ EXTRATO ============")
    transacoes = conta.extrato.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}"
            
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF.")
        return
    
    nome = input("Informe seu nome completo: ")
    if len(nome.split()) == 1:
        print("No campo NOME inserir o nome completo.")
        criar_cliente(clientes)
    while True:
        data = input("Informe a data de nascimento: ")
        try: 
            data_nascimento = datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            print("Formato de data inválido. Por favor, digite no formato dd/mm/AAAA.")
            return
    
        endereco = input("Informe seu endereço: ")
    
        cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        clientes.append(cliente)

        numero_aleatorio = random.randint(1000, 4999)
        print(numero_aleatorio)

    
        print("\n**** Cliente criado com sucesso! ****")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    conta = Conta.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n**** Conta criada com sucesso! ****")    
    
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            depositar(clientes)
            
        elif opcao == '2':
            sacar(clientes)
            
        elif opcao == '3':
            exibir_extrato(clientes)
            
        elif opcao == '4':
            criar_cliente(clientes)
            
        elif opcao == '5':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == '6':
            listar_contas(contas)
            
        elif opcao == '0':
            print("\n<><><><><><> FINALIZANDO <><><><><><><>")
            print(f"\nObrigado por usar nossos serviços.")
            print("\n=======================================")

            break
   
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

        
main()