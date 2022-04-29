import this
import ModelCalculadora
opcao = 0
num1 = 0
num2 = 0

def menu():
    print('Escolher uma das opções abaixo:\n' +
          '1. Soma\n' +
          '2. Subtração\n' +
          '3. Divisão\n' +
          '4. Multiplicação\n' +
          '5. Tabuada')
    this.opcao = int(input())

def ColetarNum1():
    print('Informe o Primeiro Número')
    this.num1 = float(input())

def ColetarNum2():
    print('Imforme o Segundo Número')
    this.num2 = float(input())

def Operacao():
    menu()
    if(this.opcao == 1):
        ColetarNum1()
        ColetarNum2()
        print(ModelCalculadora.somar(this.num1, this.num2))
    elif this.opcao == 2:
        ColetarNum1()
        ColetarNum2()
        print(ModelCalculadora.subtrair(this.num1, this.num2))
    elif this.opcao == 3:
        ColetarNum1()
        ColetarNum2()
        print(ModelCalculadora.dividir(this.num1, this.num2))
    elif this.opcao == 4:
        ColetarNum1()
        ColetarNum2()
        print(ModelCalculadora.multiplicar(this.num1, this.num2))
    elif this.opcao == 5:
        ColetarNum1()
        print(ModelCalculadora.tabuada(this.num1))
    else:
        print('Número Digitado Invalido!')
