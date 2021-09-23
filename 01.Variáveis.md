# Variáveis e Tipos Primitivos

## Definicoes:
    - Na linguagem de programacao é feito a manipulacao de variáveis. 

### Variáveis
 - Geral:
    - Variáveis são utilizadas para armazenar valores dentro do código, existem diferentes tipos de variáveis, cada uma adequada para alguma situação.

    Alguns dos tipos primários de variáveis:
    → int: utilizadas para armazenar números inteiros.
    → float: utilizada para pontos flutuantes, ou seja, números reais.
    → string: utilizadas para armazenar textos.
    → boleeano: utilizadas para armazenar condição binária de True (verdadeiro) ou False (falso).

* Em python não precisamos declarar o tipo de variável, ele reconhece de forma automática.

### Variável:

    - Nome que se refere a um valor, um endereco simbólibo;
    - Pode assumir valores distintos, mas somente um unico valor a cada instante da execucao do programa/algoritmo.

#### Comandos de atribuicao:
    - Criam uma nova variavel e tambem fornecem a elas o valor ao qual farao referencia

#### Tipos de Variáveis:
    - Os valores e variaveis em Python sao classificados em diferentes tipos que definem os valores que a variavel pode assumir e quais operacaoes que podem ser realizadas;
    - O tipo de variável se altera conforme o dado armazenado;
    - Comando Type(x) - permite saber o tipo do valor ou variável em x

### Tipos Primitivos

    - Sao informacoes dos dados em sua forma mais simples:

- INT: Números inteiros. Ex.: 1, 9, 45, 100;
- FLOAT: Números fracionários(ponto flutuante). Na parte decimal, usa-se o pornto e nao a vîrgula Ex.: 1.5, 2.70, 3.85;
- STG: String é uma sequencia de caracteres em determinada ordem; Pode ser escrito com testo de aspas 'simples' ou "duplas";
- Boll: Boleano armazena apenas valores do tipo 'True' ou 'False'

------------------------------------------------------------------------------------

## Exercícios:

<b> Geral:</b><br>
→ Variáveis são utilizadas para armazenar valores dentro do código, existem diferentes tipos de variáveis, cada uma adequada para alguma situação.
<br>

<b> Alguns dos tipos primários de variáveis</b><br>

<b>int:</b> utilizadas para armazenar números inteiros.<br>
<b>float:</b> utilizada para pontos flutuantes, ou seja, números reais.<br>
<b>string:</b> utilizadas para armazenar textos. <br>
<b>boleeano:</b> utilizadas para armazenar condição binária de True (verdadeiro) ou False (falso). <br>
<br>

→ Em python não precisamos declarar o tipo de variável, ele reconhece de forma automática.<br>
<h2>Exemplos:</h2>
    
    - inteiro = 1
    - real = 3.45
    - texto = 'isso é uma string'
    - texto_2 = "isso também, pode escolher aspas simples ou duplas"
    - booleano = True

→ Para saber o valor da variável podemos colocar o compar print, como no exemplo abaixo:

#podemos colocar comentários dentro de uma célula de código dessa forma

    print(inteiro)

#podemos colocar diversos prints na mesma célula
    
    print(inteiro)
    print(real)
    print(texto)
    print(texto_2)
    print(booleano)

	Stream Exemplos Linha 57
		1
		3.45
		isso é uma string
		isso também, pode escolher aspas simples ou duplas
		True

#ou podemos imprimir tudo em uma única linha

    print(inteiro,real,texto,texto_2,booleano)

	Stream
		1 3.45 isso é uma string isso também, pode escolher aspas simples ou duplas True

#podemos também usar uma linha de código e printar pulando linha com o <b>\n</b>

    print(inteiro,'\n',real,'\n',texto,'\n',texto_2,'\n',booleano)

	Stream
		1 
		3.45 
		isso é uma string 
		isso também, pode escolher aspas simples ou duplas 
		True

- Como em nenhum momento é declarado o tipo da variável e o python reconhece sozinho, verificar se o tipo da variável foi reconhecido corretamente é uma boa prática e ajuda diagnosticar muitos erros de código.

#o python possui a função "type()" já nativa e construída para mostar o tipo da variável
    
    print('Inteiro:',inteiro, ' Tipo:',type(inteiro))
    print('Real:',real, ' Tipo:',type(real))
    print('Texto:',texto, ' Tipo:',type(texto))
    print('texto_2:',texto_2, ' Tipo:',type(texto_2))
    print('Booleano:',booleano, ' Tipo:',type(booleano))

	Stream
		Inteiro: 1  Tipo: <class 'int'>
		Real: 3.45  Tipo: <class 'float'>
		Texto: isso é uma string  Tipo: <class 'str'>
		texto_2: isso também, pode escolher aspas simples ou duplas  Tipo: <class 'str'>
		Booleano: True  Tipo: <class 'bool'>

<b><h2>Dicas</h2>

- O Python é case sensitive, ou seja, caso você colocar a mesma letra maiúscula onde é minúscula ele não vai reconhecer.

    print(Inteiro)

	Error
		NameError
		---------------------------------------------------------------------------
		NameError                                 Traceback (most recent call last)
		<ipython-input-9-6b580d4682dd> in <module>()
		----> 1 print(Inteiro)
		
		NameError: name 'Inteiro' is not defined

- Sempre deixe o código em ordem de execução e atribua sempre nomes autoexplicativos para as variáveis, sempre vai te ajudar saber qual valor está ali e ajudará na hora de utilizar.

### Exercícios:

    1. Na célula abaixo crie uma variável de cada tipo aprendido e atribua um valor para cada uma delas, lembre-se de utilizar as dicas da aula.

        inteiro = 8
        real = 5.3
        texto = 'Keep Pounding'
        victory = True


    2. Na célula abaixo imprima os valores atribuídos em cada variável, pula uma linha de uma variável para a outra.

        print(inteiro, '\n', real,'\n', texto,'\n', victory)


    3. Na Célula abaixo imprima os tipos de cada variável.

        print('Inteiro:',inteiro, ' Tipo:',type(inteiro))
        print('Real:',real, ' Tipo:',type(real))
        print('Texto:',texto, ' Tipo:',type(texto))
        print('Victory:',victory, ' Tipo:',type(victory))
