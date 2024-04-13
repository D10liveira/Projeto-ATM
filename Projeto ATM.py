class Banco:
    def __init__(self, conta_corrente, conta_universitaria):
        self.conta_corrente = conta_corrente
        self.conta_universitaria = conta_universitaria
        self.saldo = 0
        self.extrato = ""
    
    def autenticacao(self):
        while True:
            print("\n================= BEM VINDO AO SEU CAIXA ELETRÔNICO =================\n")
            nome_completo = input("Para continuar seu atendimento, insira seu nome completo: ").title()
            print()
            if len(nome_completo.split()) >= 2:
                CPF = input(f"{nome_completo.split()[0]}, insira seu CPF: ")
                if len(CPF) == 11:
                    print("\nValidando seus dados...\n\n\n")
                    print("Bem-vindo,", nome_completo, "\n")
                    if self.selecionar_conta():
                        self.acao()
                    else:
                        return False
                else:
                    print("\nO campo CPF precisa conter 11 dígitos.\nTente novamente.\n")
            else:
                print("Erro: Insira seu NOME e SOBRENOME.\n")
            
    def selecionar_conta(self):
        print("Digite o número da opção desejada:\n")
        print("[1] CONTA CORRENTE")
        print("[2] CONTA UNIVERSITÁRIA")
        print("[3] SAIR")
        escolha = int(input("-- "))
        print()
        if escolha == 1:
            return self.conta_corrente
        elif escolha == 2:
            return self.conta_universitaria
        elif escolha == 3:
            print("<-> Obrigado por usar nossos serviços! <->\n")
            print("======== ATENDIMENTO ENCERRADO ========\n\n")
            return False
        else:
            print("Opção inválida!\n")
            return self.selecionar_conta()

    def acao(self):
        if self.conta_corrente:
            print(">>>> CONTA CORRENTE <<<<\n")
            while True:
                print("O que deseja fazer?\n")
                print("[1] SAQUE")
                print("[2] SALDO")
                print("[3] DEPÓSITO")
                print("[4] EXTRATO")
                print("[5] MENU CONTAS")
                opcao = int(input("-- "))
                print()
                if opcao == 1:
                    self.saque()
                elif opcao == 2:
                    self.consultar_saldo()
                elif opcao == 3:
                    self.deposito()
                elif opcao == 4:
                    self.exibir_extrato()
                elif opcao == 5:
                    return
                else:
                    print("Opção inválida!\nPor favor, tente novamente.\n")
        elif self.conta_universitaria:
            print("\n>>>> CONTA UNIVERSITÁRIA <<<<\n")
            while True:
                print("O que deseja fazer:\n")
                print("[1] SAQUE")
                print("[2] SALDO")
                print("[3] DEPÓSITO")
                print("[4] MENU CONTAS")
                opcao = int(input("-- "))
                print()
                if opcao == 1:
                    self.saque()
                elif opcao == 2:
                    self.consultar_saldo()
                elif opcao == 3:
                    self.deposito()
                elif opcao == 4:
                    return
                else:
                    print("Opção inválida!\nPor favor, tente novamente.\n")

    def saque(self):
        print(">>>>>>>>>>>> SAQUE <<<<<<<<<<<<\n")
        valor = float(input("Informe a quantia para o saque: "))
        print()
        if self.saldo >= valor:
            print(f"Saque no valor de R$ {valor} realizado.")
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saldo atual: {self.saldo:.2f}.\n")
            print("Voltando ao MENU anterior...\n")
        else:
            print("Saldo insuficiente.\n")
            self.cheque_especial()

    def consultar_saldo(self):
        print(">>>>>>>>>>>> SALDO <<<<<<<<<<<<\n")
        print(f"Saldo R$ {self.saldo:.2f}\n")
        print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<<\n")
        opcao = int(input("[1] MENU\n-- "))
        if opcao == 1:
           self.acao()
        else:
            print("\nOpção inválida!\n")
            return False
            
    def deposito(self):
        print(">>>>>>>>>>>> DEPÓSITO <<<<<<<<<<<<\n")
        valor_deposito = float(input("Informe o valor a ser depositado: "))
        print()
        self.saldo += valor_deposito
        self.extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Valor de R$ {valor_deposito:.2f} depositado com sucesso!\n")

    def cheque_especial(self):
        print("Você pode ter limite de Cheque especial disponível.\nGostaria de consultar?\n")
        decisao_cheque_especial = int(input("[1] SIM\n[2] NÃO\n-- "))
        if decisao_cheque_especial == 1:
            print()
            print(">>>>>>>>>>>> CHEQUE ESPECIAL <<<<<<<<<<<<\n")
            self.salario = float(input("Para continuarmos, por favor, insira o valor do seu salário mensal: "))
            if self.salario >= 2000:
                self.cheque_especial = self.salario * 0.2
                print()
                print(f"Que legal! Você possui limite de Cheque especial no valor de R$ {self.cheque_especial:.2f}.")
                opcao = int(input("Gostaria de contratar o Limite de Cheque Especial?\n\n[1] SIM\n[2] NÃO\n-- "))
                if opcao == 1:
                    self.valor_total = self.saldo + self.cheque_especial
                    print()
                    print(f"Parabéns! Seu saldo para saque agora é de R${self.valor_total:.2f}.\n")
                    self.saldo = self.valor_total
                    self.extrato += f"Cheque especial: R$ {self.cheque_especial:.2f}\n"            

    def exibir_extrato(self):
        print("================ EXTRATO ================\n")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=========================================\n")

conta_corrente = True
conta_universitaria = False

b = Banco(conta_corrente, conta_universitaria)
if b.autenticacao():
    while True:
        if not b.selecionar_conta():
            break
        b.acao()
