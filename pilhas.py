class Pilha:
    TamMax: int
    elem: list
    topo: int

    def __init__(self): 
        self.TamMax = 3
        self.topo = -1
        self.elem = [""] * (self.TamMax + 1)
    
    def inicializa_pilha(self): 
        self.topo = -1

    def pilha_vazia(self):
        return self.topo == -1
    
    def pilha_cheia(self):
        return self.topo == self.TamMax
    
    def empilha(self, x):
        if not self.pilha_cheia():
            self.topo += 1
            self.elem[self.topo] = x
    
    def desempilha(self):
        if not self.pilha_vazia():
            x = self.elem[self.topo]
            self.topo -= 1
            return x
    
    def elemento_do_topo(self):
        if not self.pilha_vazia():
            return self.elem[self.topo]
        else:
            print("<erro>")