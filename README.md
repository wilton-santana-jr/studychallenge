# -Projeto StudyChallenge
Este projeto consiste em um aplicativo web para alunos cadastrarem questões e realizarem testes para apurar como está o seu desempenho acadêmico em cada matéria estudada. Além disso o usuário poderá cadastrar apostilas e materiais para estudos e pesquisar e avaliar apostilas de outros usuários.

# -Funcionalidades

- Gerenciar flashcards que sãop as questões com perguntas e respostas sobre uma dada matéria escolar;
- Gerenciar testes e desafios com diferentes níveis de dificuldades baseado nos flashcards cadastrados;
- Gerenciar e avaliar apostilas de estudos cadastradas;
- Visualizar meu rendimento acadêmico junto aos testes respondidos e visualizar graficamente quais matérias tenho mais dificuldade e quais tenho melhor desempenho dessa forma o aluno pode focar seus estudos em conteúdos que erra mais;
- Emitir relatórios gráficos estatisticos com informações sobre o desempenho acadêmico do aluno junto aos testes realizados;

# -Home

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/d93b3767-a56d-402f-bb96-28a8b31cab64)



# -Gerenciamento de Contas Bancárias e Categorias de Gastos e Receitas Essenciais

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/2aecf1c9-2839-48f3-aa32-4031995276bb)

# -Gerenciamento de receitas e despesas e geração de extratos bancários de receitas e despesas e exportação via pdf

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/6350fad3-9f55-4b34-9ece-b9260282a02a)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/c0ee6b64-741e-4bcf-b286-6222388f976b)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/2457aa12-f1a0-4f41-82c5-4c57e37a99a6)

# -Gerenciamento do planejamento financeiro com gastos mensais

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/9652616a-ca75-4bc8-aaac-a16ba930c1a5)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/ae302ac3-e0b3-4af9-bbce-a0cace7f9fb9)

# -Gerenciamento de Contas, Boletos e Faturas a Pagar do mês corrente

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/e0bc14f9-836b-4f9f-a4d9-90b7a32b50d9)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/c94d3ad5-34c1-4122-9f8c-e80f1a0d0349)

# -Emissão de relatórios gráficos mensais de receitas e despesas no mês corrente agrupados por categoria

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/ce4fff1d-5ea0-4a77-b6ad-d80495c8d832)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/00e4d3c2-4442-46fc-8a9a-0a2298b2bb88)

![image](https://github.com/wilton-santana-jr/financa_pessoal/assets/12551792/b8bb140b-8b54-4baa-8bba-eb6484263a9e)



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

Agora você pode acessar o website através do endereço: `localhost:8000/usuarios/login/` para testar e usar o aplicativo.

Todos são livres para colaborar com este projeto!!!