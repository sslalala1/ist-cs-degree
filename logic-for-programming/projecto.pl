% lp24 - ist187565 - projecto 
:- use_module(library(clpfd)). % para poder usar transpose/2
:- set_prolog_flag(answer_write_options,[max_depth(0)]). % ver listas completas
:- [puzzles]. % Ficheiro dado. A avaliação terá mais puzzles.
:- [codigoAuxiliar]. % Ficheiro dado. Não alterar.
% Atenção: nao deves copiar nunca os puzzles para o teu ficheiro de código
% Nao remover nem modificar as linhas anteriores. Obrigado.
% Segue-se o código
%%%%%%%%%%%%

% ------------------------------------------------------------------------------------
% visualiza(Lista) 
% permite escrever cada elemento da lista Lista por linha.
% ------------------------------------------------------------------------------------
visualiza([]) :- !.
visualiza([H|T]) :- 
    writeln(H),
    visualiza(T).

% ------------------------------------------------------------------------------------
% visualizaLinha(Lista) permite escrever cada elemento da lista Lista por linha 
% sendo precedido pelo numero da linha, ":" e um espaço.
% ------------------------------------------------------------------------------------
visualizaLinha(Lista) :- visualizaLinha(Lista, 1). % Inicializa o contador do numero da linha

visualizaLinha([],_) :- !.

visualizaLinha([H|T], Index) :-
    % Escreve o numero da linha seguido do elemento correspondente
    write(Index), write(': '), write(H), nl, 
    NovoIndex is Index + 1, % Aumenta o contador
    visualizaLinha(T, NovoIndex).

% ------------------------------------------------------------------------------------
% insereObjecto((L,C), Tabuleiro, Obj) eh verdade se Tabuleiro eh um tabuleiro que apos
% a aplicacao deste predicado tem nas coordenadas (L,C) o objeto Obj.
% ------------------------------------------------------------------------------------
insereObjecto((L,C), Tabuleiro, Obj) :-
    nth1(L, Tabuleiro, ElementosLinha),
    nth1(C, ElementosLinha, Elemento),
    var(Elemento), !,
    Elemento = Obj.

insereObjecto(_, _, _) :- !.

% ------------------------------------------------------------------------------------
% insereVariosObjectos(ListaCoords, Tabuleiro, ListaObjs) 
% ListaCoords eh uma lista de coordenadas e ListaObjs uma lista de objetos. Tabuleiro
% eh o tabueiro que apos a aplicacao do predicado tem nas coordenadas das ListaCoords
% os objetos da Lista Objs.
% ------------------------------------------------------------------------------------
insereVariosObjectos([],_,[]) :- !.

insereVariosObjectos([Coord|RestoCoords],Tabuleiro,[Obj|RestoObjs]) :-
    length([Coord|RestoCoords], Len), 
    length([Obj|RestoObjs], Len), % Garante que ambas as listas tem o mesmo tamanho
    insereObjecto(Coord, Tabuleiro, Obj),
    insereVariosObjectos(RestoCoords, Tabuleiro, RestoObjs).
    
% ------------------------------------------------------------------------------------
% inserePontosVolta(Tabuleiro, (L,C))
% Tabuleiro eh o tabuleiro que apos a aplicacao do predicado inserePontosVolta tem 
% pontos (p) nas posicoes adjacentes as coordenadas (L,C).
% ------------------------------------------------------------------------------------
inserePontosVolta(Tabuleiro, (L,C)) :-
    CoordsAdjacentes = [(L2,C), (L2,C3), (L, C3), (L3, C3), (L3,C), (L3,C2), (L,C2), (L2,C2)],
    L2 is L-1, C2 is C-1, L3 is L+1, C3 is C+1,
    inserePontos(Tabuleiro, CoordsAdjacentes).

% ------------------------------------------------------------------------------------
% inserePontos(Tabuleiro, ListaCoord) 
% Tabuleiro eh o tabuleiro que apos a aplicacao do predicado inserePontos tem pontos
% em cada coordenada de ListaCoord.
% ------------------------------------------------------------------------------------
inserePontos(_,[]) :- !.

inserePontos(Tabuleiro, [Coord|RestoCoords]) :-
    insereObjecto(Coord, Tabuleiro, p), !,
    inserePontos(Tabuleiro, RestoCoords).

% ------------------------------------------------------------------------------------
% objectosEmCoordenadas(ListaCoords, Tabuleiro, ListaObjs)
% ListaObjs eh a lista dos objectos do Tabuleiro correspondentes as coordenadas da 
% ListaCoords, apresentados na mesma ordem que as coordenadas em ListaCoords.
% ------------------------------------------------------------------------------------
objectosEmCoordenadas([],_,[]) :- !.

objectosEmCoordenadas([(L,C)|RestoCoords], Tabuleiro, [Obj|RestoObjs]) :-
    nth1(L, Tabuleiro, ElementosLinha),
    nth1(C, ElementosLinha, Obj),
    objectosEmCoordenadas(RestoCoords, Tabuleiro, RestoObjs).

