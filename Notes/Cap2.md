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
