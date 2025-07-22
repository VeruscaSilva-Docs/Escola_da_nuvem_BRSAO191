# Calculadora de Preço Total

# Informações do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

# Cálculo do preço total
preco_total = preco_unitario * quantidade

# Exibindo as informações
print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", round(preco_total, 2))
Saída esperada:
yaml
Copiar
Editar
Produto: Cadeira Infantil
Preço unitário: R$ 12.4
Quantidade: 3
Preço total: R$ 37.2
Se quiser formatar o preço com duas casas decimais fixas, pode usar:

python
Copiar
Editar
print("Preço total: R$ {:.2f}".format(preco_total))
Quer que eu mostre isso em outra linguagem também (como JavaScript ou C)?




