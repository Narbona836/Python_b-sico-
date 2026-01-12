# 🧪 Python Básico para QA — Guia de Estudo e Consulta

Este repositório reúne **exemplos práticos e comentados de Python com foco em Qualidade de Software (QA)**. O objetivo é servir como **material de estudo**, **consulta rápida** e **base técnica** para quem atua ou deseja atuar como **QA Manual ou QA em Automação**.

O conteúdo foi organizado para reforçar **lógica de programação**, **leitura de código**, **entendimento de erros** e **estruturação de projetos**, habilidades essenciais no dia a dia de QA.

---

## 🎯 Público-alvo

* QAs iniciantes
* QAs manuais que querem aprender programação
* QAs em transição para automação
* Estudantes de teste de software

---

## 📂 Estrutura do Projeto

```
Python Basico/
├── Variaveis_tipos_de_dados.py
├── Operadores.py
├── Condicionais.py
├── For_while.py
├── Funcoes.py
├── Listas_arrays.py
├── Tuplas.py
├── Dicionarios.py
├── Input.py
├── Try_exept.py
└── POO/
    ├── __init__.py
    ├── usuario.py
    ├── admin.py
    └── main.py
```

---

## 📘 Conteúdo com Visão de QA

### 🔹 Fundamentos de Python

Esses arquivos ajudam o QA a:

* Entender regras de negócio escritas em código
* Validar fluxos condicionais
* Criar scripts simples de apoio a testes

Conteúdos:

* Variáveis e tipos de dados
* Operadores lógicos e relacionais
* Condicionais (`if / else`)
* Laços de repetição (`for`, `while`)
* Funções

---

### 🔹 Estruturas de Dados (Muito usadas em testes)

* **Listas** → massa de testes, cenários, dados parametrizados
* **Tuplas** → dados fixos (ex: configurações)
* **Dicionários** → payloads de API, dados de usuários, respostas JSON

---

### 🔹 Tratamento de Erros

O arquivo `Try_exept.py` aborda:

* Captura de erros
* Validação de fluxos inesperados
* Escrita de código mais resiliente

Esses conceitos são essenciais para:

* Testes negativos
* Validação de falhas esperadas
* Análise de bugs

---

## 🧱 Programação Orientada a Objetos (POO) aplicada a QA

A pasta `POO` simula um **cenário comum de sistemas reais**, muito próximo do que QAs encontram em projetos:

### 🧩 Conceitos abordados

* Classes e objetos
* Encapsulamento
* Herança
* Polimorfismo
* Organização de código em pacotes
* Importação correta de módulos

### 📌 Exemplo prático

* **Usuario**

  * Representa um usuário do sistema
  * Possui status ativo/inativo

* **Admin**

  * Herda de Usuario
  * Possui nível de acesso
  * Executa ações administrativas (ex: promover usuário)

👉 Esse modelo ajuda o QA a:

* Entender regras de permissão
* Criar cenários de teste baseados em perfis
* Ler código backend com mais segurança

---

## ▶️ Como Executar (Importante para QA)

### Scripts simples

```bash
python nome_do_arquivo.py
```

### Executar corretamente o módulo de POO

```bash
python -m POO.main
```

⚠️ Executar arquivos de pacotes diretamente pode gerar erros de importação.

---

## ❗ Erros Comuns no Dia a Dia de QA

### ❌ `ModuleNotFoundError: No module named 'POO'`

Causa: execução incorreta do módulo.

❌ Errado:

```bash
python POO/main.py
```

✅ Correto:

```bash
python -m POO.main
```

---

### ❌ Git — `non-fast-forward`

Erro comum ao versionar scripts de teste.

Solução:

```bash
git pull origin main
git push origin main
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Git
* GitHub

---

## 🚀 Próximos Passos (Evolução para QA)

Sugestões de evolução deste repositório:

* Testes automatizados com `pytest`
* Testes de API com `requests`
* Massa de dados para testes
* Estrutura de Page Objects (POM)
* Integração com CI/CD

---

## 👤 Autor

**Willian Narbona Aquino**
QA | Estudante de Automação
GitHub: [https://github.com/Narbona836](https://github.com/Narbona836)



