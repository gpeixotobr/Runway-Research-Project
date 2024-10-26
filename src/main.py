from utils import process_statistics_for_file, categorize_users, perform_mann_whitney_test

def main() -> None:
    """
    Função principal que processa as estatísticas para os arquivos Dados After.csv e Dados Runway.csv.
    """
    # Processar estatísticas para Dados After.csv
    process_statistics_for_file('../data/dados_after.csv', 'after')

    # Processar estatísticas para Dados Runway.csv
    process_statistics_for_file('../data/dados_runway.csv', 'runway')

    # Categorizar usuários e salvar em um CSV
    categorize_users('../data/questionario_de_delineamento_do_perfil_do_usuario.csv', '../output/categoria_usuario.csv')

    perform_mann_whitney_test('../data/dados_after.csv', '../data/dados_runway.csv', ['T1','T2','T3','T4','T5'])

if __name__ == "__main__":
    main()
