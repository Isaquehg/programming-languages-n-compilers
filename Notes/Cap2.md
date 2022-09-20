# Capítulo 2 - Análise Léxica

## Introdução
- Varrer o código e encontrar Tokens (Scanning)
- Remove comentários e espaços desnecessários

## Léxica vs Sintática
- Léxica: cria os Tokens INDIVIDUALMENTE
- Sintática: verifica se faz sentido a sintaxe entre os tokens

## Termos
- Lexema: Palavras já conhecidas pelo compilador
- Token: Lexema após processado e classificado < classe_do_Token, lexema >
Obs.: Palavras reservadas, normalmente, são o próprio Token, exemplo: < while >
- Padrões: RegEX

## Ex1:
Obs.: As classes podem variar
### Java:
    if(i == j){
        z = 0;
    }
    else{
        z = 1;
    }
    RESPOSTA: < PC, if>, < ( >, < ID, i >, < COMP, == >, < ID, j >, < ) >, < { >, < ID, z >, 
    < OP, = >, 

    < NUM, 0 >, < ; >, < } >, < PC, else >, < { >, < ID, z >, < OP, = >, < NUM, 1 >, < ; >, < } > 

### C++:
    while(x1 != 3){
        printf("Valor de X: %d", x1);
        x1 = x1 + 1;
    }
    RESPOSTA: < PC, while >, < ( >, < ID, x1 >, < COMP, != >, < NUM, 3 >, < { >, < PC, printf >, < ( >,

    < " >, < LIT, valor de X: %d >, < " >, < , >, < ID, x1 >, < ; >, < ID, x1>, < OP, = >, < ID, x1 >, 
    
    < OP, + >, < NUM, 1 >, < ; >, < } >

### Python:
    num = float(input("Entre com um num:"))
    while num > 0:
        num -= 0.5

    RESPOSTA: < ID, num >, < OP, = >, < PC, float >, < ( >, < PC, input >, < ( >, 

    < LIT, Entre com um num: >, < ) >, < ) >, < PC, while >, < ID, num >, < COMP, > >, < NUM, 0 >,

    < : >, < ID, num >, < OP, = >, < ID, num >, < OP, - >, < NUM, 1 >

    obs.: Pode considerar < num- > como OP

## RegEX
- Alfabeto Σ(Ex.: ASCII)
- Alfabeto tem Strings que formam a linguagem: Σ -> Strings -> linguagem
- Operações fundamentais (Metacaracteres do Regex):
    - União(|): Obtém-se somente as repetições como resultado entre dois conjuntos
    - Concatenação(. ou nada): Obtém-se a junção de todos elementos um a um com o do outro conjunto(propriedade distributiva entre elementos)
    - Fechamento(*): Nenhuma aparição ou infinitas aparições de... Os elementos aparecerão infinitamente de várias quantidades
    - Qualquer caracter sozinho(.): Qualquer caracter DO ALFABETO
    - Uma ou mais instâncias(+): igual Fechamento, porém sem vazio
    - Zero ou uma instância(?): Zero ou uma ocorrência de um carácter
- Exemplo: letra(letra | digito)*  -> começa com letra, após isso pode ter várias letras ou dígitos e se repetirem infinitas vezes ou até ser vazio
- OBS.: SEMPRE BUSQUE ATENDER O CASO BASE!

### Ex2
    a) a | b = {a, b}
    b) (a | b)(a | b) = {aa, ab, ba, bb}
    c) a* = {vazio, a, aa, aaa, aaaa, aaaaa, ...}
    d) (a | b)* = {vazio, a, b, aa, bb, aaa, bbb, aab, aba, abb, baa, bab, bba, ...}
    e) a | a * b = {a, b, ab, aab, aaab, aaaab} (Lado esquerdo produz a. Lado direito produz vazio&b, portanto b, como mínimo)
    f) (a | b)+c = {ac, bc, abc, aac, bbc, aaaac, aaabc, aabbc, abbbc, bbbbc, ...}
    g) (a | b)ab = {aab, bab}
    h) abc? = {ab, abc}
    i) a?bc. = {bca, bcb, bcc, abcc, abcb, abca}
    j) (a | bc)* = {vazio, bc, a, abc, aabc, aa, abcbc, bcaabc, aaabcbcbc, ...}

## Classes de Caracteres
- Simplificam Regex. Ex.: (a | b | c)* = [a - c]* 
- Negação/restrição: ^    Ex.: [^a - d]
- Exemplos:
    - [a - z]+{2, 5} -> Qualquer palavra de 2 a 5 letras minúsculas
    - Pythex ^[a - z0 - 9]{,5}$

