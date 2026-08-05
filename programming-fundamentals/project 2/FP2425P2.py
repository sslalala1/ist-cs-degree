# This is the Python script for your project

#2.1.1 TAD posicao

#Construtor

def cria_posicao(col,lin):
    '''Funcao recebe uma coluna e uma linha e devolve a posicao na forma de um tuplo em que o primeiro elemento é a coluna e o segundo é a linha
    
    {str,int} → {posicao}
    '''
    if not type(col) == str or not type(lin) == int or col not in 'abcdefghij' or lin > 10 or lin < 1:
        raise ValueError('cria_posicao: argumentos invalidos')
    else:
        return (col,lin)

#Seletores

def obtem_pos_col(pos):
    '''Funcao recebe uma posicao e devolve a coluna
    
    {posicao} → {str}
    '''
    return pos[0]

def obtem_pos_lin(pos):
    '''Funcao recebe uma posicao e devolve a linha
    
    {posicao} → {int}
    '''
    return pos[1]

#Reconhecedor

def eh_posicao(arg):
    '''Funcao recebe um argumento e devolve True se o argumento corresponder a uma posicao ou False se nao 
    
    {universal} → {boleano}
    '''
    return (type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and arg[0] in 'abcdefghij' and type(arg[1]) == int and arg[1] <11 and arg[1] > 0)

#Teste

def posicoes_iguais(pos1,pos2):
    '''Funcao recebe duas posicoes e devolve True se ambas forem posicoes e se forem iguais
    
    {universal,universal} → {boleano}
    '''
    return eh_posicao(pos1) and eh_posicao(pos2) and pos1 == pos2

#Transformador

def posicao_para_str(pos):
    '''Funcao recebe uma posicao e devolve a cadeia de carateres que representa a posicao
    
    {posicao} → {str}
    '''
    return pos[0] + str(pos[1])

def str_para_posicao(pos_str):
    '''Funcao recebe uma cadeia de carateres e devolve a posicao por ela representada

    {str} → {posicao}    
    '''
    if len(pos_str) <=3 and len(pos_str) > 0 and pos_str[0] in 'abcdefghij' and pos_str[1] in ('1','2','3','4','5','6','7','8','9','10'):
        return (pos_str[0], int(pos_str[1:]))
    
    return None

#Funcoes de alto nivel

def eh_posicao_valida(pos,n):
    '''Funcao recebe uma posicao e um numero de orbitas e devolve True se a posicao for uma posicao valida dentro do tabuleiro e False caso contrario
    
    {posicao,int} → {boleano}
    '''
    nr_colunas = 2*n
    ultima_coluna = chr(ord('a') + nr_colunas - 1)
    nr_linhas = 2*n

    coluna = obtem_pos_col(pos)
    linha = obtem_pos_lin(pos)

    return eh_posicao(pos) and coluna <= ultima_coluna and linha <= nr_linhas

def posicoes_tabuleiro(n):
    '''Cria um tabuleiro de Orbito-n representado por uma lista em que cada sublista corresponde a uma linha
    
    {int} → {lista}
    '''
    tabuleiro = []
    for lin in range(2 * n):
        linha = []
        for col in range(2 * n):
            coluna_str = chr(col + ord('a'))  
            linha_str = str(lin + 1)            
            linha.append(coluna_str + linha_str)  
        tabuleiro.append(linha)  
    return tabuleiro

def obtem_posicoes_adjacentes(pos,n,d):
    '''Funcao devolve um tuplo com as posicoes do tabuleiro adjacentes à posicao p se d for True, ou as posicoes adjacentes ortogonais se d for False.
    
    {posicao,int,boleano} → {tuplo}
    '''
    index_linha = int(obtem_pos_lin(pos)) - 1  #Converte a linha da posição para um indice entre 0 e 2*n-1
    index_coluna = ord(obtem_pos_col(pos)) - ord('a')  #Converte a coluna da posição um indice entre 0 e 2*n-1

    tabuleiro = posicoes_tabuleiro(n)

    posicoes_adjacentes = ()

    if d:
        #Adiciona primeiro a posicao de cima 
        if index_linha - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha - 1][index_coluna],)
        #Adiciona a posicao superior da antidiagonal
        if index_linha - 1 >= 0 and index_coluna + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha - 1][index_coluna + 1],)
        #Adicioina a posicao da direita
        if index_coluna + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha][index_coluna + 1],)
        #Adiciona a posicao inferior da diagonal 
        if index_linha + 1 < 2 * n and index_coluna + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha + 1][index_coluna + 1],)
        #Adiciona a posicao abaixo
        if index_linha + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha + 1][index_coluna],)
        #Adiciona a posicao inferior da antidiagonal
        if index_linha + 1 < 2 * n and index_coluna - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha + 1][index_coluna - 1],)
        #Adiciona a posicao da esquerda
        if index_coluna - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha][index_coluna - 1],)
        #Adiciona a posicao superior da diagonal 
        if index_linha - 1 >= 0 and index_coluna - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha - 1][index_coluna - 1],)
    else:
        #Adiciona apenas as posições ortogonais
        #Posicao de cima
        if index_linha - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha - 1][index_coluna],)
        #Posicao à direita
        if index_coluna + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha][index_coluna + 1],)
        #Posicao abaixo
        if index_linha + 1 < 2 * n:
            posicoes_adjacentes += (tabuleiro[index_linha + 1][index_coluna],)
        #Posicao à esquerda
        if index_coluna - 1 >= 0:
            posicoes_adjacentes += (tabuleiro[index_linha][index_coluna - 1],)
    
    return posicoes_adjacentes

