# GitHubUserActivity
Um projeto CLI simples para buscar informações sobre as atividades de um usuário do Github.

## Descrição
GitHubUserActivity é uma cli para exibir informações sobre os eventos de um usuário do github

Esse projeto é uma solução para o desafio proposto pelo [roadmap.sh](https://roadmap.sh/projects/github-user-activity)


## Download
Para fazer o download podemos utilizar a ferramenta [git](https://git-scm.com/)
<br>
Com essa ferramenta instalada na sua máquina o download pode ser feito no diretório onde você quer que 
seja salvo o projeto fazendo:
``` git
git clone --depth 1 https://github.com/DSV17/GitHubUserActivity.git
```


## Instalação
Para fazer a instalação desse projeto deve seguir so seguintes passos

### Criar e ativar o ambiente virtual (opcional)
Você pode criar um ambiente virtual para evitar conflito de versões. Para fazer isso primeiro execute
no diretório do projeto GitHubUserActivity:

#### No Linux
``` bash
python -m venv venv
source venv/bin/activate
```

#### No Windows 
``` PowerShell
python -m venv venv
venv\Scripts\activate
```

### Instalar as dependências do projeto
Para utilizar o projeto será necessário fazer a instalação dos pacotes do pip do quais ele tem depedência. Para fazer isso podemos fazer:
``` bash
pip install -r requirements.txt
``` 

### Instalar o projeto utilizando o pip
Agora basta instalar o projeto com o pip fazendo no diretório do projeto (mesmo diretorio do arquivo setup.py):
``` bash
pip install .
```

## Execução
Com isso já podemos usar a cli. Os comandos são:

### github-activity <username>
Para pegar todas as informações dos eventos relacionadas a um usuário. Por exemplo:
``` bash
github-activity DSV17
```

## Tecnologias
Para criar esse projeto foi utilizado a tecnologia:

1. [python](https://www.python.org/)