class Veiculo:

    def __init__(self, cor, placa, numero_rodas):
        self.cor=cor
        self.placa=placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    

   
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor,placa,numero_rodas)
        self.carregado= carregado
    
    def esta_carregado(self):
        print("Sim" if self.carregado else "Não esta carregado")
    def __str__(self):
    
        status_carregado = "Sim" if self.carregado else "Não"
        return f"{super().__str__()}, Carregado={status_carregado}"

    

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass


moto = Motocicleta("preta", "abd-123", 2)
moto.ligar_motor()

carro = Carro("Prata", "acb-534", 4)
carro.ligar_motor()

caminhao = Caminhao("Azul", "dse-659",8, False)
caminhao.ligar_motor()

print(caminhao)
