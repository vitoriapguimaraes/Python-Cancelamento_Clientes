# Cancelamentos de Clientes em Serviço de Assinatura: Análise e Redução

> Projeto de Data Science para identificar os principais fatores de cancelamento em serviços de assinatura, propor soluções para retenção e gerar visualizações interativas dos dados.

![Demonstração do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/2.%20Cancelamento%20de%20Clientes/results/resuls_show.png)

## Funcionalidades Principais

- Análise dos fatores associados ao cancelamento de clientes.
- Segmentação comportamental e demográfica dos clientes.
- Visualizações gráficas interativas dos principais insights.
- Geração automática de gráficos para cada variável relevante.
- Relatório de insights para estratégias de retenção.

## Resultados e Conclusões

Principais descobertas:

- Contratos mensais apresentam maior taxa de cancelamento.
- Clientes com mais de 20 dias de atraso têm maior probabilidade de cancelar.
- Alta frequência de ligações ao call center está associada a maior taxa de cancelamento.
- Perfil demográfico: clientes acima de 50 anos com baixo gasto total (< R$ 500) são mais propensos ao cancelamento.

Esses resultados fundamentam estratégias de retenção personalizadas e melhorias no atendimento.

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly
- Jupyter Notebook

## Como Executar

1. Clone o repositório:

   ```
   git clone https://github.com/vitoriapguimaraes/Python-dataScience-Cancelamento_Clientes.git
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

   Ou manualmente:

   ```
   pip install pandas plotly notebook kaleido nbformat
   ```

3. Executar o Notebook:

   ```
   jupyter notebook app.ipynb
   ```

   Ou abra o arquivo no VS Code e execute as células sequencialmente.

## Estrutura do Projeto

```
├── dataset/
│   └── cancelamentos_sample.csv
├── results/
│   └── ... (gráficos e relatórios gerados)
├── scripts/
│   ├── app.ipynb
│   └── app.py
├── requirements.txt
└── README.md
```

## Status

- ✅ Concluído

> Veja as [issues abertas](https://github.com/vitoriapguimaraes/Python-dataScience-Cancelamento_Clientes/issues) para sugestões de melhorias e próximos passos.

## Mais Sobre Mim

Acesse os arquivos disponíveis na [Pasta Documentos](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
