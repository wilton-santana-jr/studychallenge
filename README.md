# -Projeto StudyChallenge
Este projeto consiste em um aplicativo web para alunos cadastrarem questões e realizarem testes para apurar como está o seu desempenho acadêmico em cada matéria estudada. Além disso o usuário poderá cadastrar apostilas e materiais para estudos e pesquisar e avaliar apostilas de outros usuários.

# -Funcionalidades

- Gerenciar flashcards que sãop as questões com perguntas e respostas sobre uma dada matéria escolar;
- Gerenciar testes e desafios com diferentes níveis de dificuldades baseado nos flashcards cadastrados;
- Gerenciar e avaliar apostilas de estudos cadastradas;
- Visualizar meu rendimento acadêmico junto aos testes respondidos e visualizar graficamente quais matérias tenho mais dificuldade e quais tenho melhor desempenho dessa forma o aluno pode focar seus estudos em conteúdos que erra mais;
- Emitir relatórios gráficos estatisticos com informações sobre o desempenho acadêmico do aluno junto aos testes realizados;

# -Login

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/53e415ba-94f3-4140-bb2b-070bbb60e780)

# -Cadastro de Usuário

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/b2c8ea4a-5c4f-41a2-9c88-28e8ea27c96f)

# -Gerenciamento de FlashCards Perguntas para estudos

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/09ac1b44-deb0-4768-9e57-299198e18e6c)

# -Criação de Desafios para o aluno praticar e ver como está seu conhecimento

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/00a429cb-ec43-4a09-9180-eb74fe6a25ca)

# -Gerenciamento dos desafios criados: aqui o aluno poderá acompanhar o andamento dos desafios e filtrar e responder os mesmos.

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/36a2d1ad-049e-4e55-9e74-ff08762c9694)

# -Tela onde o Usuário consegue responder um determinado desafio indicando as questões que acertou e as que errou em um dado desafio.Além disso o usuário poderá acessar a tela de relatório detalhado do desafio para analisar seu rendimento.

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/ce53d82e-295f-4955-b289-6c2ae925de5e)

# -Tela de geração de relatórios gráficos mostrando o desempenho do aluno quais suas melhores matérias e quais suas piores matérias e onde ele precisa melhorar.

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/9f147b12-4b3e-4d7c-bf4f-5a3a2155e886)

# -Tela para Gerenciamento de Apostilas onde o usuário poderá cadastrar materias de estudo e também pesquisar materiais de estudos em geral de outros usuários para estudo e avaliação.

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/0736e4a4-6fd8-4be8-a19a-1d29ad23b89b)

# -Tela para download do material de estudo acessado onde também o usuário poderá avaliar o material didático acessado dando uma nota ruim, boa, ótima ou excelente dependendo do seu gosto com relação ao conteúdo do material acessado.

![image](https://github.com/wilton-santana-jr/studychallenge/assets/12551792/804302b7-b084-4877-9855-0584f3b3e76d)

# - Protótipo do Figma do Projeto Web

https://www.figma.com/file/SAOG2OXjqWjawFeEpjUtNF/Untitled-(Copy)?type=design&node-id=0-1&mode=design&t=roppZMocBb5DeYZk-0

# Para instalação

## Prerequisitos

Antes de iniciar instale no seu sistema:

- Python (version 3.6 or higher)
- pip (Python package installer)

## Instalação

1. Clone o repositorio do projeto:

    ```bash
    git clone https://github.com/wilton-santana-jr/studychallenge.git
    ```

2. Navege até o diretório do projeto:

    ```bash
    cd studychallenge
    ```

3. Crie um ambiente virtual:
    - No Windows:

        ```bash
        python -m venv .venv
        ```

    - No Linux:

        ```bash
        python3 -m venv .venv
        ```

4. Ative o ambiente virtual:

    - No macOS e Linux:

      ```bash
      source .venv/bin/activate
      ```

    - No Windows:

      ```bash
      .\.venv\Scripts\activate
      ```

5. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

6. Configure a base de dados:

    ```bash
    python manage.py migrate
    ```

    ```bash
    python manage.py makemigrations flashcard
    ```

    ```bash
    python manage.py makemigrations apostilas
    ```

    ```bash
    python manage.py migrate
    ```

7. Crie uma conta de superusuário (admin):

    ```bash
    python manage.py createsuperuser
    ```


8. Coletando arquivos estáticos:

    ```bash
    python manage.py collectstatic
    ```

## Rodando o projeto

Para executar o aplicativo web, execute o comando abaixo:

```bash
python manage.py runserver
```

Antes de tudo você deve acessar o website através do endereço: `localhost:8000/admin/login/` com o superusuário e cadastrar as categorias máterias de ensino que o seu app irá utilizar.

Depois disso acima você agora pode acessar o website através do endereço: `localhost:8000/usuarios/login/` para testar e usar o aplicativo.


Todos são livres para colaborar com este projeto!!!