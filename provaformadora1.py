# Sistema de pedidos de uma lanchonete!

# Tabela de preços
menu = {
    1: {"nome": "Hambúrguer", "preco": 20.00},
    2: {"nome": "Pizza", "preco": 15.00},
    3: {"nome": "Refrigerante", "preco": 5.00}
}

# Lista para armazenar pedidos !
pedidos = []

print("=== Bem-vindo à Lanchonete ===")

while True:
    print("\nEscolha uma das opções de produto:")
    print("1 - Hambúrguer")
    print("2 - Pizza")
    print("3 - Refrigerante")
    print("0 - Sair do sistema")

    opcao_input = input("Digite a opção desejada: ")

    # Validação: verifica se é número
    if not opcao_input.isdigit():
        print(" Entrada inválida! Digite apenas números.")
        continue

    opcao = int(opcao_input)

    # Opção de sair
    if opcao == 0:
        break

    # Validação da opção
    if opcao not in menu:
        print(" Opção inválida! Tente novamente.")
        continue

    # Produto escolhido
    produto = menu[opcao]["nome"]
    preco = menu[opcao]["preco"]

    print(f"\nVocê escolheu a opção - {produto}")

    quantidade_input = input("Qual a quantidade desejada? ")

    # Validação da quantidade
    if not quantidade_input.isdigit():
        print(" Quantidade inválida! Digite apenas números.")
        continue

    quantidade = int(quantidade_input)

    if quantidade <= 0:
        print(" A quantidade deve ser maior que zero.")
        continue

    # Cálculo do valor
    total_item = quantidade * preco

    print(f"\nVocê escolheu: {produto} - qtd: {quantidade} - Valor total: R$ {total_item:.2f}")

    # Armazenar pedido
    pedidos.append({
        "produto": produto,
        "quantidade": quantidade,
        "total": total_item
    })

# Encerramento
print("\n=== Encerrando pedido... ===")
print("Seu pedido foi encerrado com sucesso!")

# Verifica se houve pedidos
if len(pedidos) == 0:
    print("Nenhum item foi selecionado.")
else:
    print("\nOs itens do seu pedido são:")

    total_geral = 0

    for item in pedidos:
        print(f"{item['produto']} - qtd: {item['quantidade']} - Valor total: R$ {item['total']:.2f}")
        total_geral += item["total"]

    print(f"\nValor total: R$ {total_geral:.2f}")

print("\nObrigado pela preferência! ")