# Capítulo 1 - Introdução

## Tradutores
- Compiladores
    - Traduz o código inteiro
    - Maior velocidade após traduzir em Objective
- Interpretadores
    - Traduz linha a linha
    - É mais lento

## Processo
- Pré-Processador: Realiza pré ajustes, como remover comentários e incluir bibliotecas
- Compilador: Transforma em Assembly(Objective)
- Assembler: Transforma o código em bínario
- Linker/Loader: Conecta o código com a memória do computador

## Fases do Compilador
- Front-End
    - Análise Léxica
    - Análise Sintática
    - Análise Semântica
    - Geração de Código Intermediário
- Back-End
    - Otimização
    - Geração de código Objective(Assembly)

## Bibliotecas
- Estáticas: Inseridas antes de compilar
- Dinâmicas: Durante alguma das fases do compilador

## Análise Léxica
- Programa é lido e agrupado em sequências
- Identifica padrões(Lexema)
- Verifica o que é função, tipos de variáveis, palavras reservadas, etc (Tokens).
- Cria os Tokens

## Análise Sintática
- Verifica operações entre Tokens
- Analisa a lógica em si

## Análise Semântica
- Verifica compatibilidade entre tipos de variáveis(Ex.: Somar int com float)

## Código Intermediário
- Three Code Adress

## Otimização
- Somente em Compilados
- Melhora e simplifica os laços, remove variáveis não usadas, etc.

## Compilação Cruzada
- Usado em Embarcados
- Compila em um dispositivo Y(Ex.: Raspberry Pi), porém produzido em outro dispositivo(PC)

## Compiladores Híbridos
- Compila para uma VM
- VM interpreta para a arquitetura desejada
- Ex.: Java com JVM