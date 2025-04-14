
---

### `docs/EDA.md` — Relatório de Insights do EDA

```markdown
# 📊 Relatório de Análise Exploratória (EDA)

Este relatório resume os principais insights extraídos a partir da análise exploratória do dataset `cancelamentos.csv`, com o objetivo de identificar padrões de comportamento relacionados ao cancelamento de clientes.

---

## 🔍 Visão Geral

- Total de registros: 881.666
- Coluna alvo: `cancelou`
- Dados ausentes removidos com `.dropna()`

---

## 💥 Principais Insights

### 1. 🚺 Alta taxa de cancelamento entre mulheres

- O público feminino apresenta uma taxa de churn visivelmente maior.
- Pode indicar insatisfação ou desajuste com o produto/serviço oferecido.

**Recomendação:** Investigar feedbacks e criar segmentações específicas para o público feminino.

---

### 2. 🗓️ Assinatura mensal = Churn certo

- 100% dos clientes com **assinatura do tipo mensal** cancelam.
- Forte indício de que o modelo de pagamento mensal não oferece fidelização.

**Recomendação:** Reavaliar a atratividade das assinaturas mensais ou oferecer upgrades automáticos.

---

### 3. 👶👴 Faixa etária crítica

- Até 20 anos: ~50% de cancelamento
- Acima de 50 anos: 100% de cancelamento

**Recomendação:** Oferecer experiência personalizada por faixa etária. Verificar usabilidade e canais de comunicação.

---

### 4. ⏰ Atrasos acima de 20 dias = cancelamento total

- Todos os clientes com mais de 20 dias de atraso nos pagamentos cancelaram.

**Recomendação:** Ações preventivas e notificações antes desse limite.

---

### 5. ☎️ Call Center como alerta de risco

- Clientes que ligam mais de 4 vezes para o call center sempre cancelam.

**Recomendação:** Criar score de risco com base no número de chamadas. Investigar tempo médio de resolução.

---

## 📈 Visualizações Utilizadas

- Histogramas e boxplots para variáveis contínuas
- Gráficos de barras segmentados por `cancelou`
- Heatmap de correlação
- Análises condicionais com `.groupby()` e `.mean()`

---

## 🧠 Conclusão

A análise revelou padrões claros de comportamento que podem ser utilizados para:

- Criar políticas de retenção personalizadas
- Ajustar planos e modelos de assinatura
- Antecipar o risco de churn com base em variáveis-chave

Esses insights servirão de base para a próxima etapa: **modelagem preditiva**.

---