% ------------------------------------------------------------------------------------
% coordObjectos(Objecto, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos)
% Tabuleiro eh um tabuleiro, ListaCoords eh uma lista de coordenadas e 
% ListaCoordObjs a sublista de ListaCoords que contem as coordenadas dos objectos do 
% tipo Objecto (ordenada por linha e coluna), tal como ocorrem no tabuleiro. 
% NumObjectos é o número de objectos Objecto encontrados. 
% ------------------------------------------------------------------------------------
coordObjectos(Objecto, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-
    var(Objecto), !, % se o nosso Objecto for uma variavel
    findall((L,C), 
        (member((L,C), ListaCoords), % percorremos cada coordenada da ListaCoords
        nth1(L, Tabuleiro, ElementosLinha),
        nth1(C, ElementosLinha, Elemento),
        var(Elemento)), % so aceitamos a coordenada se o Elemento correspondente for uma variavel
        ListaCoordObjs),
    sort(ListaCoordObjs, ListaCoordObjs),
    length(ListaCoordObjs, NumObjectos).

coordObjectos(Objecto, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-
    \+  var(Objecto), !, % se o nosso Objecto for uma constante
    findall((L,C), 
        (member((L,C), ListaCoords), % percorremos cada coordenada da ListaCoords
        nth1(L, Tabuleiro, ElementosLinha),
        nth1(C, ElementosLinha, Elemento),
        Elemento == Objecto), % so aceitamos a coordenada se o Elemento for igual ao nosso Objecto
        ListaCoordObjs),
    sort(ListaCoordObjs, ListaCoordObjs),
    length(ListaCoordObjs, NumObjectos).

% ------------------------------------------------------------------------------------
% coordenadasVars(Tabuleiro, ListaVars) 
% ListaVars sao as coordenadas das variáveis do tabuleiro Tabuleiro ordenadas por linhas
% e colunas.
% ------------------------------------------------------------------------------------
coordenadasVars(Tabuleiro, ListaVars) :-
    % Primeiro, obtemos as coordenadas das posicoes com constantes
    findall((L, C),
        (nth1(L, Tabuleiro, ElementosLinha),
         nth1(C, ElementosLinha, Elemento),
         nonvar(Elemento)), 
        Constantes),

    % Depois obtemos uma lista com todas as coordenadas do tabuleiro
    findall((L, C),
        (nth1(L, Tabuleiro, ElementosLinha),
        nth1(C, ElementosLinha, Elemento)), 
        TodasCoordenadas),

    % Subtraimos as coordenadas das constantes da lista com todas as coordenadas
    subtract(TodasCoordenadas, Constantes, ListaVars),

    % Ordenamos por linhas e colunas
    sort(ListaVars, ListaVars).  

% ------------------------------------------------------------------------------------
% fechaListaCoordenadas(Tabuleiro, ListaCoord) 
% Apos a aplicação deste predicado, as coordenadas de ListaCoord deverão ser apenas 
% estrelas e pontos, considerando as hipoteses h1-h2-h3
% ------------------------------------------------------------------------------------
% Cenario h1
fechaListaCoordenadas(Tabuleiro, ListaCoord) :-
    coordObjectos(e, Tabuleiro, ListaCoord, _, 2), % Verifica que ListaCoord tem  2 estrelas
    coordObjectos(_, Tabuleiro, ListaCoord, ListaCoordObjs, _), !, % e o resto das posicoes vazias
    inserePontos(Tabuleiro, ListaCoordObjs). % enche as restantes coordenadas de pontos

% Cenario h2
fechaListaCoordenadas(Tabuleiro, ListaCoord) :-
    coordObjectos(e, Tabuleiro, ListaCoord, _, 1), % Verifica que ListaCoord tem 1 estrela
    coordObjectos(_, Tabuleiro, ListaCoord, ListaCoordObjs, 1), !, % e uma posicao livre
    nth1(_, ListaCoordObjs, CoordenadaLivre),
    insereObjecto(CoordenadaLivre, Tabuleiro, e), % insere estrela na coordenada livre
    inserePontosVolta(Tabuleiro, CoordenadaLivre). % e pontos a sua volta

% Cenario h3
fechaListaCoordenadas(Tabuleiro, ListaCoord) :-
    coordObjectos(e, Tabuleiro, ListaCoord, _, 0), % Verifica que ListaCoords nao tem estrelas
    coordObjectos(_, Tabuleiro, ListaCoord, ListaCoordObjs, 2), !, % e que tem 2 posicoes livres
    insereVariosObjectos(ListaCoordObjs, Tabuleiro, [e,e]), % insere estrelas nas posicoes livres
    member((L,C), ListaCoordObjs), 
    inserePontosVolta(Tabuleiro, (L,C)). % insere pontos a volta de cada estrela inserida

fechaListaCoordenadas(_,_) :- !.

% ------------------------------------------------------------------------------------
% fecha(Tabuleiro, ListaListasCoord) 
% Apos a aplicação deste predicado, Tabuleiro sera o resultado de aplicar o predicado
% fechaListaCoordenadas a cada lista de ListaListasCoord
% ------------------------------------------------------------------------------------
fecha(Tabuleiro,[H|T]) :-
    fechaListaCoordenadas(Tabuleiro, H), !,
    fecha(Tabuleiro, T).

fecha(_,_) :- !.

% ------------------------------------------------------------------------------------
% encontraSequencia(Tabuleiro, N, ListaCoords, Seq)
% Seq eh uma sublista de ListaCoords que apos a aplicacao do predicado vai conter
% coordenadas de variaveis que aparecem seguidas 
% ------------------------------------------------------------------------------------

encontraSequencia(Tabuleiro, N, ListaCoords, Seq) :-
    % Determina o numero de elementos de ListaCoords
    length(ListaCoords, LenListaCoords),

    ( LenListaCoords > N, ! ->
        % Cenario 1: A ListaCoords tem mais elementos que N
        coordObjectos(_, Tabuleiro, ListaCoords, _, N), % verifica que ListaCoords tem exatamente N variaveis
        coordObjectos(e, Tabuleiro, ListaCoords, _, 0), % verifica que ListaCoords nao tem estrelas
        length(Seq, N), % Seq tem de ter comprimento N
        append(_, Fim, ListaCoords),
        append(Seq, _, Fim);

      LenListaCoords == N, ! ->
        % Cenario 2: A ListaCoords tem exatamente N elementos
        Seq = ListaCoords), 
        
    % Garante que todos os elementos de Seq sao variaveis
    objectosEmCoordenadas(Seq, Tabuleiro, ListaObjsSeq),
    maplist(var, ListaObjsSeq), !.  
    
% ------------------------------------------------------------------------------------
% aplicaPadraoI(Tabuleiro, [(L1, C1), (L2, C2), (L3, C3)])
% Apos a aplicacao deste predicado, Tabuleiro sera o resultado de colocar uma estrela 
% (e) em (L1, C1) e (L3, C3) e os obrigatórios pontos (p) à volta de cada estrela
% ------------------------------------------------------------------------------------
aplicaPadraoI(Tabuleiro, [(L1, C1), _, (L3, C3)]) :-
    insereVariosObjectos([(L1, C1), (L3, C3)], Tabuleiro, [e, e]),
    inserePontosVolta(Tabuleiro, (L1, C1)),
    inserePontosVolta(Tabuleiro, (L3, C3)).

% ------------------------------------------------------------------------------------
% aplicaPadroes(Tabuleiro, ListaListaCoords)
% Apos a aplicacao deste predicado, ter-se-ao encontrado sequências de tamanho 3 e 
% aplicado o aplicaPadraoI/2, ou então ter-se-ao encontrado sequências de tamanho 4 
% e aplicado o aplicaPadraoT/2
% ------------------------------------------------------------------------------------
aplicaPadroes(_,[]) :- !.

aplicaPadroes(Tabuleiro, [Coordenadas|RestoCoordenadas]) :-
    (encontraSequencia(Tabuleiro, 3, Coordenadas, Seq) -> 
    aplicaPadraoI(Tabuleiro, Seq); % se encontra uma sequencia de 3, aplica o padraoI
    encontraSequencia(Tabuleiro, 4, Coordenadas, Seq) ->
    aplicaPadraoT(Tabuleiro, Seq)), % se encontrar uma sequencia de 4, aplica o pradraoT
    aplicaPadroes(Tabuleiro, RestoCoordenadas).

aplicaPadroes(Tabuleiro, [_|RestoCoordenadas]) :-
    aplicaPadroes(Tabuleiro, RestoCoordenadas).
% ------------------------------------------------------------------------------------
% resolve(Estruturas, Tabuleiro)
% Apos a aplicacao deste predicado, o Tabuleiro eh o tabuleiro que resulta de aplicar
% os predicados aplicaPadroes/2 e fecha/2 ate ja nao haver mais alteracoes nas 
% variaveis do tabuleiro
% ------------------------------------------------------------------------------------
resolve(_, Tabuleiro) :-
    coordenadasVars(Tabuleiro, ListaVars),
    length(ListaVars, 0), !. % termina quando nao houver mais variaveis no tabuleiro

resolve(Estruturas, Tabuleiro) :-
    coordenadasVars(Tabuleiro, ListaVars),
    length(ListaVars, Len),
    Len > 0, !, 
    coordTodas(Estruturas, CoordTodas), 
    aplicaPadroes(Tabuleiro, CoordTodas), 
    fecha(Tabuleiro, CoordTodas), 
    coordenadasVars(Tabuleiro, NovaListaVars), !, 
    length(NovaListaVars, NovaLen), % determina o numero de variaveis 
    % se o numero de variaveis diminuiu, entao continuamos a recursao
    (NovaLen < Len -> resolve(Estruturas, Tabuleiro) ; true). 
    