def obtem_orbita(pos,n):
    '''Funcao recebe uma posicao e o numero de orbitas e devolve a orbita a que essa posicao pertence
    
    {tuplo,int} → {int}
    '''
    linha = int(obtem_pos_lin(pos))
    coluna = ord(obtem_pos_col(pos)) - ord('a') + 1

    #A orbita pode ser calculada atraves do modulo da subtracao entre a distancia minima da posicao às bordas do tabuleiro e o numero de orbitas do tabuleiro
    distancia_borda_superior = linha-1  #Distancia ate a borda superior
    distancia_borda_inferior = 2*n - linha  #Distancia ate a borda inferior
    distancia_borda_esquerda = coluna-1  #Distancia ate a borda esquerda
    distancia_borda_direita = 2*n - coluna  #Distancia ate a borda direita

    dist_minima = min(distancia_borda_superior, distancia_borda_inferior, distancia_borda_esquerda, distancia_borda_direita)

    return abs(dist_minima - n)

def ordena_posicoes(posicoes,n):
    '''Funcao recebe um tuplo com posicoes e o numero de orbitas do tabuleiro e devolve o tuplo das posicoes com as posicoes ordenadas

    {tuplo,int} → {tuplo}
    '''
    dicionario_orbitas = {}
    for pos in posicoes:
        orbita = obtem_orbita(pos,n)
        if orbita not in dicionario_orbitas:
            dicionario_orbitas[orbita] = []
        dicionario_orbitas[orbita].append(pos)
    
    #Transforma cada posicao num tuplo em que o primeiro elemento é a linha e o segundo a coluna e depois ordena primeiro segundo as linhas e depois segundo as colunas
    for orbita in dicionario_orbitas:
        dicionario_orbitas[orbita].sort(key=lambda pos: (int(obtem_pos_lin(pos)), obtem_pos_col(pos))) 

    #Ordena o dicionario segundo as orbitas 
    dicionario_ordenado = {}
    orbitas_ordenadas = sorted(dicionario_orbitas)
    for orbita in orbitas_ordenadas:
        dicionario_ordenado[orbita] = dicionario_orbitas[orbita]
    
    #Transforma o dicionario numa lista so com as posicoes ordenadas segundo a orbita
    posicoes_ordenadas = []
    for orbita in orbitas_ordenadas:
        for pos in dicionario_ordenado[orbita]:  # Adiciona cada posição da órbita à lista
            posicoes_ordenadas.append(pos)

    return tuple(posicoes_ordenadas) 
    

#2.1.2 TAD pedra

#Construtores

def cria_pedra_branca():
    '''Funcao devolve uma pedra pertencente ao jogador branco 
    
    {} → {pedra}
    '''
    return -1

def cria_pedra_preta():
    '''Funcao devolve uma pedra pertencente ao jogador preto 
    
    {} → {pedra}
    '''
    return 1

def cria_pedra_neutra():
    '''Funcao devolve uma pedra neutra 
    
    {} → {pedra}
    '''
    return 0

#Reconhecedores

def eh_pedra(arg):
    '''Funcao devolve True se o argumento for um TAD pedra e False caso contrario
    
    {universal} → {boleano}
    '''
    return arg == cria_pedra_branca() or arg == cria_pedra_preta() or arg == cria_pedra_neutra()

def eh_pedra_branca(p):
    '''Funcao devolve True se a pedra p pertencer ao jogador branco e False caso contrario
    
    {pedra} → {boleano}
    '''
    return p == cria_pedra_branca()

