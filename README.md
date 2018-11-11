# coda-twitterbot
Código da palestra "Construa seu primeiro bot no Twitter com Python"

### Obtendo suas chaves para usar a API do Twitter

Você primeiro precisa solicitar uma "devloper account" do Twitter [neste endereço](https://developer.twitter.com/en/apply/user). A resposta pode levar alguns dias (até junho de 2018 o prcesso era automático). Com a permissão do Twitter, você poderá criar apps. Ao criar uma app, o Twitter te dará algumas "chaves" que permitirão automatizar processos. Após ter acesso a essas chaves, crie um arquivo neste diretório chamado .env

Nele coloque os seguintes valores:
CONSUMER_KEY=XXXXXXX
CONSUMER_SECRET=XXXXXXX
ACCESS_TOKEN=XXXXXXX
ACCESS_TOKEN_SECRET=XXXXXXX

(Substituindo o XXXXX pelos valores fornecidos pelo Twitter na página do app que você criou)

### Instale as bibliotecas

Lembrando que o código usa Python 3.6. Instale na sua máquina [aqui](https://www.python.org/downloads/)  

Rode pip install -r requirements.txt (no Mac, pip3 install)


### Rode o Jupyter Notebook
Usando o prompt de comando ou terminal no diretório onde está instalado o repositório, digite jupyter notebook

No notebook _coda-twitterbot_ tem todo o código da aula. Basta rodar cada célula para ver como é possível interagir com a API do Twitter. Algumas das funções mostradas no Jupyter Notebook estão consolidadas em uma classe chamada burgostwitter.py. Explore para ver como é possível usá-la para deixar o código mais limpo.