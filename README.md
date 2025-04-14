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

📊 Dataset

O dataset contém informações de 881.666 clientes, com variáveis relacionadas a:

    Demografia (idade, sexo)

    Comportamento (frequência de uso, atraso, ligações)

    Tipo de assinatura e contrato

    Interações com o call center

    Gasto total

    Coluna alvo: cancelou (1 = cancelou, 0 = manteve)

🔍 Análise Exploratória (EDA)

A EDA foi realizada no notebook 1_EDA.ipynb, e os principais insights foram organizados no relatório docs/EDA.md.
🔥 Highlights:

    100% dos clientes com assinatura mensal cancelam

    Clientes que ligam mais de 4x para o call center sempre cancelam

    Acima de 20 dias de atraso, a taxa de churn é total

    Jovens (<20) e idosos (>50) têm maiores taxas de cancelamento

    O público feminino apresenta maior tendência ao churn

🛠️ Tecnologias Utilizadas

    Python 3.12.7

    Pandas, NumPy, Matplotlib, Seaborn

    Jupyter Notebooks

    Conda (ambiente virtual)

    Git/GitHub

💡 Próximos Passos

Feature Engineering (tratamento, encoding, padronização)

Modelagem preditiva (classificação)

Métricas e avaliação

    Deploy e dashboard com Streamlit ou Flask

👨‍💻 Autor

Mario Pereira | Cientista de Dados em formação
💬 Sempre buscando soluções fora da caixa e insights que transformam números em ação.
📫 Contato: [omario.pereira96@gmail.com] • [LinkedIn](www.linkedin.com/in/omario-silva96) • [GitHub](https://github.com/M-4vlis)