def eh_pedra_preta(p):
    '''Funcao devolve True se a pedra p pertencer ao jogador preto e False caso contrario
    
    {pedra} → {boleano}
    '''
    return p == cria_pedra_preta()

#Testes

def pedras_iguais(p1,p2):
    '''Funcao devolve True apenas se p1 e p2 forem pedras e se forem iguais
    
    {p1,p2} → {boleano}
    '''
    if eh_pedra(p1) and eh_pedra(p2):
        return p1 == p2

#Transformador

def pedra_para_str(p):
    '''Funcao devolve a cadeia de caracteres que representa o jogador dono da pedra, isto  é, 'O', 'X' ou ' ' para pedras do jogador branco, preto ou neutra respetivamente.
    
    {pedra} → {str}
    '''
    
    if eh_pedra_preta(p):
        return 'X'
    elif eh_pedra_branca(p):
        return 'O'
    else: 
        return ' '
    

#Funcoes alto nivel

def eh_pedra_jogador(p):
    '''Funcao devolve True caso a pedra p seja de um jogador e False caso contrario.
    
    {pedra} → {boleano}
    '''
    return eh_pedra_branca(p) or eh_pedra_preta(p)

def pedra_para_int(p):
    '''Funcao devolve um inteiro valor 1, -1 ou 0, dependendo se a pedra é do jogador preto, branco ou neutra, respetivamente.
    
    {pedra} → {int}
    '''
    if eh_pedra_preta(p):
        return 1
    elif eh_pedra_branca(p):
        return -1
    else:
        return 0

def str_para_pedra(str):
    '''Funcao devolve a pedra correspondete a cadeia de caracteres que representa o jogador dono da pedra ('O', 'X' ou ' ')
    
    {str} → {pedra}
    '''

    if str == 'X':
        return 1
    if str == 'O':
        return -1
    if str == ' ':
        return 0

#2.1.3 TAD tabuleiro

#Construtores

def cria_tabuleiro_vazio(n):
    '''Funcao recebe um numero de orbitas e devolve um tabuleiro de Orbito com n orbitas, sem posicoes ocupadas
    
    {int} → {tabuleiro}
    '''
    if type(n) != int or n<2 or n>5:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    
    tabuleiro = []
    for i in range(2 * n):
        linha = []
        for j in range(2 * n):
            linha.append(0) 
        tabuleiro.append(linha)
    
    return tabuleiro

