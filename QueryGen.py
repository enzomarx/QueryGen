import pandas as pd

# Lê os IDs dos produtos de um arquivo CSV
# O CSV deve ter uma coluna chamada 'nIdProduto'
df = pd.read_csv(r"C:\Users\you\Documents\produtosid.csv")
produtos_ids = df['nIdProduto'].tolist()

queries = []

for n_id_produto in produtos_ids:
    query = f"""let
    url = "https://xxxxxxxxxxxxx/api/v1/estoque/resumo/",
    
    // corpo JSON
    body = "{{\"call\": \"ObterEstoqueProduto\", \"app_key\": \"yyyyyyyyyyyyyyyy\", \"app_secret\": \"xxxxxxxxxxxxxxxxx\", \"param\": [{{\"cEAN\": \"\", \"nIdProduto\": {n_id_produto}, \"cCodigo\": \"\", \"xCodigo\": \"\", \"dDia\": \"03/10/2024\"}}]}}",
    
    // requisição POST
    response = Web.Contents(url, [
        Content = Text.ToBinary(body),
        Headers = [#"Content-Type" = "application/json"]
    ]),
    
    // Converte a resposta 
    jsonResponse = Json.Document(response),
    
    listaEstoque = jsonResponse[listaEstoque],
    
    estoqueTable = Table.FromList(listaEstoque, Splitter.SplitByNothing(), {{"Estoque"}}),
    
    expandedTable = Table.ExpandRecordColumn(estoqueTable, "Estoque", {{"fisico", "nPrecoUltComp", "nPrevisaoEntrada", "nPrevisaoSaida", "nSaldo"}}),
    
    cCodigo = jsonResponse[cCodigo],
    cDescricao = jsonResponse[cDescricao],
    cUnidade = jsonResponse[cUnidade],  
    
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
