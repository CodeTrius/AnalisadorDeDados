from analysis import summarize_data
from visualization import plot_data
import pandas as pd

# Caminho para o arquivo CSV
file_path = "data/exemplo.csv"

def main():
    try:
        # Carrega o dataset
        df = pd.read_csv(file_path)
        print(f"Arquivo carregado com sucesso: {file_path}")

        # Resumo
        summarize_data(df)

        # Gráficos
        plot_data(df)

    except Exception as e:
        print(f"Erro ao carregar ou processar o arquivo: {e}")

if __name__ == "__main__":
    main()
