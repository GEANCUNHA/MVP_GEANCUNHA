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

**Exemplos de Teste para o Formulário e Predição**
Aqui estão quatro exemplos organizados com base nos campos necessários para o formulário de predição de empréstimos. Esses exemplos podem ser usados para verificar os resultados de "Aprovado" e "Rejeitado" na aplicação.

**Exemplo 1: Rejected**
Número de Dependentes: 0
Renda Anual: 4.500.000
Valor do Empréstimo: 11.500.000
Prazo do Empréstimo (meses): 14
Pontuação CIBIL: 509
Valor dos Ativos Residenciais: 13.400.000
Valor dos Ativos Comerciais: 2.300.000
Valor dos Ativos de Luxo: 15.400.000
Valor dos Ativos Bancários: 5.900.000
Educação (0 = Graduado, 1 = Não Graduado): 1 (Não Graduado)
Autônomo (0 = Não, 1 = Sim): 1 (Sim)

**Exemplo 2: Approved**
Número de Dependentes: 5
Renda Anual: 8.800.000
Valor do Empréstimo: 29.300.000
Prazo do Empréstimo (meses): 10
Pontuação CIBIL: 560
Valor dos Ativos Residenciais: 16.800.000
Valor dos Ativos Comerciais: 13.900.000
Valor dos Ativos de Luxo: 31.100.000
Valor dos Ativos Bancários: 9.900.000
Educação (0 = Graduado, 1 = Não Graduado): 0 (Graduado)
Autônomo (0 = Não, 1 = Sim): 0 (Não)

**Exemplo 3: Approved**
Número de Dependentes: 3
Renda Anual: 3.000.000
Valor do Empréstimo: 7.500.000
Prazo do Empréstimo (meses): 6
Pontuação CIBIL: 881
Valor dos Ativos Residenciais: 1.400.000
Valor dos Ativos Comerciais: 4.500.000
Valor dos Ativos de Luxo: 6.100.000
Valor dos Ativos Bancários: 2.300.000
Educação (0 = Graduado, 1 = Não Graduado): 0 (Graduado)
Autônomo (0 = Não, 1 = Sim): 1 (Sim)

**Exemplo 4: Rejected**
Número de Dependentes: 5
Renda Anual: 1.300.000
Valor do Empréstimo: 3.000.000
Prazo do Empréstimo (meses): 20
Pontuação CIBIL: 540
Valor dos Ativos Residenciais: 1.000.000
Valor dos Ativos Comerciais: 2.300.000
Valor dos Ativos de Luxo: 3.200.000
Valor dos Ativos Bancários: 1.900.000
Educação (0 = Graduado, 1 = Não Graduado): 0 (Graduado)
Autônomo (0 = Não, 1 = Sim): 0 (Não)