### Ex3
    a) Número negativos
        ^-[0-9]+$       Obs.: Considera -0
    b) Apenas vogais
        ^[aeiou]+$
    c)Inatel em qualquer combinação de maiusculas e minusculas
        ^[inatelINATEL]+$       ^[Ii][Nn][Aa][Tt][Ee][Ll]+$
    d)Nome de usuário válido com no minimo 3 e max 15 caracteres
        ^[a-zA-Z0-9]+ {3,15}$       ou  ^\w{3,15}$     ou      ^[A-z]{3,15}$ 
    e) cep de uma cidade(37540-000)
        ^[0-9]{5}-[0-9]{3}$
    f) Endereços de email Gmail e Yahoo
        ^[A-z]+@(gmail|yahoo)\.com$
    g) Horario no formato de 24 horas(19:30)
        ^[0-9]{2}\:[0-9]{2}$

### Ex4
    Identificar qualquer número positivo, como: 1577, 15.2, 3.14E4, 3.14E-4
    a) Dígito: [0-9]
    b) Dígitos: [0-9]+       =      dígito+   
    c) numFrac: \.[0-9]+     =      \.dígitos
    d) numExp: E-?[0-9]+     =      E-?dígitos
    e) num: [0-9]+\.[0-9]+?E-?[0-9]+?      =      dígitosnumFrac?numExp?

### Lista de Aula
    1) Defina os Tokens
    Função em C++
    /*comment 1*/
    int main(){
        int x,y;//comment 2
        x=-2;
        y=4;
        x=x*y;
        printf("value");
        printf("%d",x);
        return 0;
    }

    <PC, int>; <ID, main>; <(>; <)>; <{>; <}>; <PC, int>; <ID, x>; <,>; <ID, y>; <;>; <ID, x>; <OP, =>;
    <NUM, -2>; <ID, y>; <OP, =>; <NUM, 4>; <ID, x>; <OP, =>; <ID, x>; <OP, *>; <ID, y>; <;>; 
    <PC, printf>; <(>; <">; <LIT, "Valor:">; <">; <)>; <;>; <PC, printf>; <(>; <">; <LIT, "%d">; <">; <,>; <ID, x>; <)>; <;>; <PC, return>; <NUM, 0>; <;>; <}>

    2)Considere o alfabeto Σ = {0,1}
    a) Sequencia de numeros que iniciam com 10
    10[01]*

    b) Sequência de numeros que terminam com três 1's consecutivos
    [01]*111

    c) Sequencia de numeros que deve começar com 1 e terminar com 0
    1[0-1]*0

    d) Sequencia de numeros que contêm pelo menos três 1's em QUALQUER posição
    [01]*1[01]*1[01]*1

## Autômatos Finitos
- Definição
    - Representa um fluxo possível de símbolos 
    - Possui estados iniciais e finais(aceitação)
- Elementos
    - Fita de Entrada: "vetor" da entrada
    - Unidade de Controle: Estado atual da máquina
    - Função de Transição: Determina o novo estado
- Tipos Finitos:
    - Deterministas(DFA): Apenas um caminho possível a cada iteração(POR LETRA!)
    - Não Deterministas(NFA): Vários caminhos possíveis
    - com Movimentos Vazios(NFA-ε): Pode ter transições com ε(vazio)
- Quíntupla/5-tuple de um DFA

        A = (Q, Σ, δ, q0, F)

    - A: Nome do DFA
    - Q: Conjunto de estados
    - Σ: Conjunto de símbolos de entrada
    - δ: Função de transição
    - q0: Seu estado inicial
    - F: Estados de aceitação ou o estado q pode finalizar

- Tabela de Transição
    - Colunas: Entradas
    - Linhas: Estados
    - (->) para indicar estado inicial
    - (*) para indicar estado final

- Construção de Thompson
    1. Construir um NFA para cada subexpressão(Cada caractere necessita de dois estados)
    2. Utilizamos ε-transições para juntar cada pedaço de uma RegEx
    3. União de dois caracteres deve criar mais dois estados comuns aos dois caracteres(4 estados), um de início e outro de aceitação, ligados por ε.
    4. Repetição(\*) de um caractere (2 estados) utiliza-se mais dois estados, como em *3* , porém interligados com ε e interliga os outros dois estados com ε também.
    5. Repetição(+) interliga dois estado(1 caractere) e mais outra ligação ε entre eles 