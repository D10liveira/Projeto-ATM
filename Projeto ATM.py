class Banco:
    def __init__(self, conta_corrente, conta_universitaria):
        self.conta_corrente = conta_corrente
        self.conta_universitaria = conta_universitaria
        self.saldo = 1000
    
    def autentificacao(self):
        while True:
            nome_completo = input("Por favor, insira seu nome completo: ")
            CPF = input("Por favor, insira seu CPF: ")
            if len(nome_completo.split()) >= 2 and len(CPF) == 11:
                print("Bem-vindo,", nome_completo)
                return True
            else:
                print("Dados incorretos. Tente novamente com nome e sobrenome.\nObs. Campo CPF precisa conter 11 dígitos.")
            
    def contas(self):
        print("Selecione uma opção:")
        print("[1] Conta Corrente")
        print("[2] Conta Universitária")
        escolha = int(input())
        
        if escolha == 1:
            self.conta_corrente = True
            self.conta_universitaria = False
        elif escolha == 2:
            self.conta_corrente = False
            self.conta_universitaria = True
        else:
            print("Opção inválida!")
            return False
        return True

    def acao(self):
        if self.conta_corrente:
            print("Informe uma opção:")
            print("[1] SAQUE")
            print("[2] SALDO")
            print("[3] DEPÓSITO")
            opcao = int(input())
            if opcao == 1:
                valor = float(input("Informe a quantia para o saque: "))
                if self.saldo >= valor:
                    print(f"Saque no valor de {valor} reais realizado.")
                    saldo_atualizado = self.saldo - valor
                    print(f"Saldo atual: {saldo_atualizado} reais.\n")
                    print("OBRIGADO POR USAR NOSSOS SERVIÇOS!\nAté logo!")
                    
                else:
                    print("Saldo insuficiente.")
                    print("Você pode ter limite de Cheque especial disponível.\nGostaria de consultar?")
                    decisao_cheque_especial = int(input("[1] SIM\n[2] NÃO\n"))
                    if decisao_cheque_especial == 1:
                        self.salario = float(input("Para continuarmos, por favor, insira o valor do seu salário mensal: "))
                        if self.salario >= 2000:
                            self.cheque_especial = self.salario * 0.2
                            print(f"Que legal! Você possui limite de Cheque especial no valor de {self.cheque_especial} reais.")
                            self.valor_total = self.saldo + self.cheque_especial
                            print(f"Seu saldo para saque agora é: {self.valor_total} reais.")
                            menu_inicial = int(input("Para ir para SAQUE, digite [1]: "))
                            if menu_inicial == 1:
                                self.acao()
                        else:
                            print("Infelizmente você não possui limite de Cheque especial.")
                    elif decisao_cheque_especial == 2:
                        menu_inicial = int(input("Você será redirecionado para o Menu inicial. Digite [2]: "))
                        if menu_inicial == 2:
                            self.conta_corrente
                        else:
                            print("Opção inválida.")
                    else:
                        print("Por favor, selecione uma das opções")
                        decisao_cheque_especial
            elif opcao == 2:
                print(f"Saldo {self.saldo} reais.\n")
                int(input("Para VOLTAR, digite [1]: \n"))
                if opcao == 1:
                    self.acao()
                else:
                    print("Opção inválida.")
                    self.acao()
            elif opcao == 3:
                valor_deposito = float(input("Informe o valor a ser depositado: "))
                self.saldo = valor_deposito + self.saldo
                print(f"Valor de {valor_deposito} depositado com sucesso!\n")
                print("Retornando as opções anteriores.\n")
                self.acao()                     
            else:
                print("Opção inválida! \nPor favor, tente novamente.")
                self.acao()           
        elif self.conta_universitaria:
            print("Informe uma opção:")
            print("[1] Saque")
            print("[2] Saldo")
            opcao = int(input())
            if opcao == 1:
                valor = float(input("Informe a quantia para o saque: "))
                if self.saldo >= valor:
                    print(f"Saque no valor de {valor} reais realizado.")
                    saldo_atualizado = self.saldo - valor
                    print(f"Saldo atualizado: {saldo_atualizado} reais.\n")
                    print("OBRIGADO POR USAR NOSSOS SERVIÇOS!\nAté logo!")
                else:
                    print("Saldo insuficiente.")
            elif opcao == 2:
                print(f"Saldo {self.saldo} reais.")
                opcao = int(input("Para retornar ao SAQUE, digite o [1]: \n"))
                if opcao == 1:
                    self.acao()
            elif opcao == 3:
                valor_deposito = float(input("Informe o valor a ser depositado: \n"))
                self.saldo = valor_deposito + self.saldo
                print(f"Valor de {valor_deposito} depositado com sucesso!\n")
                print("Retornando as opções anteriores.\n")
                self.acao()
            else:
                print("Opção inválida! \nPor favor, tente novamente.")
                self.conta_universitaria

conta_corrente = True
conta_universitaria = False
           
b = Banco(conta_corrente, conta_universitaria)
if b.autentificacao():
    if b.contas():
        b.acao()