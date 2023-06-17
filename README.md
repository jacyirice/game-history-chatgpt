# Game History with ChatGPT

Este programa em Python cria uma história interativa baseada nos parâmetros fornecidos pelo usuário. Ele utiliza o modelo de linguagem ChatGPT, fornecido pela OpenAI, para gerar diálogos e desenvolver a história.

## Requisitos

Certifique-se de ter o Python 3 instalado. Em seguida, instale as dependências necessárias executando o seguinte comando no terminal:

```shell
pip install -r requirements.txt
```

## Uso

1. Clone o repositório para o seu ambiente local:

```shell
git clone https://github.com/jacyirice/game-history-chatgpt.git
```

2. Navegue até o diretório do projeto:

```shell
cd game-history-chatgpt/
```

3. Configuração do arquivo .env

Antes de executar o programa, é necessário criar um arquivo `.env` no diretório do projeto e fornecer a chave de API do OpenAI. Siga as etapas abaixo:

- Crie um arquivo chamado `.env` no diretório do projeto.
- Insira a seguinte linha no arquivo `.env`, substituindo `<SUA_CHAVE_DE_API>` pela sua chave de API do OpenAI:

        OPENAI_API_KEY=<SUA_CHAVE_DE_API>
- Duvidas? Acesse o site da [OpenAI](https://platform.openai.com/docs/quickstart/build-your-application) 
4. Execute o programa Python:

```shell
python main.py
```


5. Siga as instruções exibidas no console para interagir com a história:

- Leia a cena atual, digite sua ação e pressione Enter.
- A próxima cena será criada com base na sua ação.
- Você será solicitado a digitar a próxima ação na nova cena.

## Parâmetros da História

A história gerada seguirá as seguintes diretrizes:

- A história terá no máximo 4 cenas.
- A história começará com um homem (jogador) em um ambiente aleatório e contará como ele descobriu que foi traido.
- Serão utilizadas palavras de baixo calão para dar um tom mais realista e menos culto à história.
- A cada cena, será solicitado ao jogador que digite uma ação para criar a próxima cena.
- Cada cena será numerada e o limite máximo de cenas será respeitado.
- A última cena será finalizada com a frase "Fim da história".

## Validação de Entrada

Para garantir a sintaxe correta das ações do jogador, o programa utiliza um parser ANTLR. O parser verifica se a entrada do usuário segue o formato:
                
    <PERSONAGEM>: <AÇÃO>

Caso a sintaxe seja inválida, uma mensagem de erro será exibida e uma nova ação será solicitada.

## Observações

- Certifique-se de ter uma conexão com a internet para acessar o modelo ChatGPT.
- O programa utiliza um modelo pré-treinado, portanto, as respostas geradas pelo ChatGPT podem variar.
- O modelo de linguagem ChatGPT pode não entender ou interpretar corretamente todos os contextos ou nuances da história.
