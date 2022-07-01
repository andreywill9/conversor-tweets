import pandas as pd
import os

for arquivo in os.listdir("tweets_csv"):
    if arquivo == "ARQUIVOS_CSV_AQUI":
        continue
    dataframe = pd.read_csv("tweets_csv/" + arquivo, sep=";")
    nome_novo_arquivo = arquivo[:-4]
    dataframe.to_json("tweets_json/" + nome_novo_arquivo + ".json", force_ascii=False, orient="records")
