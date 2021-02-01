import random #biblioteca para gerar números aleatórios

'''
Função para verifica se um numero gerado é primo
'''
def prime(n): #verifica se o número é primo
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

'''
Função para gerar numeros primos aleatório respeitando as condições da função prime
'''
def generate_prime(): # gera o número primo - p e q
    while True: 
        x=random.randrange(1,100) # defini o intervalo dos números primos(inicio,para)
        if(prime(x)==True):
            return x

'''
Calcula o totiente do numero primo, retorna o  numero menos um
'''
def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False 

'''
Gera um numero aleatório E, satisfazendo as condições
'''
def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e
       

'''
Função modular entre dois números

'''
def mod(a,b):
    if(a<b):
        return a #retorna a
    else:
        c=a%b
        return c # retorna o resto da divisão 
  
'''
Cifra um texto
'''
def cifra(texto,e,n): # pega a frase digitada e o valor da chave publica e o valor do produto de n e calcula a cifragem
    tam = len(texto) #tamanho total da frase
    i = 0 #contador
    lista = [] # cria uma lista para armazenar a frase cifrada
    while(i < tam): # enquanto i for menor que o tamnho total da frase 
        letra = texto[i]  #letra vai ser igual na posição do contador
        k = ord(letra) #retorna o valor da tecla digitada referente a tabela unicode
        k = k**e # eleva  o valor de k ao valor referente a chave publica
        d = mod(k,n) #chama a função mod dando como parametro os valores de k e n
        lista.append(d)# adiciona na lista o valor de d
        i += 1 # aumenta o contador
    return lista # retorna lista

'''
Descriptografa um frase criptografada
'''
def descifra(cifra,n,d): # pega a frase cifrada e o valor da chave privada e o valor do produto de n e calcula a descriptografia
    lista = [] # cria uma lista para armazenar a frase descriptografada
    i = 0 # cria um contador
    tamanho = len(cifra) #pega o tamanho total da frase
    while i < tamanho: # enquanto i for menor que o tamnho total da frase
        result = cifra[i]**d # eleva o valor da cada posição da frase cript. pelo valor da chave privada
        texto = mod(result,n) #chama a função mod dando como parametro os valores de result e d
        letra = chr(texto) # armazena em letra o valor de texto convertendo para caracter 
        lista.append(letra) #adiciona em lista a  letra para formar a frase
        i += 1 # aumenta o contador
    return lista # retorna a lista no caso a frase  descriptografada

'''
Calcula a chave privada
'''
def calculate_private_key(toti,e): # para para calcular chave privada - recebe toti = (P-1)*(Q-1) e o valor da chave publica
    d = 0 # cria a variavel d 
    while(mod(d*e,toti)!=1): #enquanto mod(d*e,toti) for diferente de 1 
        d += 1 #adiciona mais 1 em d
    return d # retorna d que no caso será o valor da chave privada

# main
while (True):
    print('=-='*20)
    texto = input("Escreva uma frase: ")
    print('=-='*20)
    while len(texto) > 128:
        texto = input('Frase Inválida, Digite novamente: ')
    p = generate_prime() # gera random P
    q = generate_prime() # gera random Q
    n = p*q # calcula N
    y = totient(p) # calcula o  totient de P = (P-1)
    x = totient(q) # calcula o  totient de Q = (Q-1)
    totient_de_N = x*y # calcula o  totient de N =  (P-1)*(Q-1)
    e = generate_E(totient_de_N) # gera E
    public_key = (n, e)
    print('Sua chave pública:', public_key)
    text_cipher = cifra(texto,e,n)

    print('Sua mensagem criptografada:', ''.join(list(map(chr,text_cipher))))
    d = calculate_private_key(totient_de_N,e)

    print('Sua chave privada é:', d)
    print('=-='*20)
    try:
        decrip = input('Digite a mensagem criptografada: ')
        p = int(input("Digite sua chave privada: "))
        print('=-='*20)
    except:
        print(" ")
    while(p!=d and decrip != text_cipher):
        try:
            print('Mensagem criptografada e chave privada inválidas, digite novamente!!')
            decrip = input('Digite a mensagem criptografada: ')
            p = int(input("Digite a chave privada: "))
        except: 
            pass
    original_text = descifra(text_cipher,n,d)
    print('=-='*20)
    print('Sua mensagem original:', ''.join(original_text))





          