import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_data(df):
    # Cria a pasta de saída se não existir
    os.makedirs("output", exist_ok=True)

    # Exemplo: gráfico de barras da primeira coluna numérica
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) == 0:
        print("Nenhuma coluna numérica encontrada para gráficos.")
        return

    col = numeric_cols[0]
    plt.figure(figsize=(10,6))
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(f"Distribuição de {col}")
    plt.savefig(f"output/hist_{col}.png")
    print(f"Gráfico salvo em: output/hist_{col}.png")
    plt.close()
