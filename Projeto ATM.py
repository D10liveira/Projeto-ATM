class Banco:
    def __init__(self, conta_corrente, conta_universitaria):
        self.conta_corrente = conta_corrente
        self.conta_universitaria = conta_universitaria
        self.saldo = 1000
    
    def autentificacao(self):
        while True:
            nome_completo = input("Por favor, insira seu nome completo: ")
            CPF = input("Por favor, insira seu CPF: ")
            print()
            if len(nome_completo.split()) >= 2 and len(CPF) == 11:
                print("Bem-vindo,", nome_completo)
                print()
                return True
            else:
                print("Dados incorretos. Tente novamente com nome e sobrenome.\nObs. Campo CPF precisa conter 11 dígitos.")
            
    def contas(self):
        print("Selecione o tipo de conta:")
        print("[1] Conta Corrente")
        print("[2] Conta Universitária")
        escolha = int(input())
        print()
        
        if escolha == 1:
            self.conta_corrente = True
            self.conta_universitaria = False
        elif escolha == 2:
            self.conta_corrente = False
            self.conta_universitaria = True
        else:
            print("Opção inválida!")
            self.contas()
        return True

    def acao(self):
        if self.conta_corrente:
            print("O que deseja fazer?")
            print("[1] SAQUE")
            print("[2] SALDO")
            print("[3] DEPÓSITO")
            opcao = int(input())
            print()
            
            if opcao == 1:
                valor = float(input("Informe a quantia para o saque: "))
                print()
                if self.saldo >= valor:
                    print(f"Saque no valor de {valor} reais realizado.")
                    saldo_atualizado = self.saldo - valor
                    print(f"Saldo atual: {saldo_atualizado:.2f} reais.\n")
                    print("OBRIGADO POR USAR NOSSOS SERVIÇOS!\nAté logo!")   
                else:
                    print("Saldo insuficiente.")
                    print("Você pode ter limite de Cheque especial disponível.\nGostaria de consultar?")
                    decisao_cheque_especial = int(input("[1] SIM\n[2] NÃO\n"))
                    if decisao_cheque_especial == 1:
                        self.salario = float(input("Para continuarmos, por favor, insira o valor do seu salário mensal: "))
                        if self.salario >= 2000:
                            self.cheque_especial = self.salario * 0.2
                            print(f"Que legal! Você possui limite de Cheque especial no valor de {self.cheque_especial:.2f} reais.")
                            opcao = int(input("Gostaria de contratar o Limite de Cheque Especial?\n[1] SIM\n[2] NÃO\n"))
                            if opcao == 1:
                                self.valor_total = self.saldo + self.cheque_especial
                                print(f"Parabéns! Seu saldo para saque agora é de {self.valor_total:.2f} reais.\n")
                                self.saldo = self.valor_total
                                menu_inicial = int(input("Para ir para SAQUE, digite [1]: "))
                                if menu_inicial == 1:
                                    self.acao()
                            elif opcao == 2:
                                print("Você será redirecionado para o MENU INICIAL.")
                                self.acao()
                            else:
                                menu_inicial = int(input("Para ir para SAQUE, digite [1]: "))
                                if menu_inicial == 1:
                                    self.acao()
                        else:
                            print("Infelizmente você não possui limite de Cheque especial.")
                    elif decisao_cheque_especial == 2:
                        menu_inicial = int(input("Você será redirecionado para o Menu inicial. Digite [2]: "))
                        if menu_inicial == 2:
                            self.acao()
                        else:
                            print("Opção inválida.")
                    else:
                        print("Por favor, selecione uma das opções")
                        decisao_cheque_especial
            elif opcao == 2:
                print(f"Saldo {self.saldo:.2f} reais.\n")
                print("Você está sendo redirecionado para as opções anteriores...\n")
                self.acao()
            elif opcao == 3:
                valor_deposito = float(input("Informe o valor a ser depositado: "))
                print()
                self.saldo = valor_deposito + self.saldo
                print(f"Valor de {valor_deposito:.2f} depositado com sucesso!\n")
                print("Você está sendo redirecionado para as opções anteriores...\n")
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
                    print(f"Saldo atualizado: {saldo_atualizado:.2f} reais.\n")
                    print("OBRIGADO POR USAR NOSSOS SERVIÇOS!\nAté logo!")
                else:
                    print("Saldo insuficiente.")
            elif opcao == 2:
                print(f"Saldo {self.saldo:.2f} reais.")
                opcao = int(input("Para retornar ao SAQUE, digite o [1]: \n"))
                if opcao == 1:
                    self.acao()
            elif opcao == 3:
                valor_deposito = float(input("Informe o valor a ser depositado: \n"))
                self.saldo = valor_deposito + self.saldo
                print(f"Valor de {valor_deposito:.2f} depositado com sucesso!\n")
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
