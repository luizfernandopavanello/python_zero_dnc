'''Exercícios'''
"""1. Recrie a classe Carro e adicione um novo atributo e um novo método (função)."""
"""
class Motorbike():
  def __init__(self, time, velocity=0):
      self.time = time
      self.velocity = velocity

  def vel(self,time=20):
    print("Ainda faltam ",self.time,"minutos para chegar")

  def accelerate(self,velocity=0):
    velocity=self.velocity
    if self.velocity < 120:
      self.time = self.time-2   
      print("Velocity: ",self.velocity,"\nTempo para chegar: ",self.time, "minutos")
    else:
      self.time = self.time-5
      print("Velocity: ",self.velocity,"\nTempo para chegar: ",self.time, "minutos")

ducati = Motorbike(time=20)
stop = 30 

ducati.vel()#acessando função gasolina
ducati.velocity=120
ducati.accelerate()
ducati.velocity=99
ducati.accelerate()
ducati.time=ducati.time+stop
ducati.accelerate()
"""
"""2. Crie uma sub classe a partir da classe criada no exercício 1."""
"""3. Sobreescreva um dos operadores dentro de uma nova classe."""
"""
class harley(Motorbike):
  def __init__(self):  # o construtor da subclasse chama o construtor da superclasse
                         # com parametros desejados
    Motorbike.__init__(self,time=15,velocity = 100)
    


  def nitro(self):
    self.time = self.time-10
    print("Nova velocidade ",self.velocity*3," KM/h""\nTempo para chegar: ",self.time, "minutos")

beast = harley()
beast.accelerate()
beast.nitro()
"""
"""4. Crie uma classe chamada Calculadora com os atributos Digito 1 e Digito2, crie os métodos de adição e de subtração."""

class Calculator():
    def __init__(self, dig1=0, dig2=0):
        self.dig1 = dig1
        self.dig2 = dig2

    def __add__(self, dig1, dig2):
        self.dig1 = dig1
        self.dig2 = dig2
        print(self.dig1 + self.dig2)
    
    def __sub__(self, dig1, dig2):
        self.dig1 = dig1
        self.dig2 = dig2
        print(self.dig1 - self.dig2)
    
operator = Calculator()
operator.__add__(1, 2) 
operator.__sub__(3, 2)



"""5. Crie uma subclasse de Calculadora e adicione os métodos de divisão, multiplicação e exponencial."""
