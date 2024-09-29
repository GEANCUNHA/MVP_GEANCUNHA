# **Aplicação Full Stack - Predição de Aprovação de Empréstimo**

Esta aplicação full stack faz a predição de aprovação de empréstimo utilizando um modelo de Árvore de Decisão treinado com dados normalizados. O usuário pode fornecer os dados através de um formulário web, e o sistema retorna se o empréstimo será aprovado ou não com base nas características fornecidas.

**Funcionalidades**
Formulário para inserção de dados sobre o solicitante de empréstimo.
Predição de aprovação ou rejeição de empréstimo.
Integração com um modelo de Árvore de Decisão otimizado e treinado previamente.

**Use um ambiente virtual para isolar as dependências da aplicação.**

No Windows: 

python -m venv venv
venv\Scripts\activate


No MacOS/Linux:

python3 -m venv venv
source venv/bin/activate

Com o ambiente virtual ativado, instale as dependências necessárias executando o seguinte comando:

pip install -r requirements.txt


Executar a Aplicação
Após a instalação das dependências, a aplicação pode ser iniciada com o seguinte comando:


python app.py

A aplicação estará disponível no seu navegador local no endereço: http://127.0.0.1:5000/

**Estrutura do Projeto**

├── app.py               # Código principal da aplicação Flask
├── modelo_arvore_decisao_otimizado.pkl  # Arquivo do modelo treinado
├── scaler.pkl           # Arquivo do normalizador (scaler) treinado
├── templates
│   └── index.html       # Template HTML da página de predição
├── static
│   └── style.css        # Arquivo de estilos CSS (opcional)
├── venv                 # Ambiente virtual (não incluído no repositório)
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Documentação da aplicação

**Testes Automatizados**
O arquivo test_model.py contém testes automatizados usando PyTest para verificar a acurácia do modelo. Para rodar os testes, execute o seguinte comando:

pytest -s test_model.py

