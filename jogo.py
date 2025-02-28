from pilhas import Pilha
from random import randint

def add_pilhas(n:int) -> list[Pilha]: 
    '''
    Aviso: '' => Espaço vazio ou lixo!!
    Adiciona as *n* pilhas iniciais do jogo em uma lista, com duas pilhas extras para a manipulação dos números.

    >>> lista = add_pilhas(4)
    >>> lista
    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']] #Lista de Pilhas
    '''
    lista_util: list = []
    for i in range(n + 2):
        p = Pilha()
        lista_util.append(p)
    return lista_util


def Insere_num(x:int, p:Pilha) -> Pilha:
    '''
    Insere o número no topo *x*, na pilha *p*, se ela não estiver cheia.
    >>> p = Pilha()
    >>> Insere_num(1, p)
    >>> p.elem
    [1, '', '', '']
    >>> Insere_num(5, p)
    >>> p.elem
    [1, 5, '', '']
    >>> Insere_num(3, p)
    >>> Insere_num(2, p)
    >>> p.elem
    [1, 5, 3, 2]
    >>> Insere_num(3, p)
    >>> p.elem
    [1, 5, 3, 2]
    '''
    if not p.pilha_cheia():
        p.empilha(x)

def Arruma_pilha(p_inicial: Pilha, p_final:Pilha) -> Pilha:
    '''
    Transfere todos os elementos da *p_inicial* na *p_final*
    >>> p_final = Pilha()
    >>> Insere_num(5, p_final)
    >>> p_inicial = Pilha()
    >>> Insere_num(2, p_inicial)
    >>> Insere_num(3, p_inicial)
    >>> Insere_num(1, p_inicial)
    >>> Arruma_pilha(P_inicial, P_final)
    >>> P_final.elem
    [5, 1, 3, 2]
    >>> P_inicial.elem
    ['', '', '', '']
    '''

    while not p_inicial.pilha_vazia():
                    y = p_inicial.desempilha()
                    p_final.empilha(y)

def Verifica_x(x: int, Lista:list[Pilha]) -> bool: 
    '''
    Retorna False caso o número já tenha sido adicionado na lista de pilhas *Lista* o máximo de vezes possíveis, caso contrário retorna True 
    >>> p1 = Pilha()
    >>> p2 = Pilha()
    >>> p3 = Pilha()
    >>> p4 = Pilha()
    >>> Insere_num(1, p1)
    >>> Insere_num(2, p1)
    >>> Insere_num(2, p1)
    >>> Insere_num(1, p1)
    >>> p1.elem 
    [1, 2, 2, 1]
    >>> Insere_num(2, p1)
    >>> Insere_num(2, p1)
    >>> p2.elem
    [2, 2, '', '']
    >>> p3
    ['', '', '', '']
    >>> p4
    ['', '', '', '']
    >>> Lista = [p1, p2, p3, p4]
    >>> x = 2
    >>> Verifica_x(x, Lista)
    False
    >>> x = 1
    >>> Verifica_x(x, Lista)
    True    
            '''
    contador = 0 
    aux = Pilha()
    for pilha in Lista: 
        while not pilha.pilha_vazia():
            j = pilha.desempilha()
            aux.empilha(j)
            if x == j:
                contador += 1
        Arruma_pilha(aux, pilha)
    if contador == (pilha.TamMax + 1):
        return False
    else:
        return True

def Cria_Pilhas_Aleatórias(n: int, pilha:Pilha, Lista: list[Pilha]) -> Pilha:
    '''
    Cria uma pilha com números aleatórios que estão entre 1 e *n*

    >>> p = Pilha()
    >>> n = 3
    >>> Lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9] #Lista de pilhas
    >>> Cria_Pilhas_Aleatórias(n, p, Lista)
    >>> p
    [3, 2, 2, 1] #Exemplo
    '''
    while not pilha.pilha_cheia():
        x: int = randint(1, n)
        while not Verifica_x(x,Lista) == True:
            x = randint(1, n)
        Insere_num(x, pilha)


