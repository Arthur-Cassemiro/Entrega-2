

class Onibus:
    def __init__(self,placa,preco,motorista,fiscal,rota):
        self.placa = placa
        self.preco = preco
        self.motorista = motorista
        self.fiscal = fiscal
        self.rota = rota

    
    def mostrar(self):
        return 'Nome: {}, preco: R$ {}, motorista: {}, fiscal: {}'.format(self.placa,self.preco,self.motorista,self.fiscal)

    def rotaOnibus(self):

        return 'Rota: {}'.format(self.rota)
        
        


class Ponto:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero

        

class Motorista:
    def __init__(self,nome,onibus):
        self.nome = nome
        self.onibus = onibus

    def mostrar(self):
        return 'Nome: {}, ônibus: {}'.format(self.nome,self.onibus)



class Fiscal:

    def __init__(self,nome,onibus):
        self.nome = nome
        self.onibus = onibus

    def mostrar(self):
        return 'Nome: {}, ônibus: {}'.format(self.nome,self.onibus)


onibus = []
pontos = []
motoristas = []
fiscais = []


def criarOnibus(placa,preco):
    existe = False
    for x in onibus:
        if x.placa == placa:
            existe = True
            print('Esse ônibus já existe.')
            

    if existe == False:
        onib = Onibus(placa,preco,None,None,[])
        onibus.append(onib)

def criarPonto(nome,numero):
    existe = False
    for x in pontos:
        if x.nome == nome or x.numero == numero:
            existe = True
            print('Esse ponto já existe.')


    if existe == False:
        parada = Ponto(nome,numero)
        pontos.append(parada)

def criarMotorista(nome):
    existe = False
    for x in motoristas:
        if x.nome == nome:
            existe = True
            print('Esse motorista já existe.')
    
    if existe == False:
        motorista = Motorista(nome,None)
        motoristas.append(motorista)

def criarFiscal(nome):
    existe = False

    for x in fiscais:
        if x.nome == nome:
            existe = True
            print('Esse fiscal já existe')

    if existe == False:        
        fiscal = Fiscal(nome,None)
        fiscais.append(fiscal)


def mostrarOnibus():
    print("Informação: \n")
    for onib in onibus:
        print(onib.mostrar())

def mostrarRotas():
    print("Rotas: \n")
    for onib in onibus:
        print(onib.rotaOnibus())


def mostrarMotoristas():
    print("Motoristas: \n")
    for motorista in motoristas:
        print(motorista.mostrar())

def mostrarFiscais():
    for fiscal in fiscais:
        print(fiscal.mostrar())


def motoristaParaOnibus(nome_motorista,placa_onibus):

    existe_motorista = False
    existe_onibus = False

    for motorista in motoristas:
        if motorista.nome == nome_motorista:
            existe_motorista = True
            if existe_motorista == True:
                
                for onib in onibus:
                    if onib.placa == placa_onibus:
                        existe_onibus = True
                        if existe_onibus == True:
                            motorista.onibus = onib
                            onib.motorista = motorista
    
    if existe_motorista == False or existe_onibus == False:
        print("Entradas inválidas.")



def fiscalParaOnibus(nome_fiscal,placa_onibus):

    existe_fiscal = False
    existe_onibus = False
    for fiscal in fiscais:
        if fiscal.nome == nome_fiscal:
            existe_fiscal = True
            if existe_fiscal == True:
                for onib in onibus:
                    if onib.placa == placa_onibus:
                        existe_onibus = True
                        if existe_onibus == True:
                            fiscal.onibus = onib
                            onib.fiscal = fiscal


    if existe_fiscal == False or existe_onibus == False:
        print("Entradas inválidas.")


