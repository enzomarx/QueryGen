# QueryGen

**QueryGen** é uma ferramenta para gerar automaticamente consultas em formato M Query (usado no Power BI) para obter informações de estoque de produtos via a API da Omie. Esta aplicação facilita a criação de consultas em lote para múltiplos produtos a partir de um arquivo CSV, gerando um arquivo `.txt` contendo todas as queries.

## Funcionalidades

- Ler um arquivo CSV contendo os IDs dos produtos (`nIdProduto`).
- Gerar consultas M Query para cada produto listado no CSV.
- Salvar todas as consultas geradas em um único arquivo de texto (`queries.txt`).

## Pré-requisitos

Para usar o **QueryGen**, é necessário ter instalado:

- **Python 3.x**
- Biblioteca **pandas** para manipulação de dados.

Você pode instalar o pandas com o comando:

```sh
pip install pandas
```

## Como usar

1. **Prepare o CSV**: 
   - Crie um arquivo chamado `produtos.csv` contendo uma coluna chamada `nIdProduto` com os IDs dos produtos que você deseja obter informações de estoque.

   Exemplo do conteúdo do `produtos.csv`:
   ```
   nIdProduto
   1014729578
   1014729579
   1014729580
   ```

2. **Execute o Script**:
   - Execute o script Python para gerar as consultas.

   ```sh
   python querygen.py
   ```

3. **Resultado**:
   - Após executar o script, um arquivo chamado `queries.txt` será gerado no mesmo diretório. Esse arquivo conterá todas as consultas para os produtos listados no CSV.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias.

## Licença

Este projeto é licenciado sob a licença MIT 