def Troca_Pilha(P_Origem: Pilha, P_Destino: Pilha) -> Pilha: 
    '''
    Transfere o elemento do topo da *P_Origem* para o topo da *P_Destino*, porém, a *P_Destino* não pode estar cheia,
    a *P_Origem* não pode estar vazia, e o elemento do topo da *P_Origem* deve ser igual ao elemento do topo da *P_Destino*.

    >>> p = Pilha()
    >>> Insere_num(2, p)
    >>> Insere_num(3, p)
    >>> p.elem
    [2, 3, '', '']
    >>> p1 = Pilha()
    >>> Insere_num(1, p1)
    >>> Insere_num(3, p1)
    >>> p1.elem
    [1, 3, '', '']
    >>> Troca_Pilha(p, p1)
    >>> p.elem
    [2, '', '', '']
    >>> p1.elem
    [1, 3, 3, '']

    >>> p3 = Pilha()
    >>> Insere_num(1, p3)
    >>> Insere_num(3, p3)
    >>> p3.elem
    [1, 3, '', '']
    >>> p4 = Pilha()
    >>> Insere_num(2, p4)
    p4.elem
    [2, '', '', '']
    >>> Troca_Pilha(p3, p4)
    "Troca inválida:O elemento do topo da pilha de origem é diferende do topo da pilha de destino!"

    >>> p5 = Pilha()
    >>> Insere_num(2, p5)
    >>> Insere_num(1, p5)
    >>> p5.elem
    [2, 1, '', '']
    >>> p6 = Pilha()
    >>> Insere_num(1, p6)
    >>> Insere_num(3, p6)
    >>> Insere_num(2, p6)
    >>> Insere_num(1, p6)
    >>> p6.elem
    [1, 3, 2, 1]
    >>> Troca_Pilha(p5, p6)
    "Troca inválida: A pilha de destino está cheia!"

    >>> p7 = Pilha()
    >>> p7.elem
    ['', '' , '', '']
    >>> p8 = Pilha()
    >>> Insere_num(2, p8)
    >>> Insere_num(3, p8)
    >>> p8.elem
    [2, 3, '', '']
    >>> Troca_Pilha(p7, p8)
    "Troca inválida: A pilha de origem está vazia!")

    '''
    if not P_Origem.pilha_vazia():
        if not P_Destino.pilha_cheia():   
            if  P_Destino.pilha_vazia() or P_Origem.elemento_do_topo() == P_Destino.elemento_do_topo():    
                x = P_Origem.desempilha()
                P_Destino.empilha(x)
            else:
                print("Troca inválida:O elemento do topo da pilha de origem é diferende do topo da pilha de destino!")
        else:
            print("Troca inválida: A pilha de destino está cheia!")
    else:
        print("Troca inválida: A pilha de origem está vazia!")

def Ultimo_elem(P: Pilha) -> int:
    '''
    Encontra o último elemento da pilha *P*


    >>> p = Pilha()
    >>> Insere_num(1, p)
    >>> Insere_num(4, p)
    >>> Insere_num(3, p)
    >>> Insere_num(2, p)
    >>> p.elem
    [1, 4, 3, 2]
    >>> Ultimo_elem(p)
    1
    '''
    pAux = Pilha()
    Aux = int
    topo = P.topo
    Aux = P.topo   
    while Aux != 0:
        x = P.desempilha()
        pAux.empilha(x)
        Aux = Aux - 1
    y = P.elemento_do_topo()
    while Aux != topo:
        x = pAux.desempilha()
        P.empilha(x)
        Aux = Aux + 1

    return y

