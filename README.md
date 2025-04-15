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

Dataset

O dataset contém informações de 881.666 clientes, com variáveis relacionadas a:

    Demografia (idade, sexo)

    Comportamento (frequência de uso, atraso, ligações)

    Tipo de assinatura e contrato

    Interações com o call center

    Gasto total

    Coluna alvo: cancelou (1 = cancelou, 0 = manteve)

Análise Exploratória (EDA)

A EDA foi realizada no notebook [1_EDA.ipynb](1_EDA.ipynb), e os principais insights foram organizados no relatório [docs/EDA.md](docs/EDA.md).
 Highlights:

    100% dos clientes com assinatura mensal cancelam

    Clientes que ligam mais de 4x para o call center sempre cancelam

    Acima de 20 dias de atraso, a taxa de churn é total

    Jovens (<20) e idosos (>50) têm maiores taxas de cancelamento

    O público feminino apresenta maior tendência ao churn

 Tecnologias Utilizadas

    Python 3.12.7

    Pandas, NumPy, Matplotlib, Seaborn

    Jupyter Notebooks

    Conda (ambiente virtual)

    Git/GitHub

 Próximos Passos

Feature Engineering (tratamento, encoding, padronização)

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

Durante o treinamento, foi observado que o modelo SVM (`SVC` com `probability=True`) apresentou alto custo computacional, levando várias horas para concluir o processo. 

Essa decisão de manter o modelo mesmo com custo elevado reflete uma escolha consciente de simular um cenário de produção real, onde diferentes modelos são avaliados com profundidade para obter o melhor desempenho possível — mesmo que isso demande mais recursos de processamento.

---

### Automação e Modularização

Foi criado um script `src/train.py` para permitir o reuso e treinamento automático dos modelos, fora do ambiente Jupyter. Isso permite escalar o processo de forma eficiente, e também integra com pipelines futuros de deploy.

Para executar:

```bash
python src/train.py
```

### Autor

Mario Pereira | Cientista de Dados em formação

Sempre buscando soluções fora da caixa e insights que transformam números em ação.

Contatos: [E-mail](mailto:omario.pereira96@gmail.com) • [LinkedIn](https://www.linkedin.com/in/omario-silva96) • [GitHub](https://github.com/M-4vlis)