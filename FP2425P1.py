# This is the Python script for your project

# 2.1.1 eh tabuleiro: universal → booleano 

def eh_tabuleiro(tab):
    '''Funcao recebe um tabuleiro (tab) e devolve True se o argumento corresponder a um tabuleiro
    e Falso caso contrario
    
    {universal} → {boleano}
    '''
    
    #Tab tem de ser um tuplo de tuplos com um tamanho entre 2 e 100 
    # Cada elemento de tab deve ter a mesma dimensao compreendida tambem entre 2 e 100
    return type(tab)==tuple and 2 <= len(tab) <= 100 and all(type(linha) == tuple and len(linha) == len(tab[0]) and\
             2 <= len(linha) <= 100 and all(type(elem) == int for elem in linha) for linha in tab)

# 2.1.2 eh posicao: universal → booleano 

def eh_posicao(arg):
    '''Funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma
    posicao do tabuleiro e False caso contrario
    
    {universal} → {boleano}
    '''

    #Uma posicao tem de ser um numero inteiro maior que zero e no maximo 100*100
    return type(arg) == int and 0 < arg <= 100*100

# 2.1.3 obtem dimensao: tabuleiro → tuplo

def obtem_dimensao(tab):
    '''Funcao recebe um tabuleiro e devolve um tuplo formado pelo numero de linha m e coluna n
    do tabuleiro
    
    {tuplo} → {tuplo}
    '''
    
    m = len(tab) # numero de linhas
    n = len(tab[0]) # numero de colunas

    return (m, n)

# 2.1.4 obtem valor: tabuleiro × posicao → inteiro 

