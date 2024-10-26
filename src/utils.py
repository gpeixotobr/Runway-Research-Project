import pandas as pd
from scipy.stats import mannwhitneyu

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
    Processa as estatísticas, matriz de correlação para um arquivo CSV específico.

    Args:
        filepath (str): Caminho para o arquivo CSV.
        prefix (str): Prefixo para os arquivos de saída (estatísticas, correlação).
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

def perform_mann_whitney_test(filepath1: str, filepath2: str, columns: list) -> pd.DataFrame:
    """
    Realiza o teste de Mann-Whitney para uma lista de colunas entre dois arquivos CSV.

    Args:
        filepath1 (str): Caminho para o primeiro arquivo CSV contendo os dados do primeiro grupo.
        filepath2 (str): Caminho para o segundo arquivo CSV contendo os dados do segundo grupo.
        columns (list): Lista de nomes das colunas a serem comparadas entre os arquivos.

    Returns:
        pd.DataFrame: DataFrame com o resultado do teste Mann-Whitney (estatística U e valor-p) para cada coluna.
    """
    # Carregar os dados dos arquivos
    df1 = load_data(filepath1)
    df2 = load_data(filepath2)
    
    # Realizar o teste para cada coluna especificada
    results = []
    for column in columns:
        # Realizar o teste de Mann-Whitney para cada coluna
        stat, p_value = mannwhitneyu(df1[column], df2[column], alternative='two-sided')
        
        # Adicionar os resultados em uma lista de dicionários
        results.append({
            "Coluna": column,
            "Estatística U": stat,
            "Valor-p": p_value
        })

    # Converter a lista de resultados em um DataFrame
    results_df = pd.DataFrame(results)

    save_to_csv(results_df, f'../output/mann_whitney.csv')
    