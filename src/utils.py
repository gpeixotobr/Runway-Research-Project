import pandas as pd
from scipy.stats import shapiro

def load_data(filepath: str) -> pd.DataFrame:
    """
    Carrega o arquivo CSV e remove a coluna 'Nome'.

    Args:
        filepath (str): Caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados, sem a coluna 'Nome'.
    """
    data = pd.read_csv(filepath)
    data = data.drop(['Nome'], axis=1)
    return data

def calculate_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula estatísticas (média, mediana, desvio padrão e coeficiente de variação) para o DataFrame.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados numéricos.

    Returns:
        pd.DataFrame: DataFrame com as estatísticas calculadas (média, mediana, desvio padrão e coeficiente de variação).
    """
    statistics = pd.DataFrame(data={
        "mean": data.mean(),
        "median": data.median(),
        "std": data.std()
    })
    statistics['var_coeff'] = statistics["std"] * 100 / statistics['mean']
    statistics = statistics.fillna(0)
    return statistics

def calculate_correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a matriz de correlação para o DataFrame e substitui valores ausentes por 0.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados numéricos.

    Returns:
        pd.DataFrame: DataFrame com a matriz de correlação.
    """
    data_corr = data.corr()
    data_corr = data_corr.fillna(0)
    return data_corr

def perform_shapiro_test(data: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza o teste de Shapiro-Wilk em todas as colunas do DataFrame.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados numéricos.

    Returns:
        pd.DataFrame: DataFrame com os resultados do teste de Shapiro-Wilk para cada coluna.
    """
    results = []
    for column in data.columns:
        stat, p_value = shapiro(data[column])
        print(f'Coluna: {column} - Statistic: {stat}, p-value: {p_value}')
        results.append({'Coluna': column, 'W-Statistic': stat, 'p-value': p_value})
    return pd.DataFrame(results)

def categorize_user(row: pd.Series) -> str:
    """
    Categoriza o usuário como 'Avançado' ou 'Iniciante' com base no uso de ferramentas de edição de vídeo.

    Args:
        row (pd.Series): Linha de dados contendo as respostas do questionário.

    Returns:
        str: Categoria do usuário ('Avançado' ou 'Iniciante').
    """
    if row["Você faz uso frequente de alguma ferramenta de edição de vídeo?"] == "Sim":
        if row["Quanto tempo você utiliza algum software de edição de vídeo por semana?"] in ["Mais de 36h", "Entre 24h e 36h", "Entre 16h e 24h"]:
            return "Avançado"
    return "Iniciante"

def categorize_users(filepath: str, output_filename: str) -> None:
    """
    Carrega os dados do questionário, categoriza os usuários e salva os resultados em um arquivo CSV.

    Args:
        filepath (str): Caminho para o arquivo CSV do questionário.
        output_filename (str): Caminho para o arquivo CSV de saída com as categorias dos usuários.
    """
    df = pd.read_csv(filepath)
    df["Categoria"] = df.apply(categorize_user, axis=1)
    df.to_csv(output_filename, index=False)


def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Salva o DataFrame em um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        filename (str): Caminho do arquivo CSV a ser salvo.
    """
    df.to_csv(filename, index=False)

def process_statistics_for_file(filepath: str, prefix: str) -> None:
    """
    Processa as estatísticas, matriz de correlação e teste de Shapiro-Wilk para um arquivo CSV específico.

    Args:
        filepath (str): Caminho para o arquivo CSV.
        prefix (str): Prefixo para os arquivos de saída (estatísticas, correlação e teste Shapiro-Wilk).
    """
    # Carregar os dados
    data = load_data(filepath)
    
    # Calcular e salvar estatísticas
    statistics = calculate_statistics(data)
    print(f'Gerou estatísticas para {filepath}')
    save_to_csv(statistics, f'../output/{prefix}_estatisticas.csv')

    # Calcular e salvar a matriz de correlação
    data_corr = calculate_correlation_matrix(data)
    save_to_csv(data_corr, f'../output/{prefix}_matriz_correlacao.csv')

    # Realizar o teste de Shapiro-Wilk e salvar os resultados
    shapiro_results = perform_shapiro_test(data)
    save_to_csv(shapiro_results, f'../output/{prefix}_shapiro.csv')