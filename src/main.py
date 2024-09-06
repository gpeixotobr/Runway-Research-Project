from utils import process_statistics_for_file, categorize_users

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

if __name__ == "__main__":
    main()
