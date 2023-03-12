import datetime

class Carro:
    def __init__(self, placa, valordiaria, data_alugar, data_devolver, ndias, valor_aluguel, data_devolvendo,status):
        self.placa = placa
        self.valordiaria = valordiaria

        self.data_alugar = data_alugar
        self.data_devolver = data_devolver
        self.data_devolvendo = data_devolvendo

        self.ndias = ndias
        self.valor_aluguel = valor_aluguel 

        self.status = status

    def aluguel (self, diax, mesx, anox): 
        data1= datetime.date(day=diax, month=mesx, year=anox)  
        self.data_alugar = data1
      
    def devolucao (self, diay, mesy, anoy): 
        data2= datetime.date(day=diay, month=mesy, year=anoy)  
        self.data_devolver = data2  

    def devolvendo (self, diaz, mesz, anoz): 
        data3= datetime.date(day=diaz, month=mesz, year=anoz)  
        self.data_devolvendo = data3       
    
    def dias(self): 
        dias = (self.data_devolver - self.data_alugar).days
        self.ndias = dias 
        return self.ndias
    
    def valor(self):
        self.valor_aluguel = self.ndias*self.valordiaria
        return self.valor_aluguel


carro1 = Carro('ABC-1234', 50, '0/0/0', '0/0/0', 0, 0, '0/0/0', 'DISPONÍVEL')    

def menu_data():
    print('1 - ALUGAR CARRO')
    print('2 - DEVOLVER CARRO')
    print('3 - SAIR DO PROGRAMA')

menu_data()
escolha = int(input('Digite sua escolha: '))
while escolha != 3:

    if escolha == 1: 
        print('Digite a data de aluguel do carro: ')
        diax = int(input('Dia: '))
        mesx = int(input('Mês: '))
        anox = int(input('Ano: '))
        carro1.aluguel(diax, mesx, anox) 
        print('Você alugou o carro na data: ', carro1.data_alugar)

        print('Digite a data de devolução do carro: ')
        diay = int(input('Dia: '))
        mesy = int(input('Mês: '))
        anoy = int(input('Ano: '))  
        carro1.devolucao(diay, mesy, anoy) 
        print('Você pretende devolver o carro na data: ', carro1.data_devolver)
        carro1.status = 'ALUGADO'

    elif escolha == 2: 
        print('Digite a data que você está devolvendo o carro: ')
        diaz = int(input('Dia: '))
        mesz = int(input('Mês: '))
        anoz = int(input('Ano: '))
        carro1.devolvendo(diaz, mesz, anoz) 

        if carro1.data_devolvendo == carro1.data_devolver: 
            print('Você ficou com o carro por ', carro1.dias(), " dias")
            print('Como a diária é R$50...')
            print('Valor a ser pago: R$', carro1.valor())
            carro1.status = 'DISPONÍVEL'

        elif carro1.data_devolvendo < carro1.data_devolver: 
            print('Você ficou com o carro por ', carro1.dias()-(carro1.data_devolvendo-carro1.data_alugar).days, " dias")
            print('Como a diária é R$50...')
            print('Valor a ser pago: R$', (carro1.data_devolvendo-carro1.data_alugar).days*carro1.valordiaria)   
            carro1.status = 'DISPONÍVEL'

        else:
            atraso = (carro1.data_devolvendo - carro1.data_alugar).days - carro1.dias()
            valor_multa = atraso*((carro1.valordiaria*20)/100)
            print('Você atrasou o aluguel em ', atraso, ' dias')
            print('Será cobrado R$', valor_multa, 'a mais, já que é cobrado R$10.0 por cada dia de atraso')
            print('Valor cobrado pelos dias que foi alugado: R$', carro1.valor())
            print('Valor a ser pago: R$', carro1.valor() + valor_multa)
            carro1.status = 'DISPONÍVEL'

    else: 
        print('OPÇÃO INVÁLIDA')
 
    menu_data() 
    escolha = int(input('Digite sua escolha: '))  

print('FIM DO PROGRAMA')