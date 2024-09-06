# Categorização de Usuários e Processamento Estatístico para Testes de Usabilidade

Neste repositório podem ser encontrados os arquivos necessários para a categorização dos usuários e o processamento estatístico em testes de usabilidade fundamentados na metodologia adotada na pesquisa com a plataforma de edição de vídeos **Runway**.

## Arquivos

- **`main.py`**: Contém o fluxo principal de execução do processo de categorização dos usuários e o processamento estatístico. Este arquivo integra as funções necessárias para ler os dados, calcular estatísticas, e salvar os resultados.
  
- **`utils.py`**: Inclui funções utilitárias que suportam o processamento dos dados. Este arquivo contém funcionalidades auxiliares para a execução correta dos processos descritos em `main.py`.

## Funcionalidades

### Categorização de Usuários
O sistema categoriza os usuários com base nas respostas fornecidas em questionários, distinguindo-os entre "Iniciante" e "Avançado", de acordo com o tempo de uso semanal e a familiaridade com ferramentas de edição de vídeo.

### Processamento Estatístico
A ferramenta realiza análises estatísticas dos dados de usabilidade, incluindo:
- Cálculo de estatísticas descritivas (média, mediana, desvio padrão, coeficiente de variação).
- Cálculo da matriz de correlação.
- Teste de normalidade utilizando o teste de Shapiro-Wilk.

## Como Utilizar

1. Certifique-se de ter os arquivos de dados no formato `.csv`.
2. Execute o script `main.py`, que coordenará o processo de categorização e análise estatística.
3. Os resultados das análises serão gerados em arquivos CSV para visualização posterior.

## Pré-requisitos

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `scipy`

## Metodologia

O processo descrito neste repositório está fundamentado na metodologia de avaliação de usabilidade, especialmente voltado para a plataforma de edição de vídeos **Runway**. Os dados são tratados para fornecer insights sobre o perfil dos usuários e a normalidade dos dados coletados nos testes de usabilidade.
