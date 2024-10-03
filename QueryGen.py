import pandas as pd

# Lê os IDs dos produtos de um arquivo CSV
# O CSV deve ter uma coluna chamada 'nIdProduto'
df = pd.read_csv(r"C:\Users\ema\Documents\produtosid.csv")
produtos_ids = df['nIdProduto'].tolist()

queries = []

for n_id_produto in produtos_ids:
    query = f"""let
    // Define a URL da API
    url = "https://app.omie.com.br/api/v1/estoque/resumo/",
    
    // Define o corpo da requisição em formato JSON
    body = "{{\"call\": \"ObterEstoqueProduto\", \"app_key\": \"917515082484\", \"app_secret\": \"d15f8e01a6fb22915ebd9770e1407fec\", \"param\": [{{\"cEAN\": \"\", \"nIdProduto\": {n_id_produto}, \"cCodigo\": \"\", \"xCodigo\": \"\", \"dDia\": \"03/10/2024\"}}]}}",
    
    // Executa a requisição POST
    response = Web.Contents(url, [
        Content = Text.ToBinary(body),
        Headers = [#"Content-Type" = "application/json"]
    ]),
    
    // Converte a resposta JSON para um formato de tabela
    jsonResponse = Json.Document(response),
    
    // Extraí a lista de estoque
    listaEstoque = jsonResponse[listaEstoque],
    
    // Converte a lista de estoque em uma tabela
    estoqueTable = Table.FromList(listaEstoque, Splitter.SplitByNothing(), {{"Estoque"}}),
    
    // Expande a tabela para obter os campos desejados
    expandedTable = Table.ExpandRecordColumn(estoqueTable, "Estoque", {{"fisico", "nPrecoUltComp", "nPrevisaoEntrada", "nPrevisaoSaida", "nSaldo"}}),
    
    // Adiciona informações de cCodigo, cDescricao e cUnidade
    cCodigo = jsonResponse[cCodigo],
    cDescricao = jsonResponse[cDescricao],
    cUnidade = jsonResponse[cUnidade],  // Adiciona cUnidade
    
    // Adiciona colunas para cCodigo, cDescricao e cUnidade na tabela final
    finalTable = Table.AddColumn(expandedTable, "Codigo do Produto", each cCodigo),
    finalTableWithDescription = Table.AddColumn(finalTable, "Descricao do Produto", each cDescricao),
    finalTableWithUnit = Table.AddColumn(finalTableWithDescription, "Unidade do Produto", each cUnidade),
    #"Reordered Columns" = Table.ReorderColumns(finalTableWithUnit, {{"Codigo do Produto", "Descricao do Produto", "Unidade do Produto", "fisico", "nSaldo", "nPrevisaoEntrada", "nPrevisaoSaida", "nPrecoUltComp"}})  // Adiciona cUnidade
in
    // Retorna a tabela final
    #"Reordered Columns"""
    
    queries.append(query)

with open("queries.txt", "w") as file:
    for query in queries:
        file.write(query + "\n\n")  
