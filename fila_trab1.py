import time

class fila:
    def __init__(self):
        self.items = []
    
    def vazio(self):
        if len(self.items) == 0:
            print('a fila esta vazia')
        
        else:
            print('fila nao vazia')

    def full(self):

        if len(self.items) == 1000000:
            print('fila cheia')
        else:
            print('esta vazia')
    


    def pop(self):
        return self.items.pop(time)
    
    def push(self,item):
        self.items.insert(0,item)
        print(self.items)

    def peek(self):
        return self.items[len(self.itens)-1]
    
    def size(self):
        return len(self.items)
    def tempo_calc(self):
        tempo1 = time.time()
        
        s = sum(self.items)
        print('o valor somado é: ',s)
        tempo2 = time.time()
        tempo = tempo2 - tempo1
        print('o tempo é de: ', tempo)
s = fila()



s.full()
for i in range(1000000):
    s.push(i)

s.full()
s.tempo_calc()