def cria_tabuleiro(n,tp,tb):
    '''Funcao devolve um tabuleiro com n orbitas, com as posicoes do tuplo tp ocupadas por pedras pretas e as posicoes do tuplo tb ocupadas por pedras brancas
    
    {int,tuplo,tuplo} → {tabuleiro}
    '''
    if type(n) != int or n<2 or n>5 or type(tp) != tuple or type(tb) != tuple:
        raise ValueError('cria_tabuleiro: argumentos invalidos')

    for pos in tp:
        if not eh_posicao(pos) or not eh_posicao_valida(pos,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        if pos in tb:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

    for pos in tb:
        if not eh_posicao(pos) or not eh_posicao_valida(pos,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos') 
    
    tabuleiro = cria_tabuleiro_vazio(n)
    #Colocamos as pedras pretas nas posições de tp
    for pos in tp:
        index_linha = obtem_pos_lin(pos) - 1
        index_coluna = ord(obtem_pos_col(pos)) - ord('a')
        tabuleiro[index_linha][index_coluna] = 1  

    #Colocamos as pedras brancas nas posições de tb
    for pos in tb:
        index_linha = obtem_pos_lin(pos) - 1
        index_coluna = ord(obtem_pos_col(pos)) - ord('a')
        tabuleiro[index_linha][index_coluna] = -1  

    return tabuleiro

def cria_copia_tabuleiro(t):
    '''Funcao recebe um tabuleiro e devolve uma copia do tabuleiro
    
    {tabuleiro} → {tabuleiro}
    '''
    copia_tabuleiro = []
    for linha in t:
        copia_linha = []  #Cria uma nova lista para a linha copiada
        for elemento in linha:
            copia_linha.append(elemento)  #Adiciona cada elemento da linha original
        copia_tabuleiro.append(copia_linha)  #Adiciona a linha copiada ao novo tabuleiro
    
    return copia_tabuleiro

#Seletores

def obtem_numero_orbitas(t):
    '''Funcao recebe um tabuleiro e devolve o numero de orbitas do tabuleiro t
    
    {tabuleiro} → {int}
    '''
    return len(t)//2

def obtem_pedra(t,pos):
    '''Funcao devolve a pedra na posicao pos do tabuleiro t. Se a posicao nao estiver ocupada, devolve uma pedra neutra.
    
    {tabuleiro,posicao} → {pedra}
    '''
    #Obtemos o indice da linha e coluna de pos para que possamos ir ao tabuleiro identifica-la e devolver a pedra
    index_linha = obtem_pos_lin(pos) - 1
    index_coluna = ord(obtem_pos_col(pos)) - ord('a')

    return t[index_linha][index_coluna]

def obtem_linha_horizontal(t,pos):
    '''Funcao devolve o tuplo formado por tuplos de dois elementos correspondentes à posicao e o valor de todas as posicoes da linha horizontal 
    que passa pela posicao pos, ordenadas de esquerda para a direita.
    
    {tabuleiro,posicao} → {tuplo}
    '''
    
    index_linha = obtem_pos_lin(pos) - 1
    n = obtem_numero_orbitas(t)
    nr_colunas = 2*n
    linha_horizontal = ()

    for coluna in range(nr_colunas):
        posicao = cria_posicao(chr(ord('a') + coluna), obtem_pos_lin(pos))
        valor = t[index_linha][coluna]
        linha_horizontal += ((posicao,valor),)

    return linha_horizontal

def obtem_linha_vertical(t,pos):
    '''Funcao devolve o tuplo formado por tuplos de dois elementos correspondentes à posicao e o valor de todas as posicoes da linha vertical 
    que passa pela posicao pos, ordenadas de cima para baixo
    
    {tabuleiro,posicao} → {tuplo}
    '''

    index_coluna = ord(obtem_pos_col(pos)) - ord('a')
    nr_linhas = len(t)

    coluna = ()
    for i in range(nr_linhas):
        posicao = cria_posicao(obtem_pos_col(pos),i+1)
        valor = t[i][index_coluna]
        coluna += ((posicao,valor),)

    return coluna

def obtem_linhas_diagonais(t, pos):
    '''Funcao devolve dois tuplos formados cada um deles por tuplos de dois elementos correspondentes à posicao e o valor de todas as posicoes que 
    formam a diagonal (descendente da esquerda para a direita) e antidiagonal (ascendente da esquerda para a direita) que passam pela posicao pos, respetivamente.
    
    {tabuleiro, posicao} → {tuplo}
    '''

    n = obtem_numero_orbitas(t)
    nr_linha = obtem_pos_lin(pos) - 1  #Ajustar para um índice que vai de 0 a 2*n-1
    nr_coluna = ord(obtem_pos_col(pos)) - ord('a')  #Ajustar para um índice que vai de 0 a 2*n-1

    diagonal = ()
    antidiagonal = ()

    #Diagonal (descendente da esquerda para a direita)
    linha = nr_linha
    coluna = nr_coluna
    while linha >= 0 and coluna >= 0:  
        pos_atual = cria_posicao(chr(coluna + ord('a')), linha + 1) 
        diagonal = ((pos_atual,obtem_pedra(t, pos_atual)),) + diagonal
        linha -= 1
        coluna -= 1
    
    linha = nr_linha + 1
    coluna = nr_coluna + 1
    while linha < (2 * n) and coluna < (2 * n):  
        pos_atual = cria_posicao(chr(coluna + ord('a')), linha + 1) 
        diagonal = diagonal + ((pos_atual,obtem_pedra(t, pos_atual)),)
        linha += 1
        coluna += 1
    
    #Antidiagonal (ascendente da esquerda para a direita)
    linha = nr_linha
    coluna = nr_coluna
    while linha < (2 * n) and coluna >= 0:  
        pos_atual = cria_posicao(chr(coluna + ord('a')), linha + 1)  
        antidiagonal = ((pos_atual,obtem_pedra(t, pos_atual)),) + antidiagonal
        linha += 1
        coluna -= 1
    
    linha = nr_linha - 1
    coluna = nr_coluna + 1
    while linha >= 0 and coluna < (2 * n):  
        pos_atual = cria_posicao(chr(coluna + ord('a')), linha + 1)  
        antidiagonal = antidiagonal + ((pos_atual,obtem_pedra(t, pos_atual)),)
        linha -= 1
        coluna += 1
    
    return diagonal,antidiagonal

def obtem_posicoes_pedra(t,j):
    '''Funcao devolve o tuplo formado por todas as posicoes do tabuleiro ocupadas por pedras j (brancas, pretas ou neutras), 
    ordenadas em ordem de leitura do tabuleiro.
    
    {tabuleiro, pedra} → {tuplo}
    '''
    n = obtem_numero_orbitas(t)
    
    posicoes = ()
    for linha in range(len(t)):
        for coluna in range(len(t[linha])):
            if j == t[linha][coluna]:
                pos = cria_posicao(chr(coluna + ord('a')), linha + 1)  
                posicoes += (pos,)

    posicoes_ordenadas = ordena_posicoes(posicoes,n)

    return posicoes_ordenadas

#Modificadores

def coloca_pedra(t,pos,p):
    '''Funcao modifica destrutivamente o tabuleiro t colocando a pedra j na posicao pos, e devolve o proprio tabuleiro.
    
    {tabuleiro, posicao, pedra} → {tabuleiro}
    '''

    linha = obtem_pos_lin(pos) - 1
    coluna = ord(obtem_pos_col(pos)) - ord('a')

    t[linha][coluna] = p

    return t

def remove_pedra(t,pos):
    '''Funcao modifica destrutivamente o tabuleiro t removendo a pedra da posicao pos, e devolve o proprio tabuleiro.
    
    {tabuleiro, posicao} → {tabuleiro}
    '''
    linha = obtem_pos_lin(pos) - 1
    coluna = ord(obtem_pos_col(pos)) - ord('a')

    t[linha][coluna] = 0

    return t

#Reconhecedor

def eh_tabuleiro(arg):
    '''Funcao devolve True caso o seu argumento seja um TAD tabuleiro e False caso contrario.
    
    {universal} → {booleano}
    '''
    if type(arg) != list or len(arg) not in (4,6,8,10):
        return False

    for linha in arg:
        if type(linha) != list or len(linha) < 4 or len(linha) > 10:
            return False
        for elem in linha:
            if elem not in [1,-1,0]:
                return False
    return True


#Teste

def tabuleiros_iguais(t1,t2):
    '''Funcao devolve True apenas se t1 e t2 forem tabuleiros e se forem iguais
    
    {t1,t2} → {boleano}
    '''
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        return t1 == t2

#Transformador

def tabuleiro_para_str(t):
    '''Funcao recebe um tabuleiro e devolve a cadeia de caracteres que o representa
    
    {tabuleiro} → {string}'''
    
    #Transforma o tabuleiro numa lista substituindo cada valor pelo seu caracter
    lista_caracteres = [[('[X]' if elemento == 1 else '[O]' if elemento == -1 else '[ ]') for elemento in linha] for linha in t]

    #Lista que tera como elementos cada linha do tabuleiro, sendo cada linha representada por uma string
    linhas = []

    #Cria a primeira linha que corresponde às letras que identificam cada coluna
    letras_coluna = [chr(ord('a') + i) for i in range(len(t[0]))]
    letras_coluna = '    ' + '   '.join(letras_coluna)
    linhas.append(letras_coluna)

    for i in range(len(lista_caracteres)):
        #Para cada linha da lista_caracteres, adiciona - entre os seus elementos e o numero correspondente à linha no inicio de cada linha
        str_caracteres = '-'.join(lista_caracteres[i])
        if i+1 < 10:
            num_linha = '0' + str(i+1) + ' '
        else:
            num_linha = str(i + 1) + ' '
        linhas.append(num_linha + str_caracteres)  
        
        #Adiciona as barra vertical entre as linhas
        if i < len(lista_caracteres) - 1:  
            linhas.append('   ' + ' |  ' * (len(lista_caracteres[i])-1) + ' |') 

    #Adiciona \n entre cada elemento da lista linhas
    return '\n'.join(linhas)


#Funcoes de alto nivel

def move_pedra(t,pos1,pos2):
    '''Funcao modifica destrutivamente o tabuleiro t movendo a pedra da posicao pos1 para a posicao pos2, 
    e devolve o proprio tabuleiro.
    
    {tabuleiro,posicao,posicao} → {tabuleiro}'''

    p1 = obtem_pedra(t,pos1)
    t = remove_pedra(t,pos1)
    t = coloca_pedra(t,pos2,p1)

    return t

def obtem_posicao_seguinte(t,pos,s):
    '''Funcao devolve a posicao da mesma orbita em que pos que se encontra a seguir no tabuleiro t 
    em sentido horario se s for True ou anti-horario se for False.
    
    {tabuleiro,posicao,booleano} → {posicao}
    '''

    linha = obtem_pos_lin(pos) -1
    coluna = ord(obtem_pos_col(pos)) - ord('a')
    n = obtem_numero_orbitas(t)
    orbita = obtem_orbita(pos,n) 

    #Determinamos os indices maximos e minimos que as linhas e colunas podem tomar dentro de cada orbita
    max = n + orbita - 1
    min = n - orbita
    
    if s == True:
        if linha == min and coluna < max:
            coluna += 1
        elif linha < max and coluna == max:
            linha += 1
        elif linha == max and coluna > min:
            coluna -= 1
        elif linha > min and coluna == min:
            linha -= 1
        
    if s == False:
        if linha == min and coluna > min:
            coluna -= 1
        elif linha < max and coluna == min:
            linha += 1
        elif linha == max and coluna < max:
            coluna += 1
        elif linha > min and coluna == max:
            linha -= 1
       
    coluna = chr(coluna + ord('a'))
    linha = linha + 1
    return cria_posicao(coluna,linha)

def roda_tabuleiro(t):
    '''Funcao modifica destrutivamente o tabuleiro t rodando todas as pedras uma posicao em sentido anti-horario, e devolve o proprio tabuleiro.
    
    {tabuleiro} → {tabuleiro}'''

    posicoes_pedras = obtem_posicoes_pedra(t, 1) + obtem_posicoes_pedra(t, -1)
    
    novas_posicoes = []
    
    #Primeiro, armazenamos todas as movimentações para cada pedra sem modificar o tabuleiro
    i = 0
    while i < len(posicoes_pedras):
        pos = posicoes_pedras[i]
        new_pos = obtem_posicao_seguinte(t, pos, False)
        pedra = obtem_pedra(t,pos)
        novas_posicoes.append((new_pos, pedra))
        i += 1
    
    #Removemos todas as pedras das posições originais
    for pos in posicoes_pedras:
        t = remove_pedra(t, pos)
    
    #Colocamos as pedras nas novas posições
    for new_pos, pedra in novas_posicoes:
        t = coloca_pedra(t, new_pos, pedra)
    
    return t

def verifica_linha_pedras(t,pos,j,k):
    '''Funcao devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal) que contenha a posicao pos com k ou mais pedras consecutivas do jogador com pedras j, e False caso contrario.
    
    {tabuleiro,posicao,pedra,int} → {booleano}'''

    pedra_pos = obtem_pedra(t,pos)
    if pedra_pos != j:
        return False

    res = []
    
    #Em cada linha vamos contando as posicoes que tem a pedra do jogador mas reiniciamos a contagem se encontrarmos uma posicao cuja pedra nao é a do jogador
    contagem = 0
    linha = obtem_linha_horizontal(t,pos)
    for elem in linha:
        if elem[1] == j:
            contagem += 1
            if contagem >= k:
                res += [True]
        else:
            contagem = 0
                
    coluna = obtem_linha_vertical(t,pos)
    contagem = 0
    for elem in coluna:
        if elem[1] == j:
            contagem +=1
            if contagem >= k:
                res += [True]
        else:
            contagem = 0 
                
    diagonais = obtem_linhas_diagonais(t,pos)
    contagem = 0
    for elem in diagonais[0]:
        if elem[1] == j:
            contagem +=1
            if contagem >= k:
                res += [True]
        else:
            contagem = 0
    
    contagem = 0
    for elem in diagonais[1]:
        if elem[1] == j:
            contagem +=1
            if contagem >= k:
                res += [True]
        else:
            contagem = 0 
    
    #Se em alguma das linhas encontrarmos k pedras consecutivas, a funcao devolve true
    return any(res) == True

#2.2 Funcoes adicionais
#2.2.1 eh vencedor

def eh_vencedor(t, j):
    '''Funcao recebe um tabuleiro e uma pedra de jogador, e devolve True se existe uma linha completa do tabuleiro de pedras do jogador ou False caso contrario.
    
    {tabuleiro,jogador} → {booleano}'''
    
    n = obtem_numero_orbitas(t)
    k = 2*n
    
    for linha in range(2 * n):  
        for coluna in range(2 * n):  
            pos = cria_posicao(chr(coluna + ord('a')), linha + 1) 
            if verifica_linha_pedras(t, pos, j, k):
                return True
    return False

def eh_fim_jogo(t):
    '''Funcao recebe um tabuleiro e devolve True se o jogo ja  terminou ou False caso contrario.
    
    {tabuleiro} → {booleano}'''

    #Se não existirem posições livres, o jogo terminou
    posicoes_livres = obtem_posicoes_pedra(t,0)
    if len(posicoes_livres) == 0:
        return True
    
    #Verifica se há um vencedor
    for j in [1, -1]:  
        if eh_vencedor(t, j):
            return True  #Se algum jogador ganhou, o jogo terminou
    
    return False 

#2.2.3 escolhe movimento manual

def escolhe_movimento_manual(t):
    '''Funcao recebe um tabuleiro t e permite escolher uma posicao livre do tabuleiro onde colocar uma pedra.
    
    {tabuleiro} → {posicao}'''

    n = obtem_numero_orbitas(t)
    posicoes_livres = obtem_posicoes_pedra(t,0)

    while True:
        input_pos = input('Escolha uma posicao livre:')

        #Verifica se a entrada está no formato correto antes de converte-la para uma string
        if len(input_pos) != 2 or not input_pos[0].isalpha() or not input_pos[1].isdigit():
            continue

        pos = str_para_posicao(input_pos)

        #Verifica se é uma posição valida no tabuleiro
        if eh_posicao(pos) and eh_posicao_valida(pos, n):

            #Verifica se a posição está livre e so retorna a posicao se estiver livre, se nao o loop repete-se
            if pos in posicoes_livres:
                return pos 

#2.2.4 escolhe movimento auto

#Estrategia facil

def estrategia_facil(t,j):
    '''Funcao recebe um tabuleiro e um jogador e devolve uma posicao de acordo com a estrategia facil
        
    {tabuleiro,jogador} → {posicao}
    '''
    posicoes_livres = obtem_posicoes_pedra(t,0)
    n = obtem_numero_orbitas(t)

    #Para cada posicao livre ordenada do tabuleiro roda o tabuleiro e verifica se existem pedras do jogador adjacentes, se sim retorna essa posicao
    for pos in posicoes_livres:
        t_copia = cria_copia_tabuleiro(t)
        t_rodado = roda_tabuleiro(t_copia)
        pos_new = obtem_posicao_seguinte(t_copia,pos,False)
        posicoes_adjacentes = obtem_posicoes_adjacentes(pos_new,n,True)
        for pos_adj in posicoes_adjacentes:
            pos_adj_tad = str_para_posicao(pos_adj)
            posicoes_jogador = obtem_posicoes_pedra(t_rodado,j)
            if pos_adj_tad in posicoes_jogador:
                return pos
    
    #Se nao existir nenhuma posicao livre que rodando o tabuleiro fique adjacente a uma pedra do jogador, retorna a primeira posicao livre ordenada
    return posicoes_livres[0]

#Estrategia normal

def estrategia_normal(t, j):
    '''Funcao recebe um tabuleiro e um jogador e escolhe uma posicao de acordo com a estrategia normal
        
    {tuplo,int} → {int}
    '''

    n = obtem_numero_orbitas(t)
    posicoes_livres = obtem_posicoes_pedra(t,0)

    max_L_jogador = 0
    max_L_adversario = 0
    
    for pos in posicoes_livres:
        
        #Primeiro determina o L do jogador e do adversario
        t_copia_jogador = cria_copia_tabuleiro(t)
        t_rodado_jogador = roda_tabuleiro(t_copia_jogador)
        new_pos_jogador = obtem_posicao_seguinte(t_copia_jogador, pos, False)
        t_jogador = coloca_pedra(t_rodado_jogador, new_pos_jogador, j)
        
        for L in range(1, 2*n + 1):
            if verifica_linha_pedras(t_jogador, new_pos_jogador, j, L):
                if L > max_L_jogador:
                    max_L_jogador = L
        
        t_copia_adversario = cria_copia_tabuleiro(t)
        t_rodado_adversario = roda_tabuleiro(roda_tabuleiro(t_copia_adversario))
        new_pos_adversario = obtem_posicao_seguinte(t_copia_adversario, obtem_posicao_seguinte(t_copia_adversario, pos, False), False)
        t_adversario = coloca_pedra(t_rodado_adversario, new_pos_adversario, -j)
        
        for L in range(1, 2*n + 1):
            if verifica_linha_pedras(t_adversario, new_pos_adversario, -j, L):
                if L > max_L_adversario:
                    max_L_adversario = L
    
    #Se o L do jogador for maior ou igual ao do adversario, joga na posicao livre ordenada que rodando o tabuleiro forma esse L
    if max_L_jogador >= max_L_adversario:
        for pos in posicoes_livres:
            t_copia_jogador = cria_copia_tabuleiro(t)
            t_rodado_jogador = roda_tabuleiro(t_copia_jogador)
            new_pos_jogador = obtem_posicao_seguinte(t_copia_jogador, pos, False)
            t_jogador = coloca_pedra(t_rodado_jogador, new_pos_jogador, j)
            if verifica_linha_pedras(t_jogador, new_pos_jogador, j, max_L_jogador):
                return pos

    #Se o L do adversario for maior que o do jogador, joga na posicao livre ordenada que rodando o tabuleiro impede o adversario de formar o seu L
    elif max_L_jogador < max_L_adversario:
        for pos in posicoes_livres:
            t_copia_adversario = cria_copia_tabuleiro(t)
            t_rodado_adversario = roda_tabuleiro(roda_tabuleiro(t_copia_adversario))
            new_pos_adversario = obtem_posicao_seguinte(t_copia_adversario, obtem_posicao_seguinte(t_copia_adversario, pos, False), False)
            t_adversario = coloca_pedra(t_rodado_adversario, new_pos_adversario, -j)
            if verifica_linha_pedras(t_adversario, new_pos_adversario, -j, max_L_adversario):
                return pos

def escolhe_movimento_auto(t,j,lvl):
    '''Funcao recebe um tabuleiro t (em que o jogo na ̃o terminou ainda), uma pedra j, e a cadeia de carateres lvl correspondente a estrategia, e devolve a posicao escolhida 
    automaticamente de acordo com a estrategia selecionada para o jogador com pedras j.
    
    {tabuleiro,pedra,str} → {posicao}'''

    if lvl == 'facil':
        return estrategia_facil(t,j)
    if lvl == 'normal': 
        return estrategia_normal(t,j)

def orbito(n,modo,jog):
    '''Funcao recebe o numero de orbitas do tabuleiro, uma cadeia de carateres que representa o modo de jogo, e a representacao externa de uma pedra (preta ou branca), e devolve um inteiro 
    identificando o jogador vencedor (1 para preto ou -1 para branco), ou 0 em caso de empate.
    
    {int,str,str} → {posicao}'''

    if type(n) != int or n <2 or n>5 or modo not in ('facil','normal','2jogadores') or jog not in ('X','O'):
        raise ValueError('orbito: argumentos invalidos')
    
    j = str_para_pedra(jog)
    
    print('Bem-vindo ao ORBITO-2.')

    if modo == 'facil' or modo == 'normal':
        print("Jogo contra o computador (" + modo + ").")

        if j == 1:
            print("O jogador joga com 'X'.")
        else:
            print("O jogador joga com 'O'.")

        t = cria_tabuleiro_vazio(n)
        print(tabuleiro_para_str(t))

        if j == -1: #Se o jogador jogar com as pedras brancas entao quem joga primeiro é o computador
            print("Turno do computador (" + modo + "):")
            pos = escolhe_movimento_auto(t,-j,modo)
            t = coloca_pedra(t,pos,-j)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
        
        while True:
            print("Turno do jogador.")
            pos = escolhe_movimento_manual(t)
            t = coloca_pedra(t,pos,j)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t,j):
                print('VITORIA')
                return j
            
            elif eh_vencedor(t,-j):
                print('DERROTA')
                return -j
            
            else: 
                if eh_fim_jogo(t):
                    print('EMPATE')
                    return 0
            
            print("Turno do computador (" + modo + "):")
            pos = escolhe_movimento_auto(t,-j,modo)
            t = coloca_pedra(t,pos,-j)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t,j) and not eh_vencedor(t,-j):
                print('VITORIA')
                return j
            
            elif eh_vencedor(t,-j) and not eh_vencedor(t,j):
                print('DERROTA')
                return -j
            
            else: 
                if eh_fim_jogo(t):
                    print('EMPATE')
                    return 0
    
    if modo == '2jogadores':
        print('Jogo para dois jogadores.')
        t = cria_tabuleiro_vazio(n)
        print(tabuleiro_para_str(t))
        
        while True:
            print("Turno do jogador 'X'.")
            pos = escolhe_movimento_manual(t)
            t = coloca_pedra(t, pos, 1)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            
            if eh_vencedor(t, 1) and not eh_vencedor(t,-1):
                print("VITORIA DO JOGADOR 'X'")
                return 1
            elif eh_vencedor(t, -1) and not eh_vencedor(t,1):
                print("VITORIA DO JOGADOR 'O'")
                return -1
            else:
                if eh_fim_jogo(t):
                    print('EMPATE')
                    return 0
            
            print("Turno do jogador 'O'.")
            pos = escolhe_movimento_manual(t)
            t = coloca_pedra(t, pos, -1)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t, 1):
                print("VITORIA DO JOGADOR 'X'")
                return 1
            elif eh_vencedor(t, -1):
                print("VITORIA DO JOGADOR 'O'")
                return -1
            else:
                if eh_fim_jogo(t):
                    print('EMPATE')
                    return 0

print(posicoes_tabuleiro(2))