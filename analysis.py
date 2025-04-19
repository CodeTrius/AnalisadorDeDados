def summarize_data(df):
    print("\n🔍 Informações gerais:")
    print(df.info())

    print("\n📊 Estatísticas descritivas:")
    print(df.describe())

    print("\n📈 Colunas disponíveis:")
    print(df.columns.tolist())
