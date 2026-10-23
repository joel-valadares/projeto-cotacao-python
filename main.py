import pandas as pd
import requests


def buscar_cotacoes():
    # 1. Fazendo a requisição HTTP para a API pública AwesomeAPI
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    print("Buscando cotações atualizadas...")
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        # 2. Transformando o JSON em um DataFrame do Pandas
        # Convertemos o dicionário em uma lista de valores
        lista_moedas = list(dados_json.values())
        df = pd.DataFrame(lista_moedas)

        # 3. Limpeza e Seleção de Colunas relevantes com Pandas
        colunas_desejadas = {
            "name": "Moeda",
            "bid": "Valor_Compra",
            "ask": "Valor_Venda",
            "pctChange": "Variacao_Porcentagem",
        }

        df_limpo = df[list(colunas_desejadas.keys())].rename(
            columns=colunas_desejadas
        )

        print("\n--- Relatório de Cotações ---")
        print(df_limpo)

        # 4. Exportando para CSV (opcional)
        df_limpo.to_csv("cotacoes_atualizadas.csv", index=False)
        print("\nRelatório salvo em 'cotacoes_atualizadas.csv' com sucesso!")

    else:
        print(f"Erro ao acessar a API: Código {response.status_code}")


if __name__ == "__main__":
    buscar_cotacoes()