def Verifica_pilha(P_verificar: Pilha) -> bool:
    '''
    Retorna True se *P_verificar* está cheia com todos os elementos iguais ou se a pilha está vazia, 
    caso contrário retorna False

    >>> p = Pilha()
    >>> Insere_num(3, p)
    >>> Insere_num(3, p)
    >>> Insere_num(3, p)
    >>> Insere_num(3, p)
    >>> p.elem
    [3, 3, 3, 3]
    >>> Verifica_pilha(p)
    True
    >>> p1 = Pilha()
    >>> p1.elem 
    ['', '', '', '']
    >>> Verifica_pilha(p1)
    True
    >>> p2 = Pilha()
    >>> Insere_num(3, p)
    >>> Insere_num(3, p)
    >>> Insere_num(3, p)
    >>> p2.elem
    [3, 3, 3, '']
    >>> Verifica_pilha(p2)
    False
    >>> p3 = Pilha()
    >>> Insere_num(3, p)
    >>> Insere_num(1, p)
    >>> Insere_num(3, p)
    >>> Insere_num(2, p)
    p3.elem
    [3, 1, 3, 2]
    >>> Verifica_pilha(p3)
    False    
    '''
    if  P_verificar.pilha_vazia(): 
        return True
    p_Armazenador = Pilha()
    num_pilha = Ultimo_elem(P_verificar)
    if P_verificar.pilha_cheia():
        for i in range(0, P_verificar.TamMax + 1):
            if num_pilha == P_verificar.elemento_do_topo():
                y = P_verificar.desempilha()
                p_Armazenador.empilha(y)
            else: 
                Arruma_pilha(p_Armazenador, P_verificar)
                return False
        Arruma_pilha(p_Armazenador, P_verificar)
    else:
        return False
    return True

def Verifica_todas_pilhas(Lista: list[Pilha]) -> bool:
    '''
    Retorna True se todas as pilhas da *Lista* está cheia com todos os elementos iguais ou se a pilha está vazia, 
    caso contrário retorna False.

    >>> p = [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], ['', '', '', ''], ['', '', '', '']] #Lista de Pilhas
    >>> Verifica_todas_pilhas(p)
    True
    >>> p1 = [[3, 3, 2, 3], [2, 2, 1, 2], [1, 1, 3, 1], ['', '', '', ''], ['', '', '', '']] #Lista de Pilhas
    >>> Verifica_todas_pilhas(p1)
    False
    >>> p2 = [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, ''], [2, '', '', ''], ['', '', '', '']] #Lista de Pilhas
    >>> Verifica_todas_pilhas(p1)
    False
    '''
    for pilha in Lista:
        if Verifica_pilha(pilha) == False: 
            return False
    return True

def imprime_lista(Lista: list[Pilha],n:int): 
    '''
    Imprime na tela todos os elementos de cada pilha separadamente de forma vertical e após finalizar cada pilha imprime o seu número.

    
    >>> lista = [[3, 2, 1, 1], [2, 1, 3, 2], [2, 1, 3, 3], ['', '', '', ''], ['', '', '', '']] #Lista de Pilhas
    >>> imprime_lista(lista, 3)
    1
    1
    2
    3
    P1

    2
    3
    1
    2
    P2

    3
    3
    1
    2
    P3

    P4

    P5
    
    '''
    num: int = n-1
    aux = Pilha()
    for pilha in Lista:
        while not pilha.pilha_vazia():
            print(pilha.elemento_do_topo())
            x = pilha.desempilha()
            aux.empilha(x)
        print(f"P{n-num}\n")
        num -= 1
        Arruma_pilha(aux, pilha)   

        
def main():
    n: int = int(input("Digite o numero de pilhas:  "))
    Lista:list = add_pilhas(n)
   #Gera n pilhas com números de 1 até n
    contador:int = 0
    while contador != n:
        Cria_Pilhas_Aleatórias(n, Lista[contador],Lista)
        contador = contador + 1
    
    #Printa todas as pilhas na lista de pilhas 
    imprime_lista(Lista, n)

    #Verifica a quantidade de trocas necessárias para vencer o jogo 
    cont: int = 0
    #Interface do jogo, interação com o usuário e verificação da conclusão do jogo
    while Verifica_todas_pilhas(Lista) == False:
        p_desempilha = int(input("Digite o número da pilha de origem: "))
        p_empilha = int(input("Digite o número da pilha de destino: "))
        Troca_Pilha(Lista[p_desempilha - 1], Lista[p_empilha - 1])
        cont +=1
        imprime_lista(Lista,n)
        '''for i, pilha in enumerate(Lista): #printar na vertical
            print(f"Pilha {i + 1}: {pilha.elem}") Não podemos usar .elem '''
    #Mensagem da conclusão do jogo
    print("Você venceu o jogo após:", cont, "trocas")

 
if __name__ == '__main__':
    main()
