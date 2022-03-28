import time

class Pilha:
    def __init__(self):
        self.items = []
    
    def vazio(self):
        if len(self.items) == 0:
            print('a pilha esta vazia')
        
        else:
            print('pilha nao vazia')

    def full(self):

        if len(self.items) == 10:
            print('lista cheia')
        else:
            print('esta vazia')
    


    def pop(self):
        return self.items.pop(time)
    
    def push(self,item):
        self.items.append(item)
        print(self.items)

    def peek(self):
        return self.items[len(self.itens)-1]
    
    def size(self):
        return len(self.items)
    def tempo_calc(self):
        tempo1 = time.time()
        sum(self.items)
        tempo2 = time.time()
        tempo = tempo2 - tempo1
        print('o valor somado é de: ', tempo)
s = Pilha()
s.full()
for i in range(10):
    s.push(i)

s.full()
s.tempo_calc()