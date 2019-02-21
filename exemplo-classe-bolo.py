# Definimos uma classe em Python com a palavra reservada "class" e indicando
# qual é o nome da classe. Por convenção, todas as classes obrigatoriamente
# devem ter a primeira letra em maiúsculo.
class BoloLaranja:
    # Se definirmos um atributo (variável de uma classe) fora do construtor
    # da mesma, estamos definindo um atributo da CLASSE, e portanto todas
    # as instâncias criadas a partir dessa classe terão o mesmo valor palavra
    # esse atributo.
    sabor = 'laranja'

    # A função __init__ é o construtor da classe BoloLaranja. Construtor, em 
    # linguagens de programação orientadas a objeto é um método chamado assim
    # que uma nova instância do objeto for criada. Tal método é responsável
    # pela definição inicial dos atributos. Obrigatoriamente o primeiro 
    # parâmetro declarado no construtor referencia a instância que foi criada.
    def __init__(instancia, ovos, andares):
        instancia.qtde_ovos = ovos
        instancia.qtde_andares = andares

    # Método (função) da classe BoloLaranja. Obrigatoriamente deve existir um
    # parâmetro que referencie a instância, e se na função houver mais do que
    # um parâmetro, o primeiro será SEMPRE o que referencia a instância.
    def assar(instancia, tempo):
        print(f'O bolo de {instancia.qtde_andares} andares está assando por {tempo} minutos, e possui {instancia.qtde_ovos} ovos!')

    # Outro método (função) da classe BoloLaranja:
    def servir(instancia):
        print('O bolo foi servido!')

# Instanciando BoloLaranja na variável "x":
x = BoloLaranja(4, 1) # Agora "x" é uma instância da classe BoloLaranja

# Instanciando BoloLaranja na variável "y":
y = BoloLaranja(10, 3) # Agora "y" é uma instância da classe BoloLaranja

# Chamando os métodos nas instâncias:
x.assar(15)
x.servir()
