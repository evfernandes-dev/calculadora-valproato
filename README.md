# 💊 Calculadora de Valproato (Depakene)

Aplicação desktop desenvolvida em **Python** para auxiliar no planejamento da dispensação de **Valproato 250 mg e 500 mg**, considerando a quantidade disponível com o paciente e a entrega por caixas fechadas.

O objetivo do projeto é tornar o processo de dispensação mais organizado, reduzir desperdícios e ajudar no melhor aproveitamento dos medicamentos disponíveis.

---

## 🎯 Por que este projeto foi criado

A calculadora foi desenvolvida para apoiar a rotina de dispensação em uma farmácia pública.

Em alguns casos, o paciente ainda possui comprimidos restantes de uma dispensação anterior. Antes de entregar novas caixas, essa quantidade pode ser considerada no planejamento dos meses seguintes.

A aplicação automatiza esse cálculo e ajuda a visualizar:

- quantos comprimidos o paciente já possui;
- quantos comprimidos serão necessários em cada mês;
- quantas caixas precisam ser entregues;
- quantos comprimidos ficarão de saldo para o mês seguinte.

Dessa forma, o sistema ajuda a reduzir cálculos manuais e possíveis erros durante o planejamento da dispensação.

---

## ⚙️ Como funciona

A aplicação considera que:

- cada caixa possui **50 comprimidos**;
- as caixas não são fracionadas;
- o usuário informa a apresentação do medicamento: **250 mg ou 500 mg**;
- é definida a quantidade de meses do planejamento;
- é informada a quantidade de comprimidos necessária por mês;
- também é possível informar uma sobra inicial já disponível com o paciente.

A partir desses dados, o sistema realiza o cálculo mês a mês.

### Fluxo básico

```text
Dados do paciente
      ↓
Quantidade necessária por mês
      ↓
Saldo disponível
      ↓
Cálculo de caixas necessárias
      ↓
Saldo para o próximo mês
```

---

## 🧮 Exemplo

Suponha que o paciente precise de:

```text
60 comprimidos por mês
```

e já possua:

```text
20 comprimidos
```

O programa considera primeiro esses 20 comprimidos e calcula somente a quantidade adicional necessária.

Como cada caixa contém 50 comprimidos, a aplicação determina automaticamente quantas caixas fechadas precisam ser entregues e qual será o saldo restante para o próximo período.

---

## 🖥️ Interface

A aplicação possui uma interface gráfica desenvolvida com **CustomTkinter**, permitindo realizar os cálculos sem utilizar o terminal.

A interface foi pensada para ser simples e rápida de utilizar durante a rotina de atendimento.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Lógica principal da aplicação |
| CustomTkinter | Interface gráfica |
| Git | Controle de versão |
| GitHub | Armazenamento e documentação do projeto |

---

## 📂 Estrutura do projeto

```text
calculadora-valproato/
│
├── app.py
├── calculadora.py
├── requirements.txt
└── README.md
```

### Arquivos

- `app.py` — interface gráfica da aplicação.
- `calculadora.py` — lógica responsável pelos cálculos de dispensação.
- `requirements.txt` — dependências necessárias para executar o projeto.
- `README.md` — documentação do projeto.

---

## ▶️ Como executar

### Pré-requisitos

Tenha instalado:

```text
Python 3.10 ou superior
```

### 1. Clone o repositório

```bash
git clone URL-DO-SEU-REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd calculadora-valproato
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute

```bash
python app.py
```

---

## 📦 Dependências

O projeto utiliza principalmente:

```text
customtkinter
```

As dependências podem ser instaladas automaticamente através do arquivo:

```text
requirements.txt
```

---

## 💡 Principais objetivos

- Reduzir cálculos manuais.
- Facilitar o planejamento da dispensação.
- Aproveitar primeiro o saldo já disponível com o paciente.
- Reduzir desperdício de medicamentos.
- Apoiar uma melhor organização dos recursos públicos.
- Tornar o processo mais rápido e padronizado.

---

## 🚀 Melhorias futuras

- [x] Cálculo por quantidade de comprimidos.
- [x] Consideração de saldo inicial.
- [x] Planejamento mês a mês.
- [x] Interface gráfica.
- [ ] Gerar relatório da dispensação.
- [ ] Exportar resultado em PDF.
- [ ] Salvar histórico de cálculos.
- [ ] Adicionar validação mais completa dos campos.
- [ ] Criar instalador para Windows.
- [ ] Gerar executável `.exe`.
- [ ] Adicionar testes automatizados.

---

## ⚠️ Aviso

Esta aplicação é uma ferramenta de **apoio administrativo e operacional para cálculo de quantidades**.

Ela não realiza prescrição, diagnóstico, alteração de dose ou recomendação terapêutica.

A dispensação deve seguir a prescrição apresentada, os protocolos aplicáveis e as orientações dos profissionais responsáveis.

---

## 👨‍💻 Autor

**Emanuel Vítor Fernandes Nascimento**

Desenvolvedor Back-End | Automação

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) • [GitHub](https://github.com/emanuelvitorfn7-gif)

---

## ⭐ Sobre o projeto

Este projeto foi criado a partir de uma necessidade prática, utilizando programação para automatizar um cálculo repetitivo e apoiar uma rotina real de trabalho.

Além da aplicação prática, o projeto também envolve conceitos de **Python, lógica de programação, interface gráfica, organização de código e desenvolvimento de soluções para problemas reais**.
