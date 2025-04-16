# Churn Prediction Project

Este projeto tem como objetivo prever o cancelamento de clientes com base em seus comportamentos, características demográficas e interações com a empresa. A ideia é usar esse conhecimento para **reduzir churn**, **aumentar retenção** e tomar **decisões estratégicas de negócio**.

---

## Estrutura do Projeto

```bash
churn-prediction-project/
├── data/
│   ├── raw/               # Dados originais
│   └── processed/         # Dados limpos e transformados
├── notebooks/
│   └── 1_EDA.ipynb        # Análise exploratória de dados
├── outputs/               # Imagens, gráficos e artefatos gerados
├── src/                   # Scripts Python para reutilização
│   └── __init__.py
├── docs/
│   └── EDA.md             # Relatório de insights do EDA
├── .gitignore
├── requirements.txt
├── README.md
└── cancelamentos.csv      # Dataset original
```

## 📁 Dataset

O dataset contém informações de 881.666 clientes, com variáveis relacionadas a:

    Demografia (idade, sexo)

    Comportamento (frequência de uso, atraso, ligações)

    Tipo de assinatura e contrato

    Interações com o call center

    Gasto total

    Coluna alvo: cancelou (1 = cancelou, 0 = manteve)

## Análise Exploratória (EDA)

A EDA foi realizada no notebook [1_EDA.ipynb](1_EDA.ipynb), e os principais insights foram organizados no relatório [docs/EDA.md](docs/EDA.md).
 Highlights:

    100% dos clientes com assinatura mensal cancelam

    Clientes que ligam mais de 4x para o call center sempre cancelam

    Acima de 20 dias de atraso, a taxa de churn é total

    Jovens (<20) e idosos (>50) têm maiores taxas de cancelamento

    O público feminino apresenta maior tendência ao churn

## 🧰 Tecnologias Utilizadas

- Python 3.12.7
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Imbalanced-learn
- Jupyter Notebooks
- Streamlit
- Conda (ambiente virtual)
- Git + GitHub

✅ Feature Engineering realizada com encoding, balanceamento e padronização dos dados

## Modelagem Preditiva

A modelagem foi feita em duas abordagens distintas:

### Abordagem A — Dataset Original
Utilizamos os dados como estavam, com alta proporção de clientes cancelando (≈70%). Isso nos permite observar o comportamento dos modelos quando o churn é dominante.

### Abordagem B — Dataset Simulado com Churn ≈ 30%
Criamos uma versão mais realista da base, simulando uma situação de mercado onde a maioria dos clientes permanece. Essa abordagem visa avaliar o desempenho dos modelos em cenários mais alinhados com a realidade de negócios.

> ⚠️ Nota: A base original apresenta uma distribuição invertida (mais clientes cancelam do que permanecem). Veja como isso foi tratado no [relatório de EDA](docs/EDA.md#consideração-estratégica-distribuição-do-churn).

Ambas as versões foram testadas com os seguintes modelos:
- Regressão Logística
- Árvore de Decisão
- Random Forest
- Gradient Boosting
- SVM

As métricas avaliadas foram:
- Acurácia
- F1-score
- ROC AUC
- Matriz de Confusão

---

### Observações sobre performance

> ⚡ Devido ao alto custo computacional do `SVC` tradicional, optamos por utilizar o `SGDClassifier` com função de perda `hinge`, que implementa um classificador linear semelhante ao SVM, porém muito mais eficiente em grandes volumes de dados.

---

### Automação e Modularização

Foi criado um script `src/train.py` para permitir o reuso e treinamento automático dos modelos, fora do ambiente Jupyter. Isso permite escalar o processo de forma eficiente, e também integra com pipelines futuros de deploy.

Para executar:

```bash
python src/train.py
```

### 🏆 Modelo Final

Após testar 5 algoritmos em duas abordagens de dataset (base original e base simulada com 30% de churn), o modelo escolhido para deploy foi:

**Random Forest Classifier**, com performance:

- F1-score: 0.999 (base simulada)
- Acurácia: 0.9995
- ROC AUC: 1.000

Além da alta performance, o modelo foi escolhido por sua robustez, estabilidade, e boa interpretabilidade via análise de importância de variáveis.

O modelo final foi treinado com a base **balanceada via SMOTE** e **ajustada para refletir uma distribuição de churn mais próxima do mercado real**.

## 🖥️ Deploy Interativo com Streamlit

Para facilitar a visualização dos resultados e permitir a utilização prática do modelo, foi desenvolvido um aplicativo interativo com **Streamlit**.  

O app permite:
- Entrada manual de dados de um cliente
- Upload de um arquivo CSV com múltiplos clientes
- Visualização das previsões e probabilidades
- Download do resultado em CSV

### ▶️ Como executar o app

1. Instale os pacotes:

```bash
pip install -r requirements.txt
```

2. Rode o app com:

```bash
streamlit run app/streamlit_app.py
```

3. O navegador será aberto automaticamente em `http://localhost:8501`

---

### 📎 Exemplo de entrada (CSV):

```csv
sexo,tempo_como_cliente,frequencia_uso,ligacoes_callcenter,dias_atraso,total_gasto,meses_ultima_interacao,idade,assinatura_Standard,assinatura_Premium,duracao_contrato_Monthly,duracao_contrato_Quarterly
1,15,12,2,3,1230.50,5,35,1,0,0,1
0,30,8,5,21,760.00,8,58,0,1,1,0
```

### Autor

Mario Pereira | Cientista de Dados em formação

Sempre buscando soluções fora da caixa e insights que transformam números em ação.

Contatos: [E-mail](mailto:omario.pereira96@gmail.com) • [LinkedIn](https://www.linkedin.com/in/omario-silva96) • [GitHub](https://github.com/M-4vlis)