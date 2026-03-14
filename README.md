# 💳 CredIA — Assistente Inteligente de Análise de Crédito

CredIA é uma aplicação interativa desenvolvida em **Python** que utiliza **IA local e análise de dados** para ajudar usuários a entender seu perfil financeiro e tomar decisões mais conscientes sobre crédito e empréstimos.

A aplicação combina **dados financeiros simulados**, **visualização de dados** e **um modelo de linguagem rodando localmente** para fornecer recomendações personalizadas de crédito.

---

# 🚀 Funcionalidades

✔ Dashboard financeiro do cliente
✔ Visualização de transações e perfil de crédito
✔ Assistente de crédito com IA
✔ Recomendação de produtos financeiros
✔ Análise de risco baseada em dados do cliente
✔ Interface web interativa

---

# 🧠 Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* JSON / CSV datasets
* Requests API
* Ollama (LLM local)

---

# 📊 Estrutura do Projeto

```
CredIA
│
├── data
│   ├── perfil_pagador.json
│   ├── produtos_financeiros.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── tabela_de_clientes_CredIA.csv
│
├── src
│   └── app.py
│
└── README.md
```

---

# 💻 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/SEU_USUARIO/credia.git
```

### 2️⃣ Entrar na pasta

```
cd CredIA
```

### 3️⃣ Instalar dependências

```
pip install streamlit pandas requests
```

### 4️⃣ Executar a aplicação

```
streamlit run src/app.py
```

---

# 🤖 Como Funciona a IA

O CredIA utiliza um **modelo de linguagem executado localmente via Ollama** para:

* interpretar o perfil financeiro do cliente
* avaliar risco de crédito
* sugerir produtos financeiros adequados
* explicar decisões de forma simples

A IA recebe um **contexto estruturado com dados reais do cliente**, incluindo:

* renda mensal
* score de crédito
* histórico de atrasos
* comprometimento de renda
* histórico de transações

---

# 📈 Exemplo de Uso

O usuário pode perguntar coisas como:

```
Qual empréstimo é mais seguro para mim?
```

ou

```
Posso pegar um empréstimo de 20 mil?
```

E o CredIA analisa os dados do cliente para gerar uma resposta personalizada.

---

# 🎯 Objetivo do Projeto

Este projeto foi criado para demonstrar:

* uso de **IA aplicada a finanças**
* integração entre **dados e modelos de linguagem**
* construção de **interfaces analíticas com Streamlit**

---

# 🔮 Possíveis Evoluções

* Score de crédito com Machine Learning
* Simulador de parcelas de empréstimo
* Dashboard analítico avançado
* Integração com APIs bancárias
* Deploy em nuvem

---

# 👨‍💻 Autor

Projeto desenvolvido por **Anderson Santos**.

---
# 📄 pitch
- Link video youtube do NotebookLM : https://www.youtube.com/watch?v=KQv5_BEOZDM
- Link apresentação pessoal: https://www.youtube.com/shorts/d_VFByTiYWo
  


# 📄 Licença

Este projeto é open-source e pode ser utilizado para fins educacionais e experimentais.
