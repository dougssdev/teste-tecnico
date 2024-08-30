from time import sleep

def fibSequencia(limite): #CRiação da função que gera a sequência de fibonacci
    fibLista = [0, 1]
    while fibLista[-1] < limite:
        termo = fibLista[-1] + fibLista[-2]
        fibLista.append(termo)
    return fibLista

def estaNaLista (n): #verifica se o numero esta na lista
    fibLista = fibSequencia(n)
    if n in fibLista:
        print('O número {} pertence a sequencia de fibonacci.'.format(n))
    else:
        print('O número {} NÃO pertence a sequencia de fibonacci.'.format(n))

num = int(input('Digite um número:'))
print('CALCULANDO...')
sleep(3)
res = estaNaLista(num)