def obtem_valor(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve o valor contido nessa posicao
    
    {tuplo} → {int}
    '''
    
    #Numero de colunas do tabuleiro
    n = len(tab[0])

    i = (pos-1)//n
    j = (pos-1)%n

    return tab[i][j]

# 2.1.5 obtem coluna: tabuleiro × posicao → tuplo 

def lista_posicoes(tab):
    '''Funcao recebe um tabuleiro e devolve a lista formada pelas posicoes do tabuleiro 
    
    {tuplo} → {lista} '''
    
    m = len(tab)
    n = len(tab[0])

    lista = [[j for j in range(i, i+n)] for i in range(1,m*n+1,n)]

    return lista

def obtem_coluna(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve um tuplo com todas as
    posicoes que formam a coluna a que pertence a posicao
    
    {tuplo, int} → {tuplo}
    '''
    
    n = len(tab[0])
    j_pos = (pos-1)%n #Descobre a coluna a que a posicao pertence

    posicoes_tabuleiro = lista_posicoes(tab)
    
    res = ()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if j == j_pos:
                res += (posicoes_tabuleiro[i][j],)
                
    return res

# 2.1.6 obtem linha: tabuleiro × posicao → tuplo 

def obtem_linha(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve um tuplo com todas as
    posicoes que formam a linha a que pertence a posicao
    
    {tuplo,int} → {tuplo}
    '''
    n = len(tab[0])

    i_pos = (pos-1)//n #Descobre a linha a que a posicao pertence
    posicoes_tabuleiro = lista_posicoes(tab)
    
    res = ()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if i == i_pos:
                res += (posicoes_tabuleiro[i][j],)
                
    return res

#2.1.7 obtem diagonais: tabuleiro × posicao → tuplo (minha versao)

def obtem_diagonais(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve um tuplo formado por dois 
    tuplos de posicoes correspondentes a diagonal (descendente da esquerda para a direita) 
    e antidiagonal (ascendente da esquerda para a direita) que passam pela posicao
    
    {tuplo,int} → {tuplo}
    '''

    m = len(tab)
    n = len(tab[0])
    linha = (pos - 1) // n
    coluna = (pos - 1) % n

    diagonal = ()
    antidiagonal = ()

    # Diagonal (descendente da esquerda para a direita)
    i = linha
    j = coluna
    while i >= 0 and j >= 0: #iniciando na posicao, inclusive, vamos percorrer as posicoes da diagonal da direita para a esquerda e adicionando ao tuplo diagonal
        diagonal = (i * n + j + 1,) + diagonal 
        i -= 1
        j -= 1
    i, j = linha + 1, coluna + 1
    while i < m and j < n:
        diagonal = diagonal + (i * n + j + 1,) # agora percorremos as posicoes da esquerda da direita
        i += 1
        j += 1

    # Antidiagonal (ascendente da esquerda para a direita)
    i, j = linha + 1, coluna - 1
    while i < m and j >= 0:  #iniciando na posicao, vamos percorrer as posicoes da antidiagonal da direita para a esquerda e adicionando ao tuplo diagonal
        antidiagonal = (i * n + j + 1,) + antidiagonal 
        i += 1
        j -= 1
    i, j = linha, coluna
    while i >= 0 and j < n:  # agora percorremos as posicoes, incluindo a nossa posicao inicial, da esquerda para a direita
        antidiagonal = antidiagonal + (i * n + j + 1,)  
        i -= 1
        j += 1
    
    return (diagonal,antidiagonal)

# 2.1.8 tabuleiro para str: tabuleiro → cad. carateres

def tabuleiro_para_str(tab):
    '''Funcao recebe um tabuleiro e devolve a cadeia de caracteres que o representa
    
    {tuplo} → {string}'''
    
    #Transforma o tabuleiro numa lista substituindo cada valor pelo seu caracter
    lista_caracteres = [[('X' if elemento == 1 else 'O' if elemento == -1 else '+') for elemento in linha] for linha in tab]

    # Lista que tera como elementos cada linha do tabuleiro, sendo cada linha representada por uma string
    linhas = []

    for i in range(len(lista_caracteres)):
        # Para cada linha da lista_caracteres, adiciona --- entre os seus elementos
        str_caracteres = '---'.join(lista_caracteres[i])
        linhas.append(str_caracteres)  # Adiciona a linha à lista linhas
        
        # Adiciona as barra vertical entre as linhas, mas não depois da última linha
        if i < len(lista_caracteres) - 1:  
            linhas.append('|   ' * (len(lista_caracteres[i])-1) + '|') 

    # Adiciona \n entre cada elemento da lista linhas
    return '\n'.join(linhas)

# 2.2.1 eh posicao valida: tabuleiro × posicao → booleano

def eh_posicao_valida(tab,pos):
    '''Funcao recebe um tabuleiro e uma posicao e devolve True se a posiçao corresponde a uma 
    posiçao do tabuleiro, e False caso contrario
    
    {tuplo,int} → {booleano}'''

    m = len(tab) #numero de linhas
    n = len(tab[0]) #numero de colunas

    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
    return 0 < pos <= (m*n)
    
# 2.2.2 eh posicao livre: tabuleiro × posicao → booleano

def eh_posicao_livre(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve True se a posição corresponde 
    a uma posição livre e False caso contrário
    
    {tuplo*int} → {boolean}
    '''

    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    
    return obtem_valor(tab, pos) == 0
    
# 2.2.3 obtem posicoes livres: tabuleiro → tuplo

def obtem_posicoes_livres(tab):
    '''Funcao recebe um tabuleiro e devolve o tuplo com todas as posições livres do tabuleiro ordenadas
    de menor a maior
    
    {tuplo} → {tuplo}
    '''
    
    #Verifica se tab é um argumento valido
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    
    #Percorre o tabuleiro adicionando as posicoes livres (0)
    posicoes_livres = ()
    pos = 1 
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 0:
                posicoes_livres += (pos,)
            pos += 1
            
    return posicoes_livres

# 2.2.4 obtem posicoes jogador: tabuleiro × inteiro → tuplo

def obtem_posicoes_jogador(tab, jog):
    '''Funcao recebe um tabuleiro e um inteiro que identifica o jogador e devolve o tuplo com todas as 
    posições do tabuleiro ocupadas por pedras do jogador
    
    {tuplo,int} → {tuplo}
    '''

    #Verifica se tab é um argumento valido e se o argumento jog é 1 ou -1
    if not eh_tabuleiro(tab) or jog not in (1, -1):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    
    #Percorre o tabuleiro adicionando a um novo tuplo as posicoes do jogador
    posicoes_jogador = ()
    pos = 1
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == jog:
                posicoes_jogador += (pos,)
            pos += 1
    
    return posicoes_jogador 


# 2.2.5 obtem posicoes adjacentes: tabuleiro × posicao → tuplo

def obtem_posicoes_adjacentes(tab, pos):
    '''Funcao recebe um tabuleiro e uma posicao do tabuleiro e devolve o tuplo formado pelas posicoes
    do tabuleiro adjacentes
    
    {tuplo,int} → {tuplo}
    '''

    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    
    lista_posicoes_tab = lista_posicoes(tab)
    for i in range(len(lista_posicoes_tab)):
        for j in range(len(lista_posicoes_tab[i])):
            if lista_posicoes_tab[i][j] == pos:
                nr_linha = i
                nr_coluna = j 

    posicoes_adjacentes = ()
    for i in range(len(lista_posicoes_tab)):
        for j in range(len(lista_posicoes_tab[i])):
            if i in range(nr_linha-1,nr_linha+2) and j in range(nr_coluna-1,nr_coluna+2) and lista_posicoes_tab[i][j] != pos:
                posicoes_adjacentes += (lista_posicoes_tab[i][j],)

    return posicoes_adjacentes

# 2.2.6 ordena posicoes tabuleiro: tabuleiro × tuplo → tuplo

def ordena_posicoes_tabuleiro(tab, tup):
    '''Funcao recebe um tabuleiro e um tuplo de posicoes do tabuleiro e devolve o tuplo com as posicoes em ordem
    ascendente de distancia à posicao central do tabuleiro
    
    {tuplo,tuplo} → {tuplo}
    '''
    
    if not eh_tabuleiro(tab) or type(tup) != tuple:
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    
    for pos in tup:
        if not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')

    m = len(tab)
    n = len(tab[0])

    #Determina a posicao do centro e o seu numero de linha e coluna
    c = (m//2)*n+n//2+1
    print(c)
    linha_c = ((c-1)//n) + 1
    coluna_c = ((c-1)%n) + 1
    
    dicionario_distancias = {}
    for pos in tup:
        linha = ((pos-1)//n) +1
        coluna = ((pos-1)%n) +1
        dist = max(abs(linha - linha_c), abs(coluna - coluna_c))
        if dist not in dicionario_distancias:
            dicionario_distancias[dist] = []
        dicionario_distancias[dist].append(pos)
    
    return tuple(posicao for dist in sorted(dicionario_distancias) for posicao in dicionario_distancias[dist])

#2.2.7 marca posicao: tabuleiro × posicao × inteiro → tabuleiro

def marca_posicao(tab, pos, jog):

    '''Funcao recebe um tabuleiro, uma posicaoo livre do tabuleiro e um inteiro identificando um jogador
    e devolve um novo tabuleiro com uma nova pedra do jogador indicado nessa posicao
    
    {tuplo,int,int} → {tuplo}
    '''
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos) or jog not in (1,-1) or not eh_posicao_livre(tab,pos):
        raise ValueError('marca_posicao: argumentos invalidos')
    
    n = len(tab[0])
    i_pos = (pos-1)//n
    j_pos = (pos-1)%n
    lista_tabuleiro = list(list(linha) for linha in tab)

    lista_tabuleiro[i_pos][j_pos] = jog

    return tuple(tuple(i) for i in lista_tabuleiro)

# 2.2.8 verifica k linhas: tabuleiro × posicao × inteiro × inteiro → booleano

def lista_linha_valores(tab,pos):
    '''Funcao recebe um tabuleiro e uma posicao e devolve a lista dos valores da linha a que a posicao pertence
    
    {tuplo,int} → {lista}
    '''
    n = len(tab[0])
    i = (pos-1)//n

    return list(tab[i])

def lista_coluna_valores(tab,pos):
    '''Funcao recebe um tabuleiro e uma posicao e devolve a lista dos valores da coluna a que a posicao pertence
    
    {tuplo,int} → {lista}
    '''
    colunas = obtem_coluna(tab, pos)
    n = len(tab[0]) 
    return [tab[(p-1)//n][(p-1)%n] for p in colunas]

def lista_diagonal_valores(tab,pos):
    '''Funcao recebe um tabuleiro e uma posicao e devolve a lista dos valores da diagonal a que a posicao pertence
    
    {tuplo,int} → {lista}
    '''
    diagonais = obtem_diagonais(tab, pos)  # Obtém as posições das diagonais
    n = len(tab[0]) 
    return [tab[(p-1)//n][(p-1)%n] for p in diagonais[0]]  # Valores da diagonal descendente como lista
    
def lista_antidiagonal_valores(tab,pos):
    '''Funcao recebe um tabuleiro e uma posicao e devolve a lista dos valores da antidiagonal a que a posicao pertence
    
    {tuplo,int} → {lista}
    '''
    diagonais = obtem_diagonais(tab, pos)  # Obtém as posições das diagonais
    n = len(tab[0]) 
    return [tab[(p-1)//n][(p-1)%n] for p in diagonais[1]] 

def verifica_k_linhas(tab, pos, jog, k):
    '''Funcao recebe um tabuleiro, uma posicao do tabuleiro, um valor inteiro identificando um jogador e um valor inteiro positivo k
    e devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal) que contenha a posicao com k ou mais pedras consecutivas 
    do jogador indicado , e False caso contrario.
    
    {tuplo,int,int,int} → {tuplo}
    '''
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos) or jog not in (1,-1) or type(k) != int or k<=0:
        raise ValueError('verifica_k_linhas: argumentos invalidos')

    valor_pos = obtem_valor(tab,pos)
    res = []
    if valor_pos == jog:
        linha = lista_linha_valores(tab,pos)
        contagem = 0
        for valor in linha:
            if valor == jog:
                contagem +=1
                if contagem >= k:
                    res += [True]
            else:
                contagem = 0 #reinicia a contagem se valor != jog
                
        coluna = lista_coluna_valores(tab,pos)
        contagem = 0
        for valor in coluna:
            if valor == jog:
                contagem +=1
                if contagem >= k:
                    res += [True]
            else:
                contagem = 0 #reinicia a contagem se valor != jog
                
        diagonal = lista_diagonal_valores(tab,pos)
        contagem = 0
        for valor in diagonal:
            if valor == jog:
                contagem +=1
                if contagem >= k:
                    res += [True]
            else:
                contagem = 0 #reinicia a contagem se valor != jog
                
        antidiagonal = lista_antidiagonal_valores(tab,pos)
        contagem = 0
        for valor in antidiagonal:
            if valor == jog:
                contagem +=1
                if contagem >= k:
                    res += [True]
            else:
                contagem = 0 #reinicia a contagem se valor != jog
    
    return any(res) == True

#2.3.1 eh fim jogo: tabuleiro × inteiro → booleano

def eh_fim_jogo(tab,k):
    '''A funcao recebe um tabuleiro e um valor inteiro positivo k e devolve 
    um booleano a indicar se o jogo terminou (True) ou nao (False)
    
    {tuplo,int} → {booleano}
    '''
    if not eh_tabuleiro(tab) or type(k) != int or k<=0:
        raise ValueError('eh_fim_jogo: argumentos invalidos')

    lista_valores = [valor for linha in tab for valor in linha]
    
    #Se nao houver posicoes livres, o jogo termina
    if all(lista_valores) != 0:
        return True
    
    #Verifica se existem posicoes livres ou se existem k pedras consecutivas, calculando para cada 
    # valor do tabuleiro a sua posicao e jogador correspondente
    m = len(tab)
    n = len(tab[0])
    for i in range(len(tab)):
        for j in range(n):
            pos = i * n + j + 1
            if tab[i][j] == 1:
                jog = 1
            elif tab[i][j] == -1:
                jog = -1
            else:
                continue 
            if verifica_k_linhas(tab,pos,jog,k):
                return True 
    
    if all(tab[i][j] != 0 for i in range(m) for j in range(n)): #se nao houver posicoes livres ou se houver k pedras consecutivas de um dos jogadores o jogo terminou (True)
        return True
    
    return False

#2.3.2 escolhe posicao manual: tabuleiro → posicao

def escolhe_posicao_manual(tab):
    '''Funcao recebe um tabuleiro e devolve uma posicao manualmente introduzida pelo jogador
    
    {tuplo} → {int}
    '''

    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    
    m = len(tab) # numero de linhas
    n = len(tab[0]) # numero de colunas

    #Funcao repete a mensagem ate o jogador introduzir uma posicao livre
    while True:
        input_pos = input('Turno do jogador. Escolha uma posicao livre: ')
        if not input_pos.isdigit(): #verifica se a posicao inserida pelo jogador é composta por digitos 
            raise ValueError('escolhe_posicao_manual: argumento invalido')
        if input_pos.isdigit():
            pos = int(input_pos)
        
        if 1 <= pos <= m*n: #verifica se a posicao esta dentro do intervalo do tabuleiro antes de verificar se esta livre 
            if eh_posicao_livre(tab,pos):
                return pos

#2.3.3 escolhe posicao auto: tabuleiro × inteiro × inteiro × cad. carateres → posicao

#Estrategia facil
def estrategia_facil(tab, jog):
    '''Funcao recebe um tabuleiro e um jogador e escolhe uma posicao de acordo com a estrategia facil
        
    {tuplo,int} → {int}
    '''

    posicoes_livres = obtem_posicoes_livres(tab)
    posicoes_livres_ordenadas = ordena_posicoes_tabuleiro(tab,posicoes_livres)
        
    for pos in posicoes_livres_ordenadas:
        posicoes_adjacentes = obtem_posicoes_adjacentes(tab, pos)
        for pos_adj in posicoes_adjacentes:
            if obtem_valor(tab, pos_adj) == jog:
                return pos

    # Se não encontrar adjacentes livres, joga em qualquer posição livre
    return posicoes_livres_ordenadas[0]

#Estrategia normal
def calcula_L(tab, jog):
    ''' Funcao recebe um tabuleiro e um jogador e conta o número máximo de peças consecutivas que o jogador pode formar ao jogar numa posição livre.
    
    {tuplo,int} → {int}
    '''
    max_pedras_consecutivas = 0
    
    # Tamanho do tabuleiro
    m = len(tab)
    n = len(tab[0]) 

    # Verifica linhas
    # Contamos as pedras consecutivas do jog à esquerda e à direita de cada posicao livre, percorrendo cada linha
    for linha in range(m):
        for coluna in range(n):
            if tab[linha][coluna] == 0: #percorremos a linha ate encontrarmos uma posicao vazia e partir dai inciamos a contagem (primeiro dos elemento à esquerda e depois à direita)
                contagem_esquerda = 0
                for c in range(coluna - 1, -1, -1):
                    if tab[linha][c] == jog:
                        contagem_esquerda += 1
                    else:
                        break #se encontrarmos uma posicao com um valor diferente do jogador entao paramos a contagem
                
                contagem_direita = 0
                for c in range(coluna + 1, n):
                    if tab[linha][c] == jog:
                        contagem_direita += 1
                    else:
                        break

                max_pedras_consecutivas = max(max_pedras_consecutivas, contagem_esquerda + contagem_direita + 1) #adiciona-se o +1 para contar a posicao vazia que sera preenchida pelo jogador uma vez que o L a inclui

    # Verifica colunas
    # Contamos as pedras consecutivas do jog acima e abaixo de cada posicao livre, percorrendo cada coluna, da mesma forma que fizemos anteriormente
    for coluna in range(n):
        for linha in range(m):
            if tab[linha][coluna] == 0:  
                contagem_cima = 0
                for l in range(linha - 1, -1, -1):
                    if tab[l][coluna] == jog:
                        contagem_cima += 1
                    else:
                        break
                
                contagem_baixo = 0
                for l in range(linha + 1, m):
                    if tab[l][coluna] == jog:
                        contagem_baixo += 1
                    else:
                        break

                max_pedras_consecutivas = max(max_pedras_consecutivas, contagem_cima + contagem_baixo + 1)

    # Verifica diagonais (descendente da esquerda para a direita)
    # Contamos as pedras consecutivas do jog à esquerda e à direita de cada posicao livre, percorrendo cada diagonal, da mesma forma que fizemos anteriormente 
    for i in range(m):
        for j in range(n):
            if tab[i][j] == 0: 
                contagem_diag_esq = 0
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    if tab[x][y] == jog:
                        contagem_diag_esq += 1
                    else:
                        break
                    x -= 1
                    y -= 1
                
                contagem_diag_dir = 0
                x, y = i + 1, j + 1
                while x < m and y < n:
                    if tab[x][y] == jog:
                        contagem_diag_dir += 1
                    else:
                        break
                    x += 1
                    y += 1

                max_pedras_consecutivas = max(max_pedras_consecutivas, contagem_diag_esq + contagem_diag_dir + 1)

    # Verifica antidiagonais (ascendente da esquerda para a direita)
    # Contamos as pedras consecutivas do jog à direita e à esquerda de cada posicao livre, percorrendo cada antidiagonal, da mesma forma que fizemos anteriormente
    for i in range(m):
        for j in range(n):
            if tab[i][j] == 0: 
                contagem_antidiag_esq = 0
                x, y = i - 1, j + 1
                while x >= 0 and y < n:
                    if tab[x][y] == jog:
                        contagem_antidiag_esq += 1
                    else:
                        break
                    x -= 1
                    y += 1
                
                contagem_antidiag_dir = 0
                x, y = i + 1, j - 1
                while x < m and y >= 0:
                    if tab[x][y] == jog:
                        contagem_antidiag_dir += 1
                    else:
                        break
                    x += 1
                    y -= 1

                max_pedras_consecutivas = max(max_pedras_consecutivas, contagem_antidiag_esq + contagem_antidiag_dir + 1)

    return max_pedras_consecutivas

def estrategia_normal(tab,jog,k):
    '''Funcao recebe um tabuleiro, um jogador e um k e escolhe uma posicao de acordo com a estrategia normal
        
    {tuplo,int,int} → {int}
    '''
    
    L_jog = calcula_L(tab,jog)
    L_adversario = calcula_L(tab,-jog)
    posicoes_livres = obtem_posicoes_livres(tab)
    posicoes_livres_ordenadas = ordena_posicoes_tabuleiro(tab,posicoes_livres)

    #Se o jogador tiver o maior L ou se ambos os L forem iguais, entao para cada posicao livre ordenada verificamos se o jogador faz L pedras consecutivas e se sim jogamos nessa posicao
    if L_jog >= L_adversario:
        k = L_jog
        for pos in posicoes_livres_ordenadas:
            mudou_posicao = marca_posicao(tab,pos,jog)
            tab1 = mudou_posicao
            if verifica_k_linhas(tab1, pos, jog, k):
                tab = tab
                return pos
    
    #Se o adversario tiver o maior L, entao para cada posicao livre ordenada verificamos se o adversario faz L pedras consecutivas e se sim jogamos nessa posicao
    if L_jog < L_adversario:
        k = L_adversario
        for pos in posicoes_livres_ordenadas:
            mudou_posicao = marca_posicao(tab,pos,-jog)
            tab1 = mudou_posicao
            if verifica_k_linhas(tab1, pos, -jog, k):
                tab = tab
                return pos

#Estrategia dificil
def jogo_simulado(tab,pos,jog,k):
    '''Funcao recebe um tabuleiro, uma posicao, um jogador e devolve qual o jogador vencedor depois de simular um jogo 
    em que ambos os jogadores jogam de acordo com a estrategia normal
    
    {tuplo,int,int,int} → {int}
    '''
    
    tab1 = marca_posicao(tab,pos,jog) #primeiro joga o jogador jog na pos
    proximo_jogador = -jog

    while not eh_fim_jogo(tab1,k):
        proxima_posicao = estrategia_normal(tab1,proximo_jogador,k)
        tab1 = marca_posicao(tab1,proxima_posicao,proximo_jogador)
        
        if eh_fim_jogo(tab1,k):
            if verifica_k_linhas(tab1, proxima_posicao, proximo_jogador, k):
                vencedor = proximo_jogador
            else:
                vencedor = 0
        
        proximo_jogador = - proximo_jogador
    
    return vencedor

def estrategia_dificil(tab,jog,k):
    '''Funcao recebe um tabuleiro, um jogador e um k e escolhe uma posicao de acordo com a estrategia dificil
        
    {tuplo,int,int} → {int}
    '''
    posicoes_livres = obtem_posicoes_livres(tab)
    posicoes_livres_ordenadas = ordena_posicoes_tabuleiro(tab,posicoes_livres)
    
    #Verifica se existe uma posicao que permita obter uma linha propria com k pedras consecutivas
    for pos in posicoes_livres_ordenadas:
        tab1 = marca_posicao(tab,pos,jog)
        if verifica_k_linhas(tab1,pos,jog,k):
            return pos
    
    #Verifica se existe uma posicao que impossibilita o adversario de obter uma linha com k pedras consecutivas
    for pos in posicoes_livres_ordenadas:
        tab1 = marca_posicao(tab,pos,-jog)
        if verifica_k_linhas(tab1,pos,-jog,k):
            return pos
    
    #Verifica para todas as posicoes livres, simulando um jogo ate ao fim, se o jogador ganharia o jogo jogando nessa posicao
    for pos in posicoes_livres_ordenadas:
        vencedor = jogo_simulado(tab,pos,jog,k)
        if vencedor == jog:
            return pos
    
    #Verifica para todas as posicoes livres, simulando um jogo ate ao fim, se o jogador empataria o jogo jogando nessa posicao
    for pos in posicoes_livres_ordenadas:
        vencedor = jogo_simulado(tab,pos,jog,k)
        if vencedor == 0:
            return pos
    
    #Verifica para todas as posicoes livres, simulando um jogo ate ao fim, se o jogador perderia o jogo jogando nessa posicao
    for pos in posicoes_livres_ordenadas:
        vencedor = jogo_simulado(tab,pos,jog,k)
        if vencedor == -jog:
            return pos
        
def escolhe_posicao_auto(tab, jog, k, lvl):
    '''Funcao recebe um tabuleiro, um inteiro identificando um jogador, um inteiro positivo correspondendo ao valor k e a cadeia de caracteres correspondente à
    estrategia e devolve a posicao escolhida automaticamente de acordo com a estrategia selecionada.
        
    {tuplo,int,int,str} → {int}
    '''
    if not eh_tabuleiro or jog not in (1,-1) or type(k) != int or k<=0 or type(lvl) != str or lvl not in ('facil','normal','dificil'):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos') 

    if lvl == 'facil':
        return estrategia_facil(tab,jog)
    
    if lvl == 'normal':
        return estrategia_normal(tab,jog,k)
    
    if lvl == 'dificil':
        return estrategia_dificil(tab,jog,k)
    
def jogo_mnk(cfg,jog,lvl):
    '''Funcao recebe a configuracao do jogo, um jogador e uma estrategia de jogo e permite jogar um jogo completo
    devolvendo o resultado do jogo (quem foi o vencedor ou empate)
    
    {tuple,int,str} → {int}'''

    if type(cfg) != tuple or len(cfg) != 3 or any(type(elem) != int for elem in cfg) or jog not in (1,-1) or lvl not in ('facil','normal','dificil'):
        raise ValueError('jogo_mnk: argumentos invalidos')
    
    print('Bem-vindo ao JOGO MNK.')

    if jog == 1:
        print("O jogador joga com 'X'.")
    if jog == -1:
        print("O jogador joga com 'O'.")
    
    lista_tab = [[0 for x in range(cfg[1])] for x in range(cfg[0])]
    tab = tuple(tuple(linha) for linha in lista_tab)
    m = cfg[0]
    n = cfg[1]
    k = cfg[2]

    #Inicializa o tabuleiro
    print(tabuleiro_para_str(tab))

    if jog == -1: #se o jogador jogar com as pedras brancas entao quem joga primeiro é o computador
        print("Turno do computador (" + lvl + "):")
        pos = escolhe_posicao_auto(tab, 1, k, lvl)  
        tab = marca_posicao(tab, pos, 1)  
        print(tabuleiro_para_str(tab))  
    
    while True:
        pos = escolhe_posicao_manual(tab)
        tab = marca_posicao(tab,pos,jog)
        print(tabuleiro_para_str(tab))

        if verifica_k_linhas(tab,pos,jog,k):
            print("VITORIA")
            return jog
        
        if all(tab[i][j] != 0 for i in range(m) for j in range(n)):
            print("EMPATE")
            return 0

        print("Turno do computador (" + lvl + "):")
        pos = escolhe_posicao_auto(tab,-jog,k,lvl)
        tab = marca_posicao(tab,pos,-jog)
        print(tabuleiro_para_str(tab))

        if verifica_k_linhas(tab,pos,-jog,k):
            print('DERROTA')
            return -jog

print(jogo_mnk((3,3,3), 1, 'dificil'))