def adicionarParada(nome_parada,placa_onibus):
    existe_parada = False
    existe_onibus = False
    
    for parada in pontos:
        if parada.nome == nome_parada:
            existe_parada == True
    
    for onib in onibus:
        if onib.placa == placa_onibus:
            existe_onibus == True

    
    if existe_parada and existe_onibus:
        for ponto in pontos:
            if parada.nome == nome_parada:
                for onib in onibus:
                    if onib.placa == placa_onibus:
                       onib.rota.append(nome_parada)

    if existe_parada == False or existe_onibus == False:
        print("Entradas inválidas.")


def alterarOnibus(placa_onibus,novo_nome,novo_preco):

    existe_onibus = False

    for onib in onibus:
        if onib.placa == placa_onibus:
            existe_onibus = True
            if existe_onibus == True:
                onib.placa = novo_nome
                onib.preco = novo_preco
    
    if existe_onibus == False:
        print("O ônibus não existe.")


def alterarParada(ponto_nome,novo_nome,novo_numero):

    existe_parada = False

    for ponto in pontos:
        if ponto.nome == ponto_nome:
            existe_parada = True
            if existe_parada:
                ponto.nome = novo_nome
                ponto.numero = novo_numero
    
    if existe_parada == False:
        print("O ponto não existe.")



def alterarMotorista(motorista_nome,novo_nome):

    existe_motorista = False

    for motorista in motoristas:
        if motorista.nome == motorista_nome:
            existe_motorista = True
            if existe_motorista:
                motorista.nome = novo_nome

    if existe_motorista == False:
        print("O motorista não existe.")


def alterarFiscal(fiscal_nome,novo_nome):

    existe_fiscal = False

    for fiscal in fiscais:
        if fiscal.nome == fiscal_nome:
            existe_fiscal = True
            if existe_fiscal:
                fiscal.nome = novo_nome
    
    if existe_fiscal == False:
        print("O fiscal não existe.")


def alterarRota(placa_nome,nome,novo_nome,novo_numero):

    existe_onibus = False
    existe_parada = False

    for onib in onibus:
        if onib.placa == placa_nome:
            existe_onibus = True
            if existe_parada:
                for parada in onib.rota:
                    if onib.rota.nome == nome:
                        existe_parada = True
                        if existe_parada:
                            onib.rota.nome = novo_nome
                            onib.rota.numero = novo_numero

    if existe_onibus == False or existe_parada == False:
                print("Entradas inválidas.")



def deletarOnibus(placa_onibus):
    existe_onibus = False
    for onib in onibus:
        if onib.placa == placa_onibus:
            existe_onibus == True
            if existe_onibus:
                onibus.remove(onib)
    
    if existe_onibus == False:
        print('Entrada errada.')


def deletarPonto(nome_ponto):
    existe_ponto = False
    for ponto in pontos:
        if ponto.nome == nome_ponto:
            existe_ponto = True
            if existe_ponto:
                pontos.remove(ponto)

    if existe_ponto == False:
        print('Entrada errada.')

def deletarMotorista(nome_motorista):
    existe_motorista = False
    for motorista in motoristas:
        if motorista.nome == nome_motorista:
            existe_motorista = True
            if existe_motorista:
                motoristas.remove(motorista)
    
    if existe_motorista == False:
        print('Entrada errada.')

def deletarFiscal(nome_fiscal):
    existe_fiscal = False
    for fiscal in fiscais:
        if fiscal.nome == nome_fiscal:
            existe_fiscal = True
            if existe_fiscal:
                fiscais.remove(fiscal)

    if existe_fiscal == False:
        print('Entrada errada.')





rodar = True
print("Essa são as opções\n")
print("1-Criar ônibus\n")
print("2-Criar ponto de parada \n")
print("3-Criar motorista\n")
print("4-Criar fiscal\n")
print("5-Mostrar ônibus\n")
print("6-Mostrar rotas\n")
print("7-Mostrar motoristas\n")
print("8-Mostar fiscais\n")
print("9-Assignar motorista ao ônibus\n")
print("10-Assignar fiscal ao ônibus\n")
print("11-Adicionar parada ao ônibus\n")
print("12-Alterar dados do ônibus\n")
print("13-Alterar dados da parada\n")
print("14-Alterar dados do motorista\n")
print("15-Alterar dados do fiscal\n")
print("16-Alterar rota do ônibus\n")
print("17-Deletar ônibus\n")
print("18-Deletar ponto de parada\n")
print("19-Deletar motorista\n")
print("20-Deletar fiscal\n")
print("21-Sair do programa\n")





while(rodar):

    value = int(input("Digite o número correpondente a opção desejada:"))
    
    if value == 1:
        placa = input('Digite a placa do ônibus: ')
        preco = float(input('Digite o preço: '))
        criarOnibus(placa,preco)
    
    elif value == 2:
        nome_ponto = input('Digite o nome do ponto:')
        numero = int(input('Digite a numeração do ponto: '))    
        criarPonto(nome_ponto,numero)
    
    elif value == 3:
        nome_motorista = input('Digite o nome do motorista: ')
        criarMotorista(nome_motorista)
    
    elif value == 4:
        nome_fiscal = input('Digite o nome do fiscal: ')
        criarFiscal(nome_fiscal)
    
    elif value == 5:
        mostrarOnibus()

    elif value ==6 :
        mostrarRotas()
    
    elif value == 7:
        mostrarMotoristas()
    
    elif value == 8:
        mostrarFiscais()
    
    elif value == 9:
        nome_motorista= input("Digite o nome do motorista: ")
        placa_onibus = input("Digite a placa do ônibus que irá receber o motorista: ")
        motoristaParaOnibus(nome_motorista,placa_onibus)
    
    elif value == 10:
        nome_fiscal = input("Digite o nome do fiscal que irá para o ônibus: ")
        placa_onibus = input("Digite a placa do ônibus que irá receber o motorista: ")
        fiscalParaOnibus(nome_fiscal,placa_onibus)
    
    elif value == 11:
        nome_parada = input("Digite o nome da parada: ")
        placa_onibus = input("Digite a placa do ônibus que passará pela parada.")
        adicionarParada(nome_parada, placa_onibus)
    
    elif value == 12:
        placa_antiga= input("Digite a antiga placa do ônibus: ")
        placa_nova = input("Digite a nova placa do ônibus: ")
        preco = float(input("Digite o novo preço: "))
        alterarOnibus(placa_antiga,placa_nova,preco)

    elif value == 13:
        nome_antigo = input("Digite o nome antigo da parada: ")
        novo_nome = input("Digite o no nome da parada: ")
        novo_numero = int(input("Digite o novo número da parada: "))
    
    elif value == 14:
        nome_antigo = input("Digite o nome antigo do motorista: ")
        novo_nome = input("Digite o novo nome do motorista: ")
        alterarMotorista(nome_antigo,novo_nome)

    elif value == 15:
        nome_antigo = input("Digite o nome antigo do fiscal: ")
        novo_nome = input("Digite o novo nome do fiscal: ")
        alterarFiscal(nome_antigo,novo_nome)

    elif value == 16:
        placa = input("Digite a placa do ônibus que você deseja alterar a rota: ")
        nome_antigo = input("Digite o nome da parada que você deseja mudar: ")
        nome_novo = input("Digite o novo nome da parada: ")
        novo_numero = int(input("Digite o novo número da parada: "))
        alterarRota(placa,nome_antigo,novo_nome,novo_numero)
    
    elif value == 17:
        placa = input("Digite a placa do ônibus que deseja deletar: ")
        deletarOnibus(placa)
    
    elif value == 18:
        nome = input("Digite o nome da parada que você deseja deletar: ")
        deletarPonto(nome)
    
    elif value == 19:
        nome = input("Digite o nome do motorista que você deseja deletar:")
        deletarMotorista(nome)
    
    elif value == 20:
        nome = input("Digigta o nome do fiscal que deseja excluir: ")
        deletarFiscal(nome)
    
    elif value == 21:
        rodar = False 

    else:
        print("Valor não reconhecido.")