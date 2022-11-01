# Capítulo 3 - Análise Sintática

## Introdução
Objetivo: Reconhecer padrões
Como: Gramática Livre de Contexto
Resultado: Árvores de Derivação

## Gramática Livre de Contexto
    \<frase> -> \<sujeito> \<verbo> \<predicado> (Produção Inicial)

    \<sujeito> -> aluno

    \<verbo> -> estudou

    \<predicado> -> uma materia \<adjetivo>

    \<adjetivo> -> dificil

- Símbolos terminais: Já foram produzidos(ex.: aluno, estudou, uma materia, ...)

## Árvores de Derivação
- Derivação

        Ex3.:

                Expresssão: (num - num) * num
                exp -> exp op exp | (exp) | num
                op -> + | - | *

                exp -> exp op exp
                exp -> (exp) op exp
                exp -> (exp op exp) op exp
                exp -> (num op exp) op exp
                exp -> (num - exp) op exp
                exp -> (num - num) op exp
                exp -> (num - num) * exp
                exp -> (num - num) * num
                ** (OBS.: FAZER UMA MUDANÇA POR VEZ) **

        Ex4.:

                Expressão: -(id + id)
                E -> E O E | -E | (E) | id
                O -> + | - | *

                E -> -E
                E -> -(E)
                E -> -(E O E)
                E -> -(id O E)
                E -> -(id + E)
                E -> -(id + id)