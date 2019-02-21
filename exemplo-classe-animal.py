class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print('Nhom nhom')

# A classe Gato é herdeira da classe Animal, uma vez que ao declarar
# a classe, definimos "class Gato(Animal)". A partir disso, podemos
# dizer que qualquer instância a partir de Gato possuirá os atributos
# e métodos declarados em Animal. Por exemplo, além de possuir os
# atributos "nome" e "dono", as instâncias de Gato também possuirão
# um atributo chamado "raca" e um método chamado "miar".
class Gato(Animal):

    # Ao criar o construtor da classe Gato, precisamos passar como
    # parâmetros necessários para a criação de um gato qual é
    # o valor de "nome" e "raca" (atributos de Animal), uma vez que 
    # o construtor de Gato DEVE chamar o construtor de Animal. Sem
    # chamar o construtor de Animal não podemos referir que a instância
    # criada é um Animal.
    def __init__(self, nome, dono, raca):

        # A função "super" é utilizada para podermos acessar os atributos
        # e métodos da classe pai. Como precisamos chamar o construtor de
        # Animal no construtor de Gato para definirmos os valores dos 
        # atributos "nome" e "dono", fazemos isso com o "super".
        super().__init__(nome, dono)
        self.raca = raca

    def miar(self):
        print('Minhauuuuu')

class Cachorro(Animal):
    def latir(self):
        print('Au auuuu')

gato = Gato('xuxuzinho', 'Matheus', 'siames')
cachorro = Cachorro('rex', 'Bárbara')
animal = Animal('nome', 'dono')

print(gato